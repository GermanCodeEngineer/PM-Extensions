from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class jwDate:

    @staticmethod
    def now() -> p.SRBlock:
        return p.SRBlock(opcode="&jwDate::now", inputs={}, dropdowns={})

    @staticmethod
    def epoch() -> p.SRBlock:
        return p.SRBlock(opcode="&jwDate::unix epoch", inputs={}, dropdowns={})

    @staticmethod
    def parse(input: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwDate::parse (INPUT)",
            inputs={"INPUT": InputValue.try_as_input(input, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )
