from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class pmMotionExpansion:

    @grepr_dataclass()
    class rotation_style(ThirdBlock):
        OPCODE = "&pmMotionExpansion::rotation style"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class fence(ThirdBlock):
        OPCODE = "&pmMotionExpansion::manually fence"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class steptowards(ThirdBlock):
        OPCODE = "&pmMotionExpansion::move (STEPS) steps towards x: (X) y: (Y)"
        steps: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class tweentowards(ThirdBlock):
        OPCODE = "&pmMotionExpansion::move [PERCENT]% of the way to x: (X) y: (Y)"
        percent: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PERCENT", "percent", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PERCENT", "percent", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class touchingxy(ThirdBlock):
        OPCODE = "&pmMotionExpansion::touching x: (X) y: [Y]?"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class touchingrect(ThirdBlock):
        OPCODE = "&pmMotionExpansion::touching rectangle x1: (X1) y1: (Y1) x2: (X2) y2: [Y2]?"
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X1", "x1", p.SRBlockAndTextInputValue, None),
                    ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                    ("X2", "x2", p.SRBlockAndTextInputValue, None),
                    ("Y2", "y2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X1", "x1", p.SRBlockAndTextInputValue, None),
                    ("Y1", "y1", p.SRBlockAndTextInputValue, None),
                    ("X2", "x2", p.SRBlockAndTextInputValue, None),
                    ("Y2", "y2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_home(ThirdBlock):
        OPCODE = "&pmMotionExpansion::set my home"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class goto_home(ThirdBlock):
        OPCODE = "&pmMotionExpansion::go to home"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
