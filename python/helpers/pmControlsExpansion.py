from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmControlsExpansion:

    class as_new_broadcast(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::new thread {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    class restart_from_the_top(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::restart from the top",
                inputs={},
                dropdowns={},
            )

    class as_new_broadcast_args(ThirdBlock):

        def __init__(self, data: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.data = data
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::new thread with data (DATA) {SUBSTACK}",
                inputs={
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class as_new_broadcast_arg_block(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::thread data", inputs={}, dropdowns={}
            )

    class if_else_if(ThirdBlock):

        def __init__(
            self,
            condition1: INPUT_COMPATIBLE_T,
            condition2: INPUT_COMPATIBLE_T,
            substack: INPUT_COMPATIBLE_T,
            substack2: INPUT_COMPATIBLE_T,
        ):
            self.condition1 = condition1
            self.condition2 = condition2
            self.substack = substack
            self.substack2 = substack2

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2}",
                inputs={
                    "CONDITION1": ThirdInputValue.as_input(
                        self.condition1, p.SRBlockAndBoolInputValue
                    ),
                    "CONDITION2": ThirdInputValue.as_input(
                        self.condition2, p.SRBlockAndBoolInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                    "SUBSTACK2": ThirdInputValue.as_input(
                        self.substack2, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class if_else_if_else(ThirdBlock):

        def __init__(
            self,
            condition1: INPUT_COMPATIBLE_T,
            condition2: INPUT_COMPATIBLE_T,
            substack: INPUT_COMPATIBLE_T,
            substack2: INPUT_COMPATIBLE_T,
            substack3: INPUT_COMPATIBLE_T,
        ):
            self.condition1 = condition1
            self.condition2 = condition2
            self.substack = substack
            self.substack2 = substack2
            self.substack3 = substack3

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2} else {SUBSTACK3}",
                inputs={
                    "CONDITION1": ThirdInputValue.as_input(
                        self.condition1, p.SRBlockAndBoolInputValue
                    ),
                    "CONDITION2": ThirdInputValue.as_input(
                        self.condition2, p.SRBlockAndBoolInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                    "SUBSTACK2": ThirdInputValue.as_input(
                        self.substack2, p.SRScriptInputValue
                    ),
                    "SUBSTACK3": ThirdInputValue.as_input(
                        self.substack3, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )
