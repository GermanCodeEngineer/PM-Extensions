from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class procedures:

    @grepr_dataclass()
    class definition(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::define custom block", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class definition_return(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::define custom block reporter",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class prototype(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::#CUSTOM BLOCK PROTOTYPE", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class call(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    @grepr_dataclass()
    class return_(ThirdBlock):
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class set(ThirdBlock):
        param: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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
