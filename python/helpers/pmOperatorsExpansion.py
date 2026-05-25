from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class pmOperatorsExpansion:

    @grepr_dataclass()
    class shift_left(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::(num1) << (num2)"
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class shift_right(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::(num1) >> (num2)"
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class binnary_and(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::(num1) & (num2)"
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class binnary_or(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::(num1) | (num2)"
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class binnary_xor(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::(num1) ^ (num2)"
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("num1", "num1", p.SRBlockAndTextInputValue, None),
                    ("num2", "num2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class binnary_not(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::~ (num1)"
        num1: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("num1", "num1", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("num1", "num1", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class or_if_falsey(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::(ONE) or else (TWO)"
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ONE", "one", p.SRBlockAndTextInputValue, None),
                    ("TWO", "two", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ONE", "one", p.SRBlockAndTextInputValue, None),
                    ("TWO", "two", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class if_is_truthy(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::if <ONE> is true then (TWO)"
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ONE", "one", p.SRBlockAndBoolInputValue, None),
                    ("TWO", "two", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ONE", "one", p.SRBlockAndBoolInputValue, None),
                    ("TWO", "two", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_number_multiple_of(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::is (NUM) multiple of [MULTIPLE]?"
        num: INPUT_COMPATIBLE_T
        multiple: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NUM", "num", p.SRBlockAndTextInputValue, None),
                    ("MULTIPLE", "multiple", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NUM", "num", p.SRBlockAndTextInputValue, None),
                    ("MULTIPLE", "multiple", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_integer(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::is (NUM) an integer?"
        num: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NUM", "num", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NUM", "num", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class is_prime(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::is (NUM) a prime number?"
        num: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NUM", "num", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NUM", "num", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class is_even(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::is (NUM) even?"
        num: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NUM", "num", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NUM", "num", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class between_numbers(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::is (NUM) between (MIN) and [MAX]?"
        num: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NUM", "num", p.SRBlockAndTextInputValue, None),
                    ("MIN", "min", p.SRBlockAndTextInputValue, None),
                    ("MAX", "max", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NUM", "num", p.SRBlockAndTextInputValue, None),
                    ("MIN", "min", p.SRBlockAndTextInputValue, None),
                    ("MAX", "max", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class evaluate_math(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::answer to (EQUATION)"
        equation: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("EQUATION", "equation", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("EQUATION", "equation", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class part_of_ratio(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::([PART]) part of ratio (RATIO)"
        part: INPUT_COMPATIBLE_T
        ratio: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PART", "part", p.SRBlockAndDropdownInputValue, None),
                    ("RATIO", "ratio", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PART", "part", p.SRBlockAndDropdownInputValue, None),
                    ("RATIO", "ratio", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class simplify_ratio(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::simplify ratio (RATIO)"
        ratio: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("RATIO", "ratio", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("RATIO", "ratio", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class pi(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::π"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class euler(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::e"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class infinity(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::∞"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class truncate_number(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::truncate number (NUM)"
        num: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("NUM", "num", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("NUM", "num", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class atan2(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::atan2 of x (X) y (Y)"
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
    class reverse_chars(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::reverse (TEXT)"
        text: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TEXT", "text", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TEXT", "text", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class shuffle_chars(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::shuffle (TEXT)"
        text: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TEXT", "text", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TEXT", "text", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class text_after(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::text after (TEXT) in (BASE)"
        text: INPUT_COMPATIBLE_T
        base: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("BASE", "base", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("BASE", "base", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class text_before(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::text before (TEXT) in (BASE)"
        text: INPUT_COMPATIBLE_T
        base: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("BASE", "base", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                    ("BASE", "base", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class exactly_equal(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::(ONE) exactly equals [TWO]?"
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ONE", "one", p.SRBlockAndTextInputValue, None),
                    ("TWO", "two", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ONE", "one", p.SRBlockAndTextInputValue, None),
                    ("TWO", "two", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_replacer(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::set replacer (REPLACER) to (TEXT)"
        replacer: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("REPLACER", "replacer", p.SRBlockAndTextInputValue, None),
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("REPLACER", "replacer", p.SRBlockAndTextInputValue, None),
                    ("TEXT", "text", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class reset_replacers(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::reset replacers"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class apply_replacers(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::apply replacers to (TEXT)"
        text: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TEXT", "text", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("TEXT", "text", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class speed_to_pitch(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::speed (SPEED) to pitch"
        speed: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SPEED", "speed", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SPEED", "speed", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class pitch_to_speed(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::pitch (PITCH) to speed"
        pitch: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("PITCH", "pitch", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("PITCH", "pitch", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class join4(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4)"
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class join5(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5)"
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class join6(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6)"
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class join7(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7)"
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                    ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                    ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class join8(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8)"
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T
        string8: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                    ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                    ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                    ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                    ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class join9(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8) (STRING9)"
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T
        string8: INPUT_COMPATIBLE_T
        string9: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                    ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                    ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
                    ("STRING9", "string9", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
                    ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
                    ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
                    ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
                    ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
                    ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
                    ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
                    ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
                    ("STRING9", "string9", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_part(ThirdBlock):
        OPCODE = "&pmOperatorsExpansion::#menu:part"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
