from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwDate:

    class now(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwDate::now", inputs={}, dropdowns={})

    class epoch(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&jwDate::unix epoch", inputs={}, dropdowns={})

    class parse(ThirdBlock):

        def __init__(self, input: INPUT_COMPATIBLE_T):
            self.input = input

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
