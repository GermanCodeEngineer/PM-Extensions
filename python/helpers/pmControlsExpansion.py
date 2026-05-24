from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmControlsExpansion:

    @grepr_dataclass()
    class as_new_broadcast(ThirdBlock):
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class restart_from_the_top(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::restart from the top",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class as_new_broadcast_args(ThirdBlock):
        data: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class as_new_broadcast_arg_block(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmControlsExpansion::thread data", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class if_else_if(ThirdBlock):
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class if_else_if_else(ThirdBlock):
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T
        substack3: INPUT_COMPATIBLE_T

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
