from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class pmControlsExpansion:

    @staticmethod
    def as_new_broadcast(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmControlsExpansion::new thread {SUBSTACK}",
            inputs={
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def restart_from_the_top() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmControlsExpansion::restart from the top", inputs={}, dropdowns={}
        )

    @staticmethod
    def as_new_broadcast_args(
        data: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmControlsExpansion::new thread with data (DATA) {SUBSTACK}",
            inputs={
                "DATA": ThirdInputValue.as_input(data, p.SRBlockAndTextInputValue),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def as_new_broadcast_arg_block() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmControlsExpansion::thread data", inputs={}, dropdowns={}
        )

    @staticmethod
    def if_else_if(
        condition1: INPUT_COMPATIBLE_T,
        condition2: INPUT_COMPATIBLE_T,
        substack: INPUT_COMPATIBLE_T,
        substack2: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2}",
            inputs={
                "CONDITION1": ThirdInputValue.as_input(
                    condition1, p.SRBlockAndBoolInputValue
                ),
                "CONDITION2": ThirdInputValue.as_input(
                    condition2, p.SRBlockAndBoolInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
                "SUBSTACK2": ThirdInputValue.as_input(substack2, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def if_else_if_else(
        condition1: INPUT_COMPATIBLE_T,
        condition2: INPUT_COMPATIBLE_T,
        substack: INPUT_COMPATIBLE_T,
        substack2: INPUT_COMPATIBLE_T,
        substack3: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2} else {SUBSTACK3}",
            inputs={
                "CONDITION1": ThirdInputValue.as_input(
                    condition1, p.SRBlockAndBoolInputValue
                ),
                "CONDITION2": ThirdInputValue.as_input(
                    condition2, p.SRBlockAndBoolInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
                "SUBSTACK2": ThirdInputValue.as_input(substack2, p.SRScriptInputValue),
                "SUBSTACK3": ThirdInputValue.as_input(substack3, p.SRScriptInputValue),
            },
            dropdowns={},
        )
