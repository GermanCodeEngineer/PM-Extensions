from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmOperatorsExpansion:

    class shift_left(ThirdBlock):

        def __init__(self, num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T):
            self.num1 = num1
            self.num2 = num2

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

    class shift_right(ThirdBlock):

        def __init__(self, num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T):
            self.num1 = num1
            self.num2 = num2

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

    class binnary_and(ThirdBlock):

        def __init__(self, num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T):
            self.num1 = num1
            self.num2 = num2

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

    class binnary_or(ThirdBlock):

        def __init__(self, num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T):
            self.num1 = num1
            self.num2 = num2

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

    class binnary_xor(ThirdBlock):

        def __init__(self, num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T):
            self.num1 = num1
            self.num2 = num2

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

    class binnary_not(ThirdBlock):

        def __init__(self, num1: INPUT_COMPATIBLE_T):
            self.num1 = num1

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

    class or_if_falsey(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

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

    class if_is_truthy(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

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

    class is_number_multiple_of(ThirdBlock):

        def __init__(self, num: INPUT_COMPATIBLE_T, multiple: INPUT_COMPATIBLE_T):
            self.num = num
            self.multiple = multiple

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

    class is_integer(ThirdBlock):

        def __init__(self, num: INPUT_COMPATIBLE_T):
            self.num = num

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

    class is_prime(ThirdBlock):

        def __init__(self, num: INPUT_COMPATIBLE_T):
            self.num = num

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

    class is_even(ThirdBlock):

        def __init__(self, num: INPUT_COMPATIBLE_T):
            self.num = num

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

    class between_numbers(ThirdBlock):

        def __init__(
            self,
            num: INPUT_COMPATIBLE_T,
            min: INPUT_COMPATIBLE_T,
            max: INPUT_COMPATIBLE_T,
        ):
            self.num = num
            self.min = min
            self.max = max

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

    class evaluate_math(ThirdBlock):

        def __init__(self, equation: INPUT_COMPATIBLE_T):
            self.equation = equation

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

    class part_of_ratio(ThirdBlock):

        def __init__(self, part: INPUT_COMPATIBLE_T, ratio: INPUT_COMPATIBLE_T):
            self.part = part
            self.ratio = ratio

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

    class simplify_ratio(ThirdBlock):

        def __init__(self, ratio: INPUT_COMPATIBLE_T):
            self.ratio = ratio

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

    class pi(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&pmOperatorsExpansion::π", inputs={}, dropdowns={})

    class euler(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&pmOperatorsExpansion::e", inputs={}, dropdowns={})

    class infinity(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&pmOperatorsExpansion::∞", inputs={}, dropdowns={})

    class truncate_number(ThirdBlock):

        def __init__(self, num: INPUT_COMPATIBLE_T):
            self.num = num

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

    class atan2(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::atan2 of x (X) y (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class reverse_chars(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T):
            self.text = text

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

    class shuffle_chars(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T):
            self.text = text

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

    class text_after(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T, base: INPUT_COMPATIBLE_T):
            self.text = text
            self.base = base

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

    class text_before(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T, base: INPUT_COMPATIBLE_T):
            self.text = text
            self.base = base

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

    class exactly_equal(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T):
            self.one = one
            self.two = two

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

    class set_replacer(ThirdBlock):

        def __init__(self, replacer: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T):
            self.replacer = replacer
            self.text = text

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

    class reset_replacers(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::reset replacers", inputs={}, dropdowns={}
            )

    class apply_replacers(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T):
            self.text = text

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

    class speed_to_pitch(ThirdBlock):

        def __init__(self, speed: INPUT_COMPATIBLE_T):
            self.speed = speed

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

    class pitch_to_speed(ThirdBlock):

        def __init__(self, pitch: INPUT_COMPATIBLE_T):
            self.pitch = pitch

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

    class join4(ThirdBlock):

        def __init__(
            self,
            string1: INPUT_COMPATIBLE_T,
            string2: INPUT_COMPATIBLE_T,
            string3: INPUT_COMPATIBLE_T,
            string4: INPUT_COMPATIBLE_T,
        ):
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3
            self.string4 = string4

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

    class join5(ThirdBlock):

        def __init__(
            self,
            string1: INPUT_COMPATIBLE_T,
            string2: INPUT_COMPATIBLE_T,
            string3: INPUT_COMPATIBLE_T,
            string4: INPUT_COMPATIBLE_T,
            string5: INPUT_COMPATIBLE_T,
        ):
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3
            self.string4 = string4
            self.string5 = string5

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

    class join6(ThirdBlock):

        def __init__(
            self,
            string1: INPUT_COMPATIBLE_T,
            string2: INPUT_COMPATIBLE_T,
            string3: INPUT_COMPATIBLE_T,
            string4: INPUT_COMPATIBLE_T,
            string5: INPUT_COMPATIBLE_T,
            string6: INPUT_COMPATIBLE_T,
        ):
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3
            self.string4 = string4
            self.string5 = string5
            self.string6 = string6

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

    class join7(ThirdBlock):

        def __init__(
            self,
            string1: INPUT_COMPATIBLE_T,
            string2: INPUT_COMPATIBLE_T,
            string3: INPUT_COMPATIBLE_T,
            string4: INPUT_COMPATIBLE_T,
            string5: INPUT_COMPATIBLE_T,
            string6: INPUT_COMPATIBLE_T,
            string7: INPUT_COMPATIBLE_T,
        ):
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3
            self.string4 = string4
            self.string5 = string5
            self.string6 = string6
            self.string7 = string7

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

    class join8(ThirdBlock):

        def __init__(
            self,
            string1: INPUT_COMPATIBLE_T,
            string2: INPUT_COMPATIBLE_T,
            string3: INPUT_COMPATIBLE_T,
            string4: INPUT_COMPATIBLE_T,
            string5: INPUT_COMPATIBLE_T,
            string6: INPUT_COMPATIBLE_T,
            string7: INPUT_COMPATIBLE_T,
            string8: INPUT_COMPATIBLE_T,
        ):
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3
            self.string4 = string4
            self.string5 = string5
            self.string6 = string6
            self.string7 = string7
            self.string8 = string8

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

    class join9(ThirdBlock):

        def __init__(
            self,
            string1: INPUT_COMPATIBLE_T,
            string2: INPUT_COMPATIBLE_T,
            string3: INPUT_COMPATIBLE_T,
            string4: INPUT_COMPATIBLE_T,
            string5: INPUT_COMPATIBLE_T,
            string6: INPUT_COMPATIBLE_T,
            string7: INPUT_COMPATIBLE_T,
            string8: INPUT_COMPATIBLE_T,
            string9: INPUT_COMPATIBLE_T,
        ):
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3
            self.string4 = string4
            self.string5 = string5
            self.string6 = string6
            self.string7 = string7
            self.string8 = string8
            self.string9 = string9

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

    class menu_part(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmOperatorsExpansion::#menu:part", inputs={}, dropdowns={}
            )
