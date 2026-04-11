from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class argument:

    @staticmethod
    def reporter_string_number() -> p.SRBlock:
        return p.SRBlock(
            opcode="&customblocks::custom block text arg [ARGUMENT]",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def reporter_boolean() -> p.SRBlock:
        return p.SRBlock(
            opcode="&customblocks::custom block boolean arg [ARGUMENT]",
            inputs={},
            dropdowns={},
        )
