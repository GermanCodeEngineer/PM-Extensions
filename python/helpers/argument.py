from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class argument:

    class reporter_string_number(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::custom block text arg [ARGUMENT]",
                inputs={},
                dropdowns={},
            )

    class reporter_boolean(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::custom block boolean arg [ARGUMENT]",
                inputs={},
                dropdowns={},
            )
