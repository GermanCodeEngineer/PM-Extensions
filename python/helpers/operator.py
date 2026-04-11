from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class operator:

    @staticmethod
    def add(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) + (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def subtract(
        operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) - (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def multiply(
        operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) * (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def divide(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) / (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def power(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) ^ (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def adv_math_expanded(
        operand1: INPUT_COMPATIBLE_T,
        operand2: INPUT_COMPATIBLE_T,
        operand3: INPUT_COMPATIBLE_T,
        operation: str,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) * (OPERAND2) [OPERATION] (OPERAND3)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
                "OPERAND3": InputValue.try_as_input(
                    operand3, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={
                "OPERATION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, operation)
            },
        )

    @staticmethod
    def adv_math(
        operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T, operation: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) [OPERATION] (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={
                "OPERATION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, operation)
            },
        )

    @staticmethod
    def random(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::pick random (OPERAND1) to (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def constrainnumber(
        num: INPUT_COMPATIBLE_T, min: INPUT_COMPATIBLE_T, max: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::constrain (NUM) min (MIN) max (MAX)",
            inputs={
                "NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue),
                "MIN": InputValue.try_as_input(min, p.SRBlockAndTextInputValue),
                "MAX": InputValue.try_as_input(max, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def lerp_func(
        operand1: INPUT_COMPATIBLE_T,
        operand2: INPUT_COMPATIBLE_T,
        weight: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::interpolate (OPERAND1) to (OPERAND2) by (WEIGHT)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
                "WEIGHT": InputValue.try_as_input(weight, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def gt(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) > (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def gtorequal(
        operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) >= (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def lt(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) < (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def ltorequal(
        operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) <= (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def equals(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) = (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def notequal(
        operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) != (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def true_boolean() -> p.SRBlock:
        return p.SRBlock(opcode="&operators::true", inputs={}, dropdowns={})

    @staticmethod
    def false_boolean() -> p.SRBlock:
        return p.SRBlock(opcode="&operators::false", inputs={}, dropdowns={})

    @staticmethod
    def and_(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::<OPERAND1> and <OPERAND2>",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndBoolInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndBoolInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def or_(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::<OPERAND1> or <OPERAND2>",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndBoolInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndBoolInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def not_(operand: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::not <OPERAND>",
            inputs={
                "OPERAND": InputValue.try_as_input(operand, p.SRBlockAndBoolInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def new_line() -> p.SRBlock:
        return p.SRBlock(opcode="&operators::new line", inputs={}, dropdowns={})

    @staticmethod
    def tab_character() -> p.SRBlock:
        return p.SRBlock(opcode="&operators::tab character", inputs={}, dropdowns={})

    @staticmethod
    def join(string1: INPUT_COMPATIBLE_T, string2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::join (STRING1) (STRING2)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def join3(
        string1: INPUT_COMPATIBLE_T,
        string2: INPUT_COMPATIBLE_T,
        string3: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::join (STRING1) (STRING2) (STRING3)",
            inputs={
                "STRING1": InputValue.try_as_input(string1, p.SRBlockAndTextInputValue),
                "STRING2": InputValue.try_as_input(string2, p.SRBlockAndTextInputValue),
                "STRING3": InputValue.try_as_input(string3, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def index_of_text_in_text(
        substring: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::index of (SUBSTRING) in (TEXT)",
            inputs={
                "SUBSTRING": InputValue.try_as_input(
                    substring, p.SRBlockAndTextInputValue
                ),
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def last_index_of_text_in_text(
        substring: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::last index of (SUBSTRING) in (TEXT)",
            inputs={
                "SUBSTRING": InputValue.try_as_input(
                    substring, p.SRBlockAndTextInputValue
                ),
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def letter_of(letter: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::letter (LETTER) of (STRING)",
            inputs={
                "LETTER": InputValue.try_as_input(letter, p.SRBlockAndTextInputValue),
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_letters_from_index_to_index_in_text(
        start: INPUT_COMPATIBLE_T, stop: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::letters from (START) to (STOP) in (TEXT)",
            inputs={
                "START": InputValue.try_as_input(start, p.SRBlockAndTextInputValue),
                "STOP": InputValue.try_as_input(stop, p.SRBlockAndTextInputValue),
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def length(text: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::length of (TEXT)",
            inputs={"TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def contains(text: INPUT_COMPATIBLE_T, substring: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(TEXT) contains (SUBSTRING) ?",
            inputs={
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "SUBSTRING": InputValue.try_as_input(
                    substring, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def text_starts_or_ends_with(
        text: INPUT_COMPATIBLE_T, substring: INPUT_COMPATIBLE_T, operation: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(TEXT) [OPERATION] with (SUBSTRING) ?",
            inputs={
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "SUBSTRING": InputValue.try_as_input(
                    substring, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={
                "OPERATION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, operation)
            },
        )

    @staticmethod
    def replace_all(
        text: INPUT_COMPATIBLE_T,
        oldvalue: INPUT_COMPATIBLE_T,
        newvalue: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::in (TEXT) replace all (OLDVALUE) with (NEWVALUE)",
            inputs={
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "OLDVALUE": InputValue.try_as_input(
                    oldvalue, p.SRBlockAndTextInputValue
                ),
                "NEWVALUE": InputValue.try_as_input(
                    newvalue, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def replace_first(
        text: INPUT_COMPATIBLE_T,
        oldvalue: INPUT_COMPATIBLE_T,
        newvalue: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::in (TEXT) replace first (OLDVALUE) with (NEWVALUE)",
            inputs={
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "OLDVALUE": InputValue.try_as_input(
                    oldvalue, p.SRBlockAndTextInputValue
                ),
                "NEWVALUE": InputValue.try_as_input(
                    newvalue, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def regexmatch(
        text: INPUT_COMPATIBLE_T,
        regex: INPUT_COMPATIBLE_T,
        modifier: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::match (TEXT) with regex (REGEX) (MODIFIER)",
            inputs={
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "REGEX": InputValue.try_as_input(regex, p.SRBlockAndTextInputValue),
                "MODIFIER": InputValue.try_as_input(
                    modifier, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def to_upper_lower_case(text: INPUT_COMPATIBLE_T, case: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(TEXT) to [CASE]",
            inputs={"TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue)},
            dropdowns={"CASE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, case)},
        )

    @staticmethod
    def mod(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(OPERAND1) mod (OPERAND2)",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndTextInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def round(num: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::round (NUM)",
            inputs={"NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def mathop(num: INPUT_COMPATIBLE_T, operation: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::[OPERATION] of (NUM)",
            inputs={"NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue)},
            dropdowns={
                "OPERATION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, operation)
            },
        )

    @staticmethod
    def stringify(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def boolify(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operators::(VALUE) as a boolean",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def expandable_math() -> p.SRBlock:
        raise NotImplementedError(
            "This opcode is not supported yet, because it requires flexible input counts."
        )

    @staticmethod
    def expandable_bool() -> p.SRBlock:
        raise NotImplementedError(
            "This opcode is not supported yet, because it requires flexible input counts."
        )

    @staticmethod
    def expandable_compare() -> p.SRBlock:
        raise NotImplementedError(
            "This opcode is not supported yet, because it requires flexible input counts."
        )

    @staticmethod
    def expandablejoininputs() -> p.SRBlock:
        raise NotImplementedError(
            "This opcode is not supported yet, because it requires flexible input counts."
        )

    @staticmethod
    def nand(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::<OPERAND1> nand <OPERAND2>",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndBoolInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndBoolInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def nor(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::<OPERAND1> nor <OPERAND2>",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndBoolInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndBoolInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def xor(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::<OPERAND1> xor <OPERAND2>",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndBoolInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndBoolInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def xnor(operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::<OPERAND1> xnor <OPERAND2>",
            inputs={
                "OPERAND1": InputValue.try_as_input(
                    operand1, p.SRBlockAndBoolInputValue
                ),
                "OPERAND2": InputValue.try_as_input(
                    operand2, p.SRBlockAndBoolInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def random_boolean() -> p.SRBlock:
        return p.SRBlock(opcode="&operator::random", inputs={}, dropdowns={})

    @staticmethod
    def count_appear_times(
        text1: INPUT_COMPATIBLE_T, text2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::amount of times (TEXT1) appears in (TEXT2)",
            inputs={
                "TEXT1": InputValue.try_as_input(text1, p.SRBlockAndTextInputValue),
                "TEXT2": InputValue.try_as_input(text2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def read_line_in_multiline_text(
        line: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::read line (LINE) in (TEXT)",
            inputs={
                "LINE": InputValue.try_as_input(line, p.SRBlockAndTextInputValue),
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def text_includes_letter_from(
        text1: INPUT_COMPATIBLE_T, text2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::(TEXT1) includes a letter from (TEXT2) ?",
            inputs={
                "TEXT1": InputValue.try_as_input(text1, p.SRBlockAndTextInputValue),
                "TEXT2": InputValue.try_as_input(text2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def character_to_code(one: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::character (ONE) to id",
            inputs={"ONE": InputValue.try_as_input(one, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def code_to_character(one: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&operator::id (ONE) to character",
            inputs={"ONE": InputValue.try_as_input(one, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )
