from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class pmControlsExpansion:

    @grepr_dataclass()
    class as_new_broadcast(ThirdBlock):
        OPCODE: ClassVar = "&pmControlsExpansion::new thread {SUBSTACK}"
        INPUT_SPECS: ClassVar = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class restart_from_the_top(ThirdBlock):
        OPCODE: ClassVar = "&pmControlsExpansion::restart from the top"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class as_new_broadcast_args(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmControlsExpansion::new thread with data (DATA) {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        data: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class as_new_broadcast_arg_block(ThirdBlock):
        OPCODE: ClassVar = "&pmControlsExpansion::thread data"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class if_else_if(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2}"
        )
        INPUT_SPECS: ClassVar = (
            ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
            ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_else_if_else(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2} else {SUBSTACK3}"
        )
        INPUT_SPECS: ClassVar = (
            ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
            ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
            ("SUBSTACK3", "substack3", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T
        substack3: INPUT_COMPATIBLE_T
