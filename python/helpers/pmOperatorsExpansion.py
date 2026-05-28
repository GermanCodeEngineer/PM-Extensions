from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class pmOperatorsExpansion:

    @grepr_dataclass()
    class shift_left(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) << (num2)"
        INPUT_SPECS: ClassVar = (
            ("num1", "num1", p.SRBlockAndTextInputValue, None),
            ("num2", "num2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class shift_right(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) >> (num2)"
        INPUT_SPECS: ClassVar = (
            ("num1", "num1", p.SRBlockAndTextInputValue, None),
            ("num2", "num2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class binnary_and(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) & (num2)"
        INPUT_SPECS: ClassVar = (
            ("num1", "num1", p.SRBlockAndTextInputValue, None),
            ("num2", "num2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class binnary_or(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) | (num2)"
        INPUT_SPECS: ClassVar = (
            ("num1", "num1", p.SRBlockAndTextInputValue, None),
            ("num2", "num2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class binnary_xor(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::(num1) ^ (num2)"
        INPUT_SPECS: ClassVar = (
            ("num1", "num1", p.SRBlockAndTextInputValue, None),
            ("num2", "num2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        num1: INPUT_COMPATIBLE_T
        num2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class binnary_not(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::~ (num1)"
        INPUT_SPECS: ClassVar = (("num1", "num1", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        num1: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class or_if_falsey(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::(ONE) or else (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockAndTextInputValue, None),
            ("TWO", "two", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class if_is_truthy(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::if <ONE> is true then (TWO)"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockAndBoolInputValue, None),
            ("TWO", "two", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_number_multiple_of(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) multiple of [MULTIPLE]?"
        INPUT_SPECS: ClassVar = (
            ("NUM", "num", p.SRBlockAndTextInputValue, None),
            ("MULTIPLE", "multiple", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        num: INPUT_COMPATIBLE_T
        multiple: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_integer(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) an integer?"
        INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_prime(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) a prime number?"
        INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_even(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) even?"
        INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class between_numbers(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::is (NUM) between (MIN) and [MAX]?"
        INPUT_SPECS: ClassVar = (
            ("NUM", "num", p.SRBlockAndTextInputValue, None),
            ("MIN", "min", p.SRBlockAndTextInputValue, None),
            ("MAX", "max", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        num: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class evaluate_math(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::answer to (EQUATION)"
        INPUT_SPECS: ClassVar = (
            ("EQUATION", "equation", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        equation: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class part_of_ratio(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::([PART]) part of ratio (RATIO)"
        INPUT_SPECS: ClassVar = (
            ("PART", "part", p.SRBlockAndDropdownInputValue, None),
            ("RATIO", "ratio", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        part: INPUT_COMPATIBLE_T
        ratio: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class simplify_ratio(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::simplify ratio (RATIO)"
        INPUT_SPECS: ClassVar = (("RATIO", "ratio", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        ratio: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pi(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::π"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class euler(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::e"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class infinity(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::∞"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class truncate_number(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::truncate number (NUM)"
        INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class atan2(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::atan2 of x (X) y (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reverse_chars(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::reverse (TEXT)"
        INPUT_SPECS: ClassVar = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class shuffle_chars(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::shuffle (TEXT)"
        INPUT_SPECS: ClassVar = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class text_after(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::text after (TEXT) in (BASE)"
        INPUT_SPECS: ClassVar = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("BASE", "base", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T
        base: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class text_before(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::text before (TEXT) in (BASE)"
        INPUT_SPECS: ClassVar = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("BASE", "base", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T
        base: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class exactly_equal(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::(ONE) exactly equals [TWO]?"
        INPUT_SPECS: ClassVar = (
            ("ONE", "one", p.SRBlockAndTextInputValue, None),
            ("TWO", "two", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
        two: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_replacer(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::set replacer (REPLACER) to (TEXT)"
        INPUT_SPECS: ClassVar = (
            ("REPLACER", "replacer", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        replacer: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class reset_replacers(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::reset replacers"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class apply_replacers(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::apply replacers to (TEXT)"
        INPUT_SPECS: ClassVar = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class speed_to_pitch(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::speed (SPEED) to pitch"
        INPUT_SPECS: ClassVar = (("SPEED", "speed", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        speed: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pitch_to_speed(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::pitch (PITCH) to speed"
        INPUT_SPECS: ClassVar = (("PITCH", "pitch", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        pitch: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join4(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4)"
        )
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
            ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join5(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5)"
        )
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
            ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
            ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join6(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6)"
        )
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
            ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
            ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
            ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join7(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7)"
        )
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
            ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
            ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
            ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
            ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join8(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8)"
        )
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
            ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
            ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
            ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
            ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
            ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T
        string8: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join9(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmOperatorsExpansion::join (STRING1) (STRING2) (STRING3) (STRING4) (STRING5) (STRING6) (STRING7) (STRING8) (STRING9)"
        )
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
            ("STRING4", "string4", p.SRBlockAndTextInputValue, None),
            ("STRING5", "string5", p.SRBlockAndTextInputValue, None),
            ("STRING6", "string6", p.SRBlockAndTextInputValue, None),
            ("STRING7", "string7", p.SRBlockAndTextInputValue, None),
            ("STRING8", "string8", p.SRBlockAndTextInputValue, None),
            ("STRING9", "string9", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T
        string4: INPUT_COMPATIBLE_T
        string5: INPUT_COMPATIBLE_T
        string6: INPUT_COMPATIBLE_T
        string7: INPUT_COMPATIBLE_T
        string8: INPUT_COMPATIBLE_T
        string9: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_part(ThirdBlock):
        OPCODE: ClassVar = "&pmOperatorsExpansion::#menu:part"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
