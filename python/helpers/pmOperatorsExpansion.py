from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmOperatorsExpansion:

    @grepr_dataclass()
    class shift_left(ThirdBlock):
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::(num1) << (num2)",
                inputs={
                    "num1": ThirdInputValue.as_input(
                        self.num1, p.SRBlockAndTextInputValue
                    ),
                    "num2": ThirdInputValue.as_input(
                        self.num2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class shift_right(ThirdBlock):
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::(num1) >> (num2)",
                inputs={
                    "num1": ThirdInputValue.as_input(
                        self.num1, p.SRBlockAndTextInputValue
                    ),
                    "num2": ThirdInputValue.as_input(
                        self.num2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class binnary_and(ThirdBlock):
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::(num1) & (num2)",
                inputs={
                    "num1": ThirdInputValue.as_input(
                        self.num1, p.SRBlockAndTextInputValue
                    ),
                    "num2": ThirdInputValue.as_input(
                        self.num2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class binnary_or(ThirdBlock):
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::(num1) | (num2)",
                inputs={
                    "num1": ThirdInputValue.as_input(
                        self.num1, p.SRBlockAndTextInputValue
                    ),
                    "num2": ThirdInputValue.as_input(
                        self.num2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class binnary_xor(ThirdBlock):
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::(num1) ^ (num2)",
                inputs={
                    "num1": ThirdInputValue.as_input(
                        self.num1, p.SRBlockAndTextInputValue
                    ),
                    "num2": ThirdInputValue.as_input(
                        self.num2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class binnary_not(ThirdBlock):
        num1: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::~ (num1)",
                inputs={
                    "num1": ThirdInputValue.as_input(
                        self.num1, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class or_if_falsey(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::(ONE) or else (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(
                        self.one, p.SRBlockAndTextInputValue
                    ),
                    "TWO": ThirdInputValue.as_input(
                        self.two, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class if_is_truthy(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::if <ONE> is true then (TWO)",
                inputs={
                    "ONE": ThirdInputValue.as_input(
                        self.one, p.SRBlockAndBoolInputValue
                    ),
                    "TWO": ThirdInputValue.as_input(
                        self.two, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_number_multiple_of(ThirdBlock):
        num: INPUT_COMPATIBLE_T
        multiple: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::is (NUM) multiple of [MULTIPLE]?",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    ),
                    "MULTIPLE": ThirdInputValue.as_input(
                        self.multiple, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_integer(ThirdBlock):
        num: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::is (NUM) an integer?",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_prime(ThirdBlock):
        num: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::is (NUM) a prime number?",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_even(ThirdBlock):
        num: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::is (NUM) even?",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class between_numbers(ThirdBlock):
        num: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::is (NUM) between (MIN) and [MAX]?",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    ),
                    "MIN": ThirdInputValue.as_input(
                        self.min, p.SRBlockAndTextInputValue
                    ),
                    "MAX": ThirdInputValue.as_input(
                        self.max, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class evaluate_math(ThirdBlock):
        equation: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::answer to (EQUATION)",
                inputs={
                    "EQUATION": ThirdInputValue.as_input(
                        self.equation, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class part_of_ratio(ThirdBlock):
        part: INPUT_COMPATIBLE_T
        ratio: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::([PART]) part of ratio (RATIO)",
                inputs={
                    "PART": ThirdInputValue.as_input(
                        self.part, p.SRBlockAndDropdownInputValue
                    ),
                    "RATIO": ThirdInputValue.as_input(
                        self.ratio, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class simplify_ratio(ThirdBlock):
        ratio: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::simplify ratio (RATIO)",
                inputs={
                    "RATIO": ThirdInputValue.as_input(
                        self.ratio, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class pi(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&pmOperatorsExpansion::π", inputs={}, dropdowns={})

    @grepr_dataclass()
    class euler(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&pmOperatorsExpansion::e", inputs={}, dropdowns={})

    @grepr_dataclass()
    class infinity(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&pmOperatorsExpansion::∞", inputs={}, dropdowns={})

    @grepr_dataclass()
    class truncate_number(ThirdBlock):
        num: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::truncate number (NUM)",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class atan2(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::atan2 of x (X) y (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class reverse_chars(ThirdBlock):
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::reverse (TEXT)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class shuffle_chars(ThirdBlock):
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::shuffle (TEXT)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class text_after(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        base: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::text after (TEXT) in (BASE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "BASE": ThirdInputValue.as_input(
                        self.base, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class text_before(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        base: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::text before (TEXT) in (BASE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "BASE": ThirdInputValue.as_input(
                        self.base, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class exactly_equal(ThirdBlock):
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::(ONE) exactly equals [TWO]?",
                inputs={
                    "ONE": ThirdInputValue.as_input(
                        self.one, p.SRBlockAndTextInputValue
                    ),
                    "TWO": ThirdInputValue.as_input(
                        self.two, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_replacer(ThirdBlock):
        replacer: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::set replacer (REPLACER) to (TEXT)",
                inputs={
                    "REPLACER": ThirdInputValue.as_input(
                        self.replacer, p.SRBlockAndTextInputValue
                    ),
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class reset_replacers(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::reset replacers", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class apply_replacers(ThirdBlock):
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::apply replacers to (TEXT)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class speed_to_pitch(ThirdBlock):
        speed: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::speed (SPEED) to pitch",
                inputs={
                    "SPEED": ThirdInputValue.as_input(
                        self.speed, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class pitch_to_speed(ThirdBlock):
        pitch: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::pitch (PITCH) to speed",
                inputs={
                    "PITCH": ThirdInputValue.as_input(
                        self.pitch, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class join4(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4)",
                inputs={
                    "STRING1": ThirdInputValue.as_input(
                        self.string1, p.SRBlockAndTextInputValue
                    ),
                    "STRING2": ThirdInputValue.as_input(
                        self.string2, p.SRBlockAndTextInputValue
                    ),
                    "STRING3": ThirdInputValue.as_input(
                        self.string3, p.SRBlockAndTextInputValue
                    ),
                    "STRING4": ThirdInputValue.as_input(
                        self.string4, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class join5(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5)",
                inputs={
                    "STRING1": ThirdInputValue.as_input(
                        self.string1, p.SRBlockAndTextInputValue
                    ),
                    "STRING2": ThirdInputValue.as_input(
                        self.string2, p.SRBlockAndTextInputValue
                    ),
                    "STRING3": ThirdInputValue.as_input(
                        self.string3, p.SRBlockAndTextInputValue
                    ),
                    "STRING4": ThirdInputValue.as_input(
                        self.string4, p.SRBlockAndTextInputValue
                    ),
                    "STRING5": ThirdInputValue.as_input(
                        self.string5, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class join6(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6)",
                inputs={
                    "STRING1": ThirdInputValue.as_input(
                        self.string1, p.SRBlockAndTextInputValue
                    ),
                    "STRING2": ThirdInputValue.as_input(
                        self.string2, p.SRBlockAndTextInputValue
                    ),
                    "STRING3": ThirdInputValue.as_input(
                        self.string3, p.SRBlockAndTextInputValue
                    ),
                    "STRING4": ThirdInputValue.as_input(
                        self.string4, p.SRBlockAndTextInputValue
                    ),
                    "STRING5": ThirdInputValue.as_input(
                        self.string5, p.SRBlockAndTextInputValue
                    ),
                    "STRING6": ThirdInputValue.as_input(
                        self.string6, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class join7(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7)",
                inputs={
                    "STRING1": ThirdInputValue.as_input(
                        self.string1, p.SRBlockAndTextInputValue
                    ),
                    "STRING2": ThirdInputValue.as_input(
                        self.string2, p.SRBlockAndTextInputValue
                    ),
                    "STRING3": ThirdInputValue.as_input(
                        self.string3, p.SRBlockAndTextInputValue
                    ),
                    "STRING4": ThirdInputValue.as_input(
                        self.string4, p.SRBlockAndTextInputValue
                    ),
                    "STRING5": ThirdInputValue.as_input(
                        self.string5, p.SRBlockAndTextInputValue
                    ),
                    "STRING6": ThirdInputValue.as_input(
                        self.string6, p.SRBlockAndTextInputValue
                    ),
                    "STRING7": ThirdInputValue.as_input(
                        self.string7, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class join8(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T
        string8: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8)",
                inputs={
                    "STRING1": ThirdInputValue.as_input(
                        self.string1, p.SRBlockAndTextInputValue
                    ),
                    "STRING2": ThirdInputValue.as_input(
                        self.string2, p.SRBlockAndTextInputValue
                    ),
                    "STRING3": ThirdInputValue.as_input(
                        self.string3, p.SRBlockAndTextInputValue
                    ),
                    "STRING4": ThirdInputValue.as_input(
                        self.string4, p.SRBlockAndTextInputValue
                    ),
                    "STRING5": ThirdInputValue.as_input(
                        self.string5, p.SRBlockAndTextInputValue
                    ),
                    "STRING6": ThirdInputValue.as_input(
                        self.string6, p.SRBlockAndTextInputValue
                    ),
                    "STRING7": ThirdInputValue.as_input(
                        self.string7, p.SRBlockAndTextInputValue
                    ),
                    "STRING8": ThirdInputValue.as_input(
                        self.string8, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class join9(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T
        string8: INPUT_COMPATIBLE_T
        string9: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8) (STRING9)",
                inputs={
                    "STRING1": ThirdInputValue.as_input(
                        self.string1, p.SRBlockAndTextInputValue
                    ),
                    "STRING2": ThirdInputValue.as_input(
                        self.string2, p.SRBlockAndTextInputValue
                    ),
                    "STRING3": ThirdInputValue.as_input(
                        self.string3, p.SRBlockAndTextInputValue
                    ),
                    "STRING4": ThirdInputValue.as_input(
                        self.string4, p.SRBlockAndTextInputValue
                    ),
                    "STRING5": ThirdInputValue.as_input(
                        self.string5, p.SRBlockAndTextInputValue
                    ),
                    "STRING6": ThirdInputValue.as_input(
                        self.string6, p.SRBlockAndTextInputValue
                    ),
                    "STRING7": ThirdInputValue.as_input(
                        self.string7, p.SRBlockAndTextInputValue
                    ),
                    "STRING8": ThirdInputValue.as_input(
                        self.string8, p.SRBlockAndTextInputValue
                    ),
                    "STRING9": ThirdInputValue.as_input(
                        self.string9, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_part(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::#menu:part", inputs={}, dropdowns={}
            )
