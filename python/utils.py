from __future__ import annotations
from gceutils import grepr_dataclass, enforce_argument_types
from typing import Any
import pmp_manip as p

INPUT_COMPATIBLE_T = list[p.SRBlock] | p.SRBlock | str | bool | p.SRDropdownValue


@grepr_dataclass()
class InputValue:
    value: INPUT_COMPATIBLE_T

    def as_type[_T: p.SRInputValue](self, input_type: type[_T]) -> _T:
        match input_type:
            case p.SRBlockAndTextInputValue:
                if isinstance(self.value, p.SRBlock):
                    return input_type(block=self.value, immediate="")
                elif isinstance(self.value, str):
                    return input_type(block=None, immediate=self.value)
                elif isinstance(self.value, bool):
                    return input_type(
                        block=p.SRBlock(opcode="&operators::true" if self.value else "&operators::false"),
                        immediate="",
                    )
                else: raise ValueError(self.value, type(self.value))

            case p.SRBlockAndDropdownInputValue:
                if isinstance(self.value, p.SRBlock):
                    return input_type(block=self.value, dropdown=None)
                elif isinstance(self.value, p.SRDropdownValue):
                    return input_type(block=None, dropdown=self.value)
                else: raise ValueError(self.value)

            case p.SRBlockAndBoolInputValue:
                if isinstance(self.value, p.SRBlock):
                    return input_type(block=self.value, immediate=False)
                elif isinstance(self.value, bool):
                    return input_type(block=None, immediate=self.value)
                else: raise ValueError(self.value)

            case p.SRBlockOnlyInputValue | p.SREmbeddedBlockInputValue:
                if isinstance(self.value, p.SRBlock):
                    return input_type(block=self.value)
                else: raise ValueError(self.value)

            case p.SRScriptInputValue:
                if isinstance(self.value, list):
                    # and all(isinstance(item, p.SRBlock) for item in self.value)
                    return input_type(blocks=self.value)
                else: raise ValueError(self.value)

            case _:
                raise ValueError()

    @enforce_argument_types
    @staticmethod
    def try_as_input[_T: p.SRInputValue](value: INPUT_COMPATIBLE_T | InputValue | Any, input_type: type[_T]) -> _T | Any:
        if isinstance(value, (list, p.SRBlock, str, bool, p.SRDropdownValue)):
            return InputValue(value).as_type(input_type)
        elif isinstance(value, InputValue):
            return value.as_type(input_type)
        else:
            return value


__all__ = ["InputValue"]
