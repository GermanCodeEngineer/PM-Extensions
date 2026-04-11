from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class pmOperatorsExpansion:

    @staticmethod
    def shift_left(num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::(num1) << (num2)",
            inputs={
                "num1": InputValue.try_as_input(num1, p.SRBlockAndTextInputValue),
                "num2": InputValue.try_as_input(num2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def shift_right(num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::(num1) >> (num2)",
            inputs={
                "num1": InputValue.try_as_input(num1, p.SRBlockAndTextInputValue),
                "num2": InputValue.try_as_input(num2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def binnary_and(num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::(num1) & (num2)",
            inputs={
                "num1": InputValue.try_as_input(num1, p.SRBlockAndTextInputValue),
                "num2": InputValue.try_as_input(num2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def binnary_or(num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::(num1) | (num2)",
            inputs={
                "num1": InputValue.try_as_input(num1, p.SRBlockAndTextInputValue),
                "num2": InputValue.try_as_input(num2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def binnary_xor(num1: INPUT_COMPATIBLE_T, num2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::(num1) ^ (num2)",
            inputs={
                "num1": InputValue.try_as_input(num1, p.SRBlockAndTextInputValue),
                "num2": InputValue.try_as_input(num2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def binnary_not(num1: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::~ (num1)",
            inputs={"num1": InputValue.try_as_input(num1, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def or_if_falsey(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::(ONE) or else (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockAndTextInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def if_is_truthy(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::if <ONE> is true then (TWO)",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockAndBoolInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_number_multiple_of(
        num: INPUT_COMPATIBLE_T, multiple: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::is (NUM) multiple of [MULTIPLE]?",
            inputs={
                "NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue),
                "MULTIPLE": InputValue.try_as_input(
                    multiple, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def is_integer(num: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::is (NUM) an integer?",
            inputs={"NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def is_prime(num: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::is (NUM) a prime number?",
            inputs={"NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def is_even(num: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::is (NUM) even?",
            inputs={"NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def between_numbers(
        num: INPUT_COMPATIBLE_T, min: INPUT_COMPATIBLE_T, max: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::is (NUM) between (MIN) and [MAX]?",
            inputs={
                "NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue),
                "MIN": InputValue.try_as_input(min, p.SRBlockAndTextInputValue),
                "MAX": InputValue.try_as_input(max, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def evaluate_math(equation: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::answer to (EQUATION)",
            inputs={
                "EQUATION": InputValue.try_as_input(
                    equation, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def part_of_ratio(part: INPUT_COMPATIBLE_T, ratio: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::([PART]) part of ratio (RATIO)",
            inputs={
                "PART": InputValue.try_as_input(part, p.SRBlockAndDropdownInputValue),
                "RATIO": InputValue.try_as_input(ratio, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def simplify_ratio(ratio: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::simplify ratio (RATIO)",
            inputs={
                "RATIO": InputValue.try_as_input(ratio, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def pi() -> p.SRBlock:
        return p.SRBlock(opcode="&pmOperatorsExpansion::π", inputs={}, dropdowns={})

    @staticmethod
    def euler() -> p.SRBlock:
        return p.SRBlock(opcode="&pmOperatorsExpansion::e", inputs={}, dropdowns={})

    @staticmethod
    def infinity() -> p.SRBlock:
        return p.SRBlock(opcode="&pmOperatorsExpansion::∞", inputs={}, dropdowns={})

    @staticmethod
    def truncate_number(num: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::truncate number (NUM)",
            inputs={"NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def atan2(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::atan2 of x (X) y (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def reverse_chars(text: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::reverse (TEXT)",
            inputs={"TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def shuffle_chars(text: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::shuffle (TEXT)",
            inputs={"TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def text_after(text: INPUT_COMPATIBLE_T, base: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::text after (TEXT) in (BASE)",
            inputs={
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "BASE": InputValue.try_as_input(base, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def text_before(text: INPUT_COMPATIBLE_T, base: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::text before (TEXT) in (BASE)",
            inputs={
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "BASE": InputValue.try_as_input(base, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def exactly_equal(one: INPUT_COMPATIBLE_T, two: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::(ONE) exactly equals [TWO]?",
            inputs={
                "ONE": InputValue.try_as_input(one, p.SRBlockAndTextInputValue),
                "TWO": InputValue.try_as_input(two, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_replacer(
        replacer: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::set replacer (REPLACER) to (TEXT)",
            inputs={
                "REPLACER": InputValue.try_as_input(
                    replacer, p.SRBlockAndTextInputValue
                ),
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def reset_replacers() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::reset replacers", inputs={}, dropdowns={}
        )

    @staticmethod
    def apply_replacers(text: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::apply replacers to (TEXT)",
            inputs={"TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def speed_to_pitch(speed: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::speed (SPEED) to pitch",
            inputs={
                "SPEED": InputValue.try_as_input(speed, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def pitch_to_speed(pitch: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::pitch (PITCH) to speed",
            inputs={
                "PITCH": InputValue.try_as_input(pitch, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def join4(
        string1: INPUT_COMPATIBLE_T,
        string2: INPUT_COMPATIBLE_T,
        string3: INPUT_COMPATIBLE_T,
        string4: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
                "STRING3": InputValue.try_as_input(string3, p.SRBlockAndTextInputValue),
                "STRING4": InputValue.try_as_input(string4, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def join5(
        string1: INPUT_COMPATIBLE_T,
        string2: INPUT_COMPATIBLE_T,
        string3: INPUT_COMPATIBLE_T,
        string4: INPUT_COMPATIBLE_T,
        string5: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
                "STRING3": InputValue.try_as_input(string3, p.SRBlockAndTextInputValue),
                "STRING4": InputValue.try_as_input(string4, p.SRBlockAndTextInputValue),
                "STRING5": InputValue.try_as_input(string5, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def join6(
        string1: INPUT_COMPATIBLE_T,
        string2: INPUT_COMPATIBLE_T,
        string3: INPUT_COMPATIBLE_T,
        string4: INPUT_COMPATIBLE_T,
        string5: INPUT_COMPATIBLE_T,
        string6: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
                "STRING3": InputValue.try_as_input(string3, p.SRBlockAndTextInputValue),
                "STRING4": InputValue.try_as_input(string4, p.SRBlockAndTextInputValue),
                "STRING5": InputValue.try_as_input(string5, p.SRBlockAndTextInputValue),
                "STRING6": InputValue.try_as_input(string6, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def join7(
        string1: INPUT_COMPATIBLE_T,
        string2: INPUT_COMPATIBLE_T,
        string3: INPUT_COMPATIBLE_T,
        string4: INPUT_COMPATIBLE_T,
        string5: INPUT_COMPATIBLE_T,
        string6: INPUT_COMPATIBLE_T,
        string7: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
                "STRING3": InputValue.try_as_input(string3, p.SRBlockAndTextInputValue),
                "STRING4": InputValue.try_as_input(string4, p.SRBlockAndTextInputValue),
                "STRING5": InputValue.try_as_input(string5, p.SRBlockAndTextInputValue),
                "STRING6": InputValue.try_as_input(string6, p.SRBlockAndTextInputValue),
                "STRING7": InputValue.try_as_input(string7, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def join8(
        string1: INPUT_COMPATIBLE_T,
        string2: INPUT_COMPATIBLE_T,
        string3: INPUT_COMPATIBLE_T,
        string4: INPUT_COMPATIBLE_T,
        string5: INPUT_COMPATIBLE_T,
        string6: INPUT_COMPATIBLE_T,
        string7: INPUT_COMPATIBLE_T,
        string8: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
                "STRING3": InputValue.try_as_input(string3, p.SRBlockAndTextInputValue),
                "STRING4": InputValue.try_as_input(string4, p.SRBlockAndTextInputValue),
                "STRING5": InputValue.try_as_input(string5, p.SRBlockAndTextInputValue),
                "STRING6": InputValue.try_as_input(string6, p.SRBlockAndTextInputValue),
                "STRING7": InputValue.try_as_input(string7, p.SRBlockAndTextInputValue),
                "STRING8": InputValue.try_as_input(string8, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def join9(
        string1: INPUT_COMPATIBLE_T,
        string2: INPUT_COMPATIBLE_T,
        string3: INPUT_COMPATIBLE_T,
        string4: INPUT_COMPATIBLE_T,
        string5: INPUT_COMPATIBLE_T,
        string6: INPUT_COMPATIBLE_T,
        string7: INPUT_COMPATIBLE_T,
        string8: INPUT_COMPATIBLE_T,
        string9: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8) (STRING9)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
                "STRING3": InputValue.try_as_input(string3, p.SRBlockAndTextInputValue),
                "STRING4": InputValue.try_as_input(string4, p.SRBlockAndTextInputValue),
                "STRING5": InputValue.try_as_input(string5, p.SRBlockAndTextInputValue),
                "STRING6": InputValue.try_as_input(string6, p.SRBlockAndTextInputValue),
                "STRING7": InputValue.try_as_input(string7, p.SRBlockAndTextInputValue),
                "STRING8": InputValue.try_as_input(string8, p.SRBlockAndTextInputValue),
                "STRING9": InputValue.try_as_input(string9, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_part() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmOperatorsExpansion::#menu:part", inputs={}, dropdowns={}
        )
