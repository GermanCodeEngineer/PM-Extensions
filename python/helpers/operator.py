from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class operator:

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) + (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class subtract(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) - (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class multiply(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) * (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class divide(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) / (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class power(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) ^ (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class adv_math_expanded(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) * (OPERAND2) [OPERATION] (OPERAND3)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            ("OPERAND3", "operand3", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = (("OPERATION", "operation"),)
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        operand3: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class adv_math(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) [OPERATION] (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = (("OPERATION", "operation"),)
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class random(ThirdBlock):
        OPCODE = "&operators::pick random (OPERAND1) to (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class constrainnumber(ThirdBlock):
        OPCODE = "&operators::constrain (NUM) min (MIN) max (MAX)"
        INPUT_SPECS = (
            ("NUM", "num", p.SRBlockAndTextInputValue, None),
            ("MIN", "min", p.SRBlockAndTextInputValue, None),
            ("MAX", "max", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        num: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class lerp_func(ThirdBlock):
        OPCODE = "&operators::interpolate (OPERAND1) to (OPERAND2) by (WEIGHT)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
            ("WEIGHT", "weight", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        weight: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gt(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) > (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gtorequal(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) >= (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class lt(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) < (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ltorequal(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) <= (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class equals(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) = (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class notequal(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) != (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class true_boolean(ThirdBlock):
        OPCODE = "&operators::true"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class false_boolean(ThirdBlock):
        OPCODE = "&operators::false"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class and_(ThirdBlock):
        OPCODE = "&operators::<OPERAND1> and <OPERAND2>"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class or_(ThirdBlock):
        OPCODE = "&operators::<OPERAND1> or <OPERAND2>"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class not_(ThirdBlock):
        OPCODE = "&operators::not <OPERAND>"
        INPUT_SPECS = (("OPERAND", "operand", p.SRBlockAndBoolInputValue, None),)
        DROPDOWN_SPECS = ()
        operand: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class new_line(ThirdBlock):
        OPCODE = "&operators::new line"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class tab_character(ThirdBlock):
        OPCODE = "&operators::tab character"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class join(ThirdBlock):
        OPCODE = "&operators::join (STRING1) (STRING2)"
        INPUT_SPECS = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class join3(ThirdBlock):
        OPCODE = "&operators::join (STRING1) (STRING2) (STRING3)"
        INPUT_SPECS = (
            ("STRING1", "string1", p.SRBlockAndTextInputValue, None),
            ("STRING2", "string2", p.SRBlockAndTextInputValue, None),
            ("STRING3", "string3", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class index_of_text_in_text(ThirdBlock):
        OPCODE = "&operators::index of (SUBSTRING) in (TEXT)"
        INPUT_SPECS = (
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substring: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class last_index_of_text_in_text(ThirdBlock):
        OPCODE = "&operators::last index of (SUBSTRING) in (TEXT)"
        INPUT_SPECS = (
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        substring: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class letter_of(ThirdBlock):
        OPCODE = "&operators::letter (LETTER) of (STRING)"
        INPUT_SPECS = (
            ("LETTER", "letter", p.SRBlockAndTextInputValue, None),
            ("STRING", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        letter: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_letters_from_index_to_index_in_text(ThirdBlock):
        OPCODE = "&operators::letters from (START) to (STOP) in (TEXT)"
        INPUT_SPECS = (
            ("START", "start", p.SRBlockAndTextInputValue, None),
            ("STOP", "stop", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        start: INPUT_COMPATIBLE_T
        stop: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class length(ThirdBlock):
        OPCODE = "&operators::length of (TEXT)"
        INPUT_SPECS = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class contains(ThirdBlock):
        OPCODE = "&operators::(TEXT) contains (SUBSTRING) ?"
        INPUT_SPECS = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T
        substring: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class text_starts_or_ends_with(ThirdBlock):
        OPCODE = "&operators::(TEXT) [OPERATION] with (SUBSTRING) ?"
        INPUT_SPECS = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("SUBSTRING", "substring", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = (("OPERATION", "operation"),)
        text: INPUT_COMPATIBLE_T
        substring: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class replace_all(ThirdBlock):
        OPCODE = "&operators::in (TEXT) replace all (OLDVALUE) with (NEWVALUE)"
        INPUT_SPECS = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("OLDVALUE", "oldvalue", p.SRBlockAndTextInputValue, None),
            ("NEWVALUE", "newvalue", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T
        oldvalue: INPUT_COMPATIBLE_T
        newvalue: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class replace_first(ThirdBlock):
        OPCODE = "&operators::in (TEXT) replace first (OLDVALUE) with (NEWVALUE)"
        INPUT_SPECS = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("OLDVALUE", "oldvalue", p.SRBlockAndTextInputValue, None),
            ("NEWVALUE", "newvalue", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T
        oldvalue: INPUT_COMPATIBLE_T
        newvalue: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class regexmatch(ThirdBlock):
        OPCODE = "&operators::match (TEXT) with regex (REGEX) (MODIFIER)"
        INPUT_SPECS = (
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
            ("REGEX", "regex", p.SRBlockAndTextInputValue, None),
            ("MODIFIER", "modifier", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T
        modifier: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class to_upper_lower_case(ThirdBlock):
        OPCODE = "&operators::(TEXT) to [CASE]"
        INPUT_SPECS = (("TEXT", "text", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("CASE", "case"),)
        text: INPUT_COMPATIBLE_T
        case: str

    @grepr_dataclass()
    class mod(ThirdBlock):
        OPCODE = "&operators::(OPERAND1) mod (OPERAND2)"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndTextInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class round(ThirdBlock):
        OPCODE = "&operators::round (NUM)"
        INPUT_SPECS = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class mathop(ThirdBlock):
        OPCODE = "&operators::[OPERATION] of (NUM)"
        INPUT_SPECS = (("NUM", "num", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("OPERATION", "operation"),)
        num: INPUT_COMPATIBLE_T
        operation: str

    @grepr_dataclass()
    class stringify(ThirdBlock):
        OPCODE = "&operators::(VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class boolify(ThirdBlock):
        OPCODE = "&operators::(VALUE) as a boolean"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class expandable_math(ThirdBlock):
        OPCODE = "&operators::{{EXPANDABLE MATH CHAIN}}"
        INPUT_SPECS = None
        DROPDOWN_SPECS = None

    @grepr_dataclass()
    class expandable_bool(ThirdBlock):
        OPCODE = "&operators::{{EXPANDABLE BOOL CHAIN}}"
        INPUT_SPECS = None
        DROPDOWN_SPECS = None

    @grepr_dataclass()
    class expandable_compare(ThirdBlock):
        OPCODE = "&operators::{{EXPANDABLE COMPARE CHAIN}}"
        INPUT_SPECS = None
        DROPDOWN_SPECS = None

    @grepr_dataclass()
    class expandablejoininputs(ThirdBlock):
        OPCODE = "&operators::{{EXPANDABLE JOIN CHAIN}}"
        INPUT_SPECS = None
        DROPDOWN_SPECS = None

    @grepr_dataclass()
    class nand(ThirdBlock):
        OPCODE = "&operator::<OPERAND1> nand <OPERAND2>"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class nor(ThirdBlock):
        OPCODE = "&operator::<OPERAND1> nor <OPERAND2>"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class xor(ThirdBlock):
        OPCODE = "&operator::<OPERAND1> xor <OPERAND2>"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class xnor(ThirdBlock):
        OPCODE = "&operator::<OPERAND1> xnor <OPERAND2>"
        INPUT_SPECS = (
            ("OPERAND1", "operand1", p.SRBlockAndBoolInputValue, None),
            ("OPERAND2", "operand2", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class random_boolean(ThirdBlock):
        OPCODE = "&operator::random"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class count_appear_times(ThirdBlock):
        OPCODE = "&operator::amount of times (TEXT1) appears in (TEXT2)"
        INPUT_SPECS = (
            ("TEXT1", "text1", p.SRBlockAndTextInputValue, None),
            ("TEXT2", "text2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text1: INPUT_COMPATIBLE_T
        text2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class read_line_in_multiline_text(ThirdBlock):
        OPCODE = "&operator::read line (LINE) in (TEXT)"
        INPUT_SPECS = (
            ("LINE", "line", p.SRBlockAndTextInputValue, None),
            ("TEXT", "text", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        line: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class text_includes_letter_from(ThirdBlock):
        OPCODE = "&operator::(TEXT1) includes a letter from (TEXT2) ?"
        INPUT_SPECS = (
            ("TEXT1", "text1", p.SRBlockAndTextInputValue, None),
            ("TEXT2", "text2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        text1: INPUT_COMPATIBLE_T
        text2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class character_to_code(ThirdBlock):
        OPCODE = "&operator::character (ONE) to id"
        INPUT_SPECS = (("ONE", "one", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class code_to_character(ThirdBlock):
        OPCODE = "&operator::id (ONE) to character"
        INPUT_SPECS = (("ONE", "one", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        one: INPUT_COMPATIBLE_T
