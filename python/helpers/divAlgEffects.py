from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class divAlgEffects:

    @staticmethod
    def eff_perform_ret(eff: INPUT_COMPATIBLE_T, data: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerformRet}}",
            inputs={
                "EFF": InputValue.try_as_input(eff, p.SRBlockAndTextInputValue),
                "DATA": InputValue.try_as_input(data, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def eff_handle(
        substack: INPUT_COMPATIBLE_T, substack2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::handle in {SUBSTACK} effects {SUBSTACK2}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
                "SUBSTACK2": InputValue.try_as_input(substack2, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def eff_handler_case(
        eff: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::effect (EFF) with {:DATA:} {SUBSTACK}",
            inputs={
                "EFF": InputValue.try_as_input(eff, p.SRBlockAndTextInputValue),
                "DATA": InputValue.try_as_input(
                    InputValue(divAlgEffects.eff_data()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def eff_recurse_handler(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::recursively handle {SUBSTACK}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def eff_resume_ret(data: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeRet}}",
            inputs={"DATA": InputValue.try_as_input(data, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def eff_resume_tail(data: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeTail}}",
            inputs={"DATA": InputValue.try_as_input(data, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def eff_data() -> p.SRBlock:
        return p.SRBlock(opcode="&divAlgEffects::data", inputs={}, dropdowns={})

    @staticmethod
    def eff_continuation() -> p.SRBlock:
        return p.SRBlock(opcode="&divAlgEffects::continuation", inputs={}, dropdowns={})

    @staticmethod
    def eff_cont_has_resumed(cont: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::has (CONT) resumed?",
            inputs={"CONT": InputValue.try_as_input(cont, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def eff_resume(data: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResume}}",
            inputs={"DATA": InputValue.try_as_input(data, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def eff_perform(eff: INPUT_COMPATIBLE_T, data: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerform}}",
            inputs={
                "EFF": InputValue.try_as_input(eff, p.SRBlockAndTextInputValue),
                "DATA": InputValue.try_as_input(data, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )
