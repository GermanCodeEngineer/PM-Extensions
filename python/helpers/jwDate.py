from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwDate:

    @grepr_dataclass()
    class now(ThirdBlock):
        OPCODE = "&jwDate::now"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class epoch(ThirdBlock):
        OPCODE = "&jwDate::unix epoch"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class parse(ThirdBlock):
        OPCODE = "&jwDate::parse (INPUT)"
        INPUT_SPECS = (("INPUT", "input", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        input: INPUT_COMPATIBLE_T
