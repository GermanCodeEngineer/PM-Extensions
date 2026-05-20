from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class procedures:

    class definition(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::define custom block", inputs={}, dropdowns={}
            )

    class definition_return(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::define custom block reporter",
                inputs={},
                dropdowns={},
            )

    class prototype(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::#CUSTOM BLOCK PROTOTYPE", inputs={}, dropdowns={}
            )

    class call(ThirdBlock):

        def __init__(self):
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    class return_(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::return (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class set(ThirdBlock):

        def __init__(self, param: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.param = param
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::set (PARAM) to (VALUE)",
                inputs={
                    "PARAM": ThirdInputValue.as_input(
                        self.param, p.SRBlockOnlyInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )
