from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class divAlgEffects:

    @grepr_dataclass()
    class eff_perform_ret(ThirdBlock):
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerformRet}}",
                inputs={
                    "EFF": ThirdInputValue.as_input(
                        self.eff, p.SRBlockAndTextInputValue
                    ),
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_handle(ThirdBlock):
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::handle in {SUBSTACK} effects {SUBSTACK2}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                    "SUBSTACK2": ThirdInputValue.as_input(
                        self.substack2, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_handler_case(ThirdBlock):
        eff: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::effect (EFF) with {:DATA:} {SUBSTACK}",
                inputs={
                    "EFF": ThirdInputValue.as_input(
                        self.eff, p.SRBlockAndTextInputValue
                    ),
                    "DATA": ThirdInputValue.as_input(
                        ThirdInputValue(divAlgEffects.eff_data()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_recurse_handler(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::recursively handle {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_resume_ret(ThirdBlock):
        data: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeRet}}",
                inputs={
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_resume_tail(ThirdBlock):
        data: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeTail}}",
                inputs={
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_data(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divAlgEffects::data", inputs={}, dropdowns={})

    @grepr_dataclass()
    class eff_continuation(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::continuation", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class eff_cont_has_resumed(ThirdBlock):
        cont: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::has (CONT) resumed?",
                inputs={
                    "CONT": ThirdInputValue.as_input(
                        self.cont, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_perform(ThirdBlock):
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerform}}",
                inputs={
                    "EFF": ThirdInputValue.as_input(
                        self.eff, p.SRBlockAndTextInputValue
                    ),
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class eff_resume(ThirdBlock):
        data: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResume}}",
                inputs={
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )
