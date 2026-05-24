from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwDate:

    @grepr_dataclass()
    class now(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwDate::now", inputs={}, dropdowns={})

    @grepr_dataclass()
    class epoch(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwDate::unix epoch", inputs={}, dropdowns={})

    @grepr_dataclass()
    class parse(ThirdBlock):
        input: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwDate::parse (INPUT)",
                inputs={
                    "INPUT": ThirdInputValue.as_input(
                        self.input, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )
