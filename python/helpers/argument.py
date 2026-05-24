from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class argument:

    @grepr_dataclass()
    class reporter_string_number(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::custom block text arg [ARGUMENT]",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class reporter_boolean(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&customblocks::custom block boolean arg [ARGUMENT]",
                inputs={},
                dropdowns={},
            )
