from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class operator:

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) + (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class subtract(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) - (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class multiply(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) * (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class divide(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) / (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class power(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) ^ (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class adv_math_expanded(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) * (OPERAND2) [OPERATION] (OPERAND3)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            ("OPERAND3", "operand3", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        operand3: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class adv_math(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) [OPERATION] (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class random(ThirdBlock):
        OPCODE: ClassVar = "&operators::pick random (OPERAND1) to (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class constrainnumber(ThirdBlock):
        OPCODE: ClassVar = "&operators::constrain (NUM) min (MIN) max (MAX)"
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
    class lerp_func(ThirdBlock):
        OPCODE: ClassVar = (
            "&operators::interpolate (OPERAND1) to (OPERAND2) by (WEIGHT)"
        )
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            ("WEIGHT", "weight", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        weight: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gt(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) > (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gtorequal(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) >= (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class lt(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) < (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ltorequal(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) <= (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class equals(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) = (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class notequal(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) != (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class true_boolean(ThirdBlock):
        OPCODE: ClassVar = "&operators::true"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class false_boolean(ThirdBlock):
        OPCODE: ClassVar = "&operators::false"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class and_(ThirdBlock):
        OPCODE: ClassVar = "&operators::<OPERAND1> and <OPERAND2>"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class or_(ThirdBlock):
        OPCODE: ClassVar = "&operators::<OPERAND1> or <OPERAND2>"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class not_(ThirdBlock):
        OPCODE: ClassVar = "&operators::not <OPERAND>"
        INPUT_SPECS: ClassVar = (
            ("OPERAND", "operand", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class new_line(ThirdBlock):
        OPCODE: ClassVar = "&operators::new line"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class tab_character(ThirdBlock):
        OPCODE: ClassVar = "&operators::tab character"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class join(ThirdBlock):
        OPCODE: ClassVar = "&operators::join (STRING1) (STRING2)"
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join3(ThirdBlock):
        OPCODE: ClassVar = "&operators::join (STRING1) (STRING2) (STRING3)"
        INPUT_SPECS: ClassVar = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class index_of_text_in_text(ThirdBlock):
        OPCODE: ClassVar = "&operators::index of (SUBSTRING) in (TEXT)"
        INPUT_SPECS: ClassVar = (
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substring: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class last_index_of_text_in_text(ThirdBlock):
        OPCODE: ClassVar = "&operators::last index of (SUBSTRING) in (TEXT)"
        INPUT_SPECS: ClassVar = (
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        substring: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class letter_of(ThirdBlock):
        OPCODE: ClassVar = "&operators::letter (LETTER) of (STRING)"
        INPUT_SPECS: ClassVar = (
            ("LETTER", "letter", p.SRBlockAndTextInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        letter: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_letters_from_index_to_index_in_text(ThirdBlock):
        OPCODE: ClassVar = "&operators::letters from (START) to (STOP) in (TEXT)"
        INPUT_SPECS: ClassVar = (
            ("START", "start", p.SRBlockAndTextInputValue, None),
            ("STOP", "stop", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        start: INPUT_COMPATIBLE_T
        stop: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class length(ThirdBlock):
        OPCODE: ClassVar = "&operators::length of (TEXT)"
        INPUT_SPECS: ClassVar = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class contains(ThirdBlock):
        OPCODE: ClassVar = "&operators::(TEXT) contains (SUBSTRING) ?"
        INPUT_SPECS: ClassVar = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T
        substring: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class text_starts_or_ends_with(ThirdBlock):
        OPCODE: ClassVar = "&operators::(TEXT) [OPERATION] with (SUBSTRING) ?"
        INPUT_SPECS: ClassVar = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
        text: INPUT_COMPATIBLE_T
        substring: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class replace_all(ThirdBlock):
        OPCODE: ClassVar = (
            "&operators::in (TEXT) replace all (OLDVALUE) with (NEWVALUE)"
        )
        INPUT_SPECS: ClassVar = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("OLDVALUE", "oldvalue", p.SRBlockAndTextInputValue, None),
            ("NEWVALUE", "newvalue", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T
        oldvalue: INPUT_COMPATIBLE_T
        newvalue: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class replace_first(ThirdBlock):
        OPCODE: ClassVar = (
            "&operators::in (TEXT) replace first (OLDVALUE) with (NEWVALUE)"
        )
        INPUT_SPECS: ClassVar = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("OLDVALUE", "oldvalue", p.SRBlockAndTextInputValue, None),
            ("NEWVALUE", "newvalue", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T
        oldvalue: INPUT_COMPATIBLE_T
        newvalue: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class regexmatch(ThirdBlock):
        OPCODE: ClassVar = "&operators::match (TEXT) with regex (REGEX) (MODIFIER)"
        INPUT_SPECS: ClassVar = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockAndTextInputValue, None),
            ("MODIFIER", "modifier", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T
        modifier: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_upper_lower_case(ThirdBlock):
        OPCODE: ClassVar = "&operators::(TEXT) to [CASE]"
        INPUT_SPECS: ClassVar = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("CASE", "case"),)
        text: INPUT_COMPATIBLE_T
        case: str

    @grepr_dataclass()
    class mod(ThirdBlock):
        OPCODE: ClassVar = "&operators::(OPERAND1) mod (OPERAND2)"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class round(ThirdBlock):
        OPCODE: ClassVar = "&operators::round (NUM)"
        INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mathop(ThirdBlock):
        OPCODE: ClassVar = "&operators::[OPERATION] of (NUM)"
        INPUT_SPECS: ClassVar = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("OPERATION", "operation"),)
        num: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class stringify(ThirdBlock):
        OPCODE: ClassVar = "&operators::(VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class boolify(ThirdBlock):
        OPCODE: ClassVar = "&operators::(VALUE) as a boolean"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class expandable_math(ThirdBlock):
        OPCODE: ClassVar = "&operators::{{EXPANDABLE MATH CHAIN}}"
        INPUT_SPECS: ClassVar = None
        DROPDOWN_SPECS: ClassVar = None

    @grepr_dataclass()
    class expandable_bool(ThirdBlock):
        OPCODE: ClassVar = "&operators::{{EXPANDABLE BOOL CHAIN}}"
        INPUT_SPECS: ClassVar = None
        DROPDOWN_SPECS: ClassVar = None

    @grepr_dataclass()
    class expandable_compare(ThirdBlock):
        OPCODE: ClassVar = "&operators::{{EXPANDABLE COMPARE CHAIN}}"
        INPUT_SPECS: ClassVar = None
        DROPDOWN_SPECS: ClassVar = None

    @grepr_dataclass()
    class expandablejoininputs(ThirdBlock):
        OPCODE: ClassVar = "&operators::{{EXPANDABLE JOIN CHAIN}}"
        INPUT_SPECS: ClassVar = None
        DROPDOWN_SPECS: ClassVar = None

    @grepr_dataclass()
    class nand(ThirdBlock):
        OPCODE: ClassVar = "&operator::<OPERAND1> nand <OPERAND2>"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nor(ThirdBlock):
        OPCODE: ClassVar = "&operator::<OPERAND1> nor <OPERAND2>"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class xor(ThirdBlock):
        OPCODE: ClassVar = "&operator::<OPERAND1> xor <OPERAND2>"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class xnor(ThirdBlock):
        OPCODE: ClassVar = "&operator::<OPERAND1> xnor <OPERAND2>"
        INPUT_SPECS: ClassVar = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class random_boolean(ThirdBlock):
        OPCODE: ClassVar = "&operator::random"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class count_appear_times(ThirdBlock):
        OPCODE: ClassVar = "&operator::amount of times (TEXT1) appears in (TEXT2)"
        INPUT_SPECS: ClassVar = (
            ("TEXT1", "text1", p.SRBlockAndTextInputValue, None),
            ("TEXT2", "text2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text1: INPUT_COMPATIBLE_T
        text2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class read_line_in_multiline_text(ThirdBlock):
        OPCODE: ClassVar = "&operator::read line (LINE) in (TEXT)"
        INPUT_SPECS: ClassVar = (
            ("LINE", "line", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        line: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class text_includes_letter_from(ThirdBlock):
        OPCODE: ClassVar = "&operator::(TEXT1) includes a letter from (TEXT2) ?"
        INPUT_SPECS: ClassVar = (
            ("TEXT1", "text1", p.SRBlockAndTextInputValue, None),
            ("TEXT2", "text2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        text1: INPUT_COMPATIBLE_T
        text2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class character_to_code(ThirdBlock):
        OPCODE: ClassVar = "&operator::character (ONE) to id"
        INPUT_SPECS: ClassVar = (("ONE", "one", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class code_to_character(ThirdBlock):
        OPCODE: ClassVar = "&operator::id (ONE) to character"
        INPUT_SPECS: ClassVar = (("ONE", "one", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        one: INPUT_COMPATIBLE_T
