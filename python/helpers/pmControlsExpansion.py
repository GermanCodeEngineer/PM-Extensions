from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class pmControlsExpansion:

    @grepr_dataclass()
    class as_new_broadcast(ThirdBlock):
        OPCODE = "&pmControlsExpansion::new thread {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SUBSTACK", "substack", p.SRScriptInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SUBSTACK", "substack", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class restart_from_the_top(ThirdBlock):
        OPCODE = "&pmControlsExpansion::restart from the top"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class as_new_broadcast_args(ThirdBlock):
        OPCODE = "&pmControlsExpansion::new thread with data (DATA) {SUBSTACK}"
        data: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class as_new_broadcast_arg_block(ThirdBlock):
        OPCODE = "&pmControlsExpansion::thread data"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class if_else_if(ThirdBlock):
        OPCODE = "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2}"
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
                    ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                    ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
                    ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                    ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class if_else_if_else(ThirdBlock):
        OPCODE = "&pmControlsExpansion::if <CONDITION1> then {SUBSTACK} else if <CONDITION2> then {SUBSTACK2} else {SUBSTACK3}"
        condition1: INPUT_COMPATIBLE_T
        condition2: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T
        substack3: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
                    ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                    ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
                    ("SUBSTACK3", "substack3", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CONDITION1", "condition1", p.SRBlockAndBoolInputValue, None),
                    ("CONDITION2", "condition2", p.SRBlockAndBoolInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                    ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
                    ("SUBSTACK3", "substack3", p.SRScriptInputValue, None),
                ),
                (),
            )
