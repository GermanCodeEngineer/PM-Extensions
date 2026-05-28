from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class divAlgEffects:

    @grepr_dataclass()
    class eff_perform_ret(ThirdBlock):
        OPCODE: ClassVar = (
            "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerformRet}}"
        )
        INPUT_SPECS: ClassVar = (
            ("EFF", "eff", p.SRBlockAndTextInputValue, None),
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_handle(ThirdBlock):
        OPCODE: ClassVar = "&divAlgEffects::handle in {SUBSTACK} effects {SUBSTACK2}"
        INPUT_SPECS: ClassVar = (
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_handler_case(ThirdBlock):
        OPCODE: ClassVar = "&divAlgEffects::effect (EFF) with {:DATA:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("EFF", "eff", p.SRBlockAndTextInputValue, None),
            (
                "DATA",
                "data",
                p.SREmbeddedBlockInputValue,
                lambda: divAlgEffects.eff_data(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        eff: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_recurse_handler(ThirdBlock):
        OPCODE: ClassVar = "&divAlgEffects::recursively handle {SUBSTACK}"
        INPUT_SPECS: ClassVar = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_resume_ret(ThirdBlock):
        OPCODE: ClassVar = (
            "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeRet}}"
        )
        INPUT_SPECS: ClassVar = (("DATA", "data", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_resume_tail(ThirdBlock):
        OPCODE: ClassVar = (
            "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeTail}}"
        )
        INPUT_SPECS: ClassVar = (("DATA", "data", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_data(ThirdBlock):
        OPCODE: ClassVar = "&divAlgEffects::data"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class eff_continuation(ThirdBlock):
        OPCODE: ClassVar = "&divAlgEffects::continuation"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class eff_cont_has_resumed(ThirdBlock):
        OPCODE: ClassVar = "&divAlgEffects::has (CONT) resumed?"
        INPUT_SPECS: ClassVar = (("CONT", "cont", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        cont: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_perform(ThirdBlock):
        OPCODE: ClassVar = (
            "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerform}}"
        )
        INPUT_SPECS: ClassVar = (
            ("EFF", "eff", p.SRBlockAndTextInputValue, None),
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_resume(ThirdBlock):
        OPCODE: ClassVar = (
            "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResume}}"
        )
        INPUT_SPECS: ClassVar = (("DATA", "data", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        data: INPUT_COMPATIBLE_T
