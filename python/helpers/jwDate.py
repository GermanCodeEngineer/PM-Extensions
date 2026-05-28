from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwDate:

    @grepr_dataclass()
    class now(ThirdBlock):
        OPCODE: ClassVar = "&jwDate::now"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class epoch(ThirdBlock):
        OPCODE: ClassVar = "&jwDate::unix epoch"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE: ClassVar = "&jwDate::parse (INPUT)"
        INPUT_SPECS: ClassVar = (("INPUT", "input", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        input: INPUT_COMPATIBLE_T
