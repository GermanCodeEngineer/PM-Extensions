from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class argument:

    @grepr_dataclass()
    class reporter_string_number(ThirdBlock):
        OPCODE = "&customblocks::custom block text arg [ARGUMENT]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class reporter_boolean(ThirdBlock):
        OPCODE = "&customblocks::custom block boolean arg [ARGUMENT]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
