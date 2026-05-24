from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class operator:

    @grepr_dataclass()
    class add(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) + (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class subtract(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) - (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class multiply(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) * (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class divide(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) / (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class power(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) ^ (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class adv_math_expanded(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        operand3: INPUT_COMPATIBLE_T
        operation: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) * (OPERAND2) [OPERATION] (OPERAND3)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND3": ThirdInputValue.as_input(
                        self.operand3, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "OPERATION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.operation
                    )
                },
            )

    @grepr_dataclass()
    class adv_math(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        operation: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) [OPERATION] (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "OPERATION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.operation
                    )
                },
            )

    @grepr_dataclass()
    class random(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::pick random (OPERAND1) to (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class constrainnumber(ThirdBlock):
        num: INPUT_COMPATIBLE_T
        min: INPUT_COMPATIBLE_T
        max: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::constrain (NUM) min (MIN) max (MAX)",
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
    class lerp_func(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T
        weight: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::interpolate (OPERAND1) to (OPERAND2) by (WEIGHT)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                    "WEIGHT": ThirdInputValue.as_input(
                        self.weight, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class gt(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) > (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class gtorequal(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) >= (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class lt(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) < (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class ltorequal(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) <= (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class equals(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) = (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class notequal(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) != (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class true_boolean(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operators::true", inputs={}, dropdowns={})

    @grepr_dataclass()
    class false_boolean(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operators::false", inputs={}, dropdowns={})

    @grepr_dataclass()
    class and_(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::<OPERAND1> and <OPERAND2>",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndBoolInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class or_(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::<OPERAND1> or <OPERAND2>",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndBoolInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class not_(ThirdBlock):
        operand: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::not <OPERAND>",
                inputs={
                    "OPERAND": ThirdInputValue.as_input(
                        self.operand, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class new_line(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operators::new line", inputs={}, dropdowns={})

    @grepr_dataclass()
    class tab_character(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::tab character", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class join(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::join (STRING1) (STRING2)",
                inputs={
                    "STRING1": ThirdInputValue.as_input(
                        self.string1, p.SRBlockAndTextInputValue
                    ),
                    "STRING2": ThirdInputValue.as_input(
                        self.string2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class join3(ThirdBlock):
        string1: INPUT_COMPATIBLE_T
        string2: INPUT_COMPATIBLE_T
        string3: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::join (STRING1) (STRING2) (STRING3)",
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
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class index_of_text_in_text(ThirdBlock):
        substring: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::index of (SUBSTRING) in (TEXT)",
                inputs={
                    "SUBSTRING": ThirdInputValue.as_input(
                        self.substring, p.SRBlockAndTextInputValue
                    ),
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class last_index_of_text_in_text(ThirdBlock):
        substring: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::last index of (SUBSTRING) in (TEXT)",
                inputs={
                    "SUBSTRING": ThirdInputValue.as_input(
                        self.substring, p.SRBlockAndTextInputValue
                    ),
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class letter_of(ThirdBlock):
        letter: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::letter (LETTER) of (STRING)",
                inputs={
                    "LETTER": ThirdInputValue.as_input(
                        self.letter, p.SRBlockAndTextInputValue
                    ),
                    "STRING": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_letters_from_index_to_index_in_text(ThirdBlock):
        start: INPUT_COMPATIBLE_T
        stop: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::letters from (START) to (STOP) in (TEXT)",
                inputs={
                    "START": ThirdInputValue.as_input(
                        self.start, p.SRBlockAndTextInputValue
                    ),
                    "STOP": ThirdInputValue.as_input(
                        self.stop, p.SRBlockAndTextInputValue
                    ),
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class length(ThirdBlock):
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::length of (TEXT)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class contains(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        substring: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(TEXT) contains (SUBSTRING) ?",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTRING": ThirdInputValue.as_input(
                        self.substring, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class text_starts_or_ends_with(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        substring: INPUT_COMPATIBLE_T
        operation: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(TEXT) [OPERATION] with (SUBSTRING) ?",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTRING": ThirdInputValue.as_input(
                        self.substring, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "OPERATION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.operation
                    )
                },
            )

    @grepr_dataclass()
    class replace_all(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        oldvalue: INPUT_COMPATIBLE_T
        newvalue: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::in (TEXT) replace all (OLDVALUE) with (NEWVALUE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "OLDVALUE": ThirdInputValue.as_input(
                        self.oldvalue, p.SRBlockAndTextInputValue
                    ),
                    "NEWVALUE": ThirdInputValue.as_input(
                        self.newvalue, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class replace_first(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        oldvalue: INPUT_COMPATIBLE_T
        newvalue: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::in (TEXT) replace first (OLDVALUE) with (NEWVALUE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "OLDVALUE": ThirdInputValue.as_input(
                        self.oldvalue, p.SRBlockAndTextInputValue
                    ),
                    "NEWVALUE": ThirdInputValue.as_input(
                        self.newvalue, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class regexmatch(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T
        modifier: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::match (TEXT) with regex (REGEX) (MODIFIER)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "REGEX": ThirdInputValue.as_input(
                        self.regex, p.SRBlockAndTextInputValue
                    ),
                    "MODIFIER": ThirdInputValue.as_input(
                        self.modifier, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class to_upper_lower_case(ThirdBlock):
        text: INPUT_COMPATIBLE_T
        case: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(TEXT) to [CASE]",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "CASE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.case)
                },
            )

    @grepr_dataclass()
    class mod(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(OPERAND1) mod (OPERAND2)",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndTextInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class round(ThirdBlock):
        num: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::round (NUM)",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class mathop(ThirdBlock):
        num: INPUT_COMPATIBLE_T
        operation: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::[OPERATION] of (NUM)",
                inputs={
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "OPERATION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.operation
                    )
                },
            )

    @grepr_dataclass()
    class stringify(ThirdBlock):
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class boolify(ThirdBlock):
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::(VALUE) as a boolean",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class expandable_math(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    @grepr_dataclass()
    class expandable_bool(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    @grepr_dataclass()
    class expandable_compare(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    @grepr_dataclass()
    class expandablejoininputs(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    @grepr_dataclass()
    class nand(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::<OPERAND1> nand <OPERAND2>",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndBoolInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class nor(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::<OPERAND1> nor <OPERAND2>",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndBoolInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class xor(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::<OPERAND1> xor <OPERAND2>",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndBoolInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class xnor(ThirdBlock):
        operand1: INPUT_COMPATIBLE_T
        operand2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::<OPERAND1> xnor <OPERAND2>",
                inputs={
                    "OPERAND1": ThirdInputValue.as_input(
                        self.operand1, p.SRBlockAndBoolInputValue
                    ),
                    "OPERAND2": ThirdInputValue.as_input(
                        self.operand2, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class random_boolean(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operator::random", inputs={}, dropdowns={})

    @grepr_dataclass()
    class count_appear_times(ThirdBlock):
        text1: INPUT_COMPATIBLE_T
        text2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::amount of times (TEXT1) appears in (TEXT2)",
                inputs={
                    "TEXT1": ThirdInputValue.as_input(
                        self.text1, p.SRBlockAndTextInputValue
                    ),
                    "TEXT2": ThirdInputValue.as_input(
                        self.text2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class read_line_in_multiline_text(ThirdBlock):
        line: INPUT_COMPATIBLE_T
        text: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::read line (LINE) in (TEXT)",
                inputs={
                    "LINE": ThirdInputValue.as_input(
                        self.line, p.SRBlockAndTextInputValue
                    ),
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class text_includes_letter_from(ThirdBlock):
        text1: INPUT_COMPATIBLE_T
        text2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::(TEXT1) includes a letter from (TEXT2) ?",
                inputs={
                    "TEXT1": ThirdInputValue.as_input(
                        self.text1, p.SRBlockAndTextInputValue
                    ),
                    "TEXT2": ThirdInputValue.as_input(
                        self.text2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class character_to_code(ThirdBlock):
        one: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::character (ONE) to id",
                inputs={
                    "ONE": ThirdInputValue.as_input(
                        self.one, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class code_to_character(ThirdBlock):
        one: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operator::id (ONE) to character",
                inputs={
                    "ONE": ThirdInputValue.as_input(
                        self.one, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )
