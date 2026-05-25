from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmControlsExpansion:

    @grepr_dataclass()
    class as_new_broadcast(ThirdBlock):
        OPCODE = "&pmControlsExpansion::new thread {SUBSTACK}"
        INPUT_SPECS = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class restart_from_the_top(ThirdBlock):
        OPCODE = "&pmControlsExpansion::restart from the top"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class as_new_broadcast_args(ThirdBlock):
        OPCODE = "&pmControlsExpansion::new thread with data (DATA) {SUBSTACK}"
        INPUT_SPECS = (
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        data: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class as_new_broadcast_arg_block(ThirdBlock):
        OPCODE = "&pmControlsExpansion::thread data"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class if_else_if(ThirdBlock):
        OPCODE = "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2}"
        INPUT_SPECS = (
            ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
            ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_else_if_else(ThirdBlock):
        OPCODE = "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2} else {SUBSTACK3}"
        INPUT_SPECS = (
            ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
            ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
            ("SUBSTACK3", "substack3", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T
        substack3: INPUT_COMPATIBLE_T
