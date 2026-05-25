from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class divAlgEffects:

    @grepr_dataclass()
    class eff_perform_ret(ThirdBlock):
        OPCODE = "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerformRet}}"
        INPUT_SPECS = (
            ("EFF", "eff", p.SRBlockAndTextInputValue, None),
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_handle(ThirdBlock):
        OPCODE = "&divAlgEffects::handle in {SUBSTACK} effects {SUBSTACK2}"
        INPUT_SPECS = (
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
            ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_handler_case(ThirdBlock):
        OPCODE = "&divAlgEffects::effect (EFF) with {:DATA:} {SUBSTACK}"
        INPUT_SPECS = (
            ("EFF", "eff", p.SRBlockAndTextInputValue, None),
            (
                "DATA",
                "data",
                p.SREmbeddedBlockInputValue,
                lambda: divAlgEffects.eff_data(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        eff: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_recurse_handler(ThirdBlock):
        OPCODE = "&divAlgEffects::recursively handle {SUBSTACK}"
        INPUT_SPECS = (("SUBSTACK", "substack", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = ()
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_resume_ret(ThirdBlock):
        OPCODE = "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeRet}}"
        INPUT_SPECS = (("DATA", "data", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_resume_tail(ThirdBlock):
        OPCODE = "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeTail}}"
        INPUT_SPECS = (("DATA", "data", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_data(ThirdBlock):
        OPCODE = "&divAlgEffects::data"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class eff_continuation(ThirdBlock):
        OPCODE = "&divAlgEffects::continuation"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class eff_cont_has_resumed(ThirdBlock):
        OPCODE = "&divAlgEffects::has (CONT) resumed?"
        INPUT_SPECS = (("CONT", "cont", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        cont: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_perform(ThirdBlock):
        OPCODE = (
            "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerform}}"
        )
        INPUT_SPECS = (
            ("EFF", "eff", p.SRBlockAndTextInputValue, None),
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class eff_resume(ThirdBlock):
        OPCODE = "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResume}}"
        INPUT_SPECS = (("DATA", "data", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        data: INPUT_COMPATIBLE_T
