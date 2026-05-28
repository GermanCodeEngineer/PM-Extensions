from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class argument:

    @grepr_dataclass()
    class reporter_string_number(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::custom block text arg [ARGUMENT]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class reporter_boolean(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::custom block boolean arg [ARGUMENT]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
