from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class divAlgEffects:

    class eff_perform_ret(ThirdBlock):

        def __init__(self, eff: INPUT_COMPATIBLE_T, data: INPUT_COMPATIBLE_T):
            self.eff = eff
            self.data = data

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

    class eff_handle(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T, substack2: INPUT_COMPATIBLE_T):
            self.substack = substack
            self.substack2 = substack2

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

    class eff_handler_case(ThirdBlock):

        def __init__(self, eff: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.eff = eff
            self.substack = substack

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

    class eff_recurse_handler(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

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

    class eff_resume_ret(ThirdBlock):

        def __init__(self, data: INPUT_COMPATIBLE_T):
            self.data = data

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

    class eff_resume_tail(ThirdBlock):

        def __init__(self, data: INPUT_COMPATIBLE_T):
            self.data = data

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

    class eff_data(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divAlgEffects::data", inputs={}, dropdowns={})

    class eff_continuation(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divAlgEffects::continuation", inputs={}, dropdowns={}
            )

    class eff_cont_has_resumed(ThirdBlock):

        def __init__(self, cont: INPUT_COMPATIBLE_T):
            self.cont = cont

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

    class eff_perform(ThirdBlock):

        def __init__(self, eff: INPUT_COMPATIBLE_T, data: INPUT_COMPATIBLE_T):
            self.eff = eff
            self.data = data

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

    class eff_resume(ThirdBlock):

        def __init__(self, data: INPUT_COMPATIBLE_T):
            self.data = data

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
