from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class operator:

    class add(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class subtract(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class multiply(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class divide(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class power(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class adv_math_expanded(ThirdBlock):

        def __init__(
            self,
            operand1: INPUT_COMPATIBLE_T,
            operand2: INPUT_COMPATIBLE_T,
            operand3: INPUT_COMPATIBLE_T,
            operation: str,
        ):
            self.operand1 = operand1
            self.operand2 = operand2
            self.operand3 = operand3
            self.operation = operation

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

    class adv_math(ThirdBlock):

        def __init__(
            self,
            operand1: INPUT_COMPATIBLE_T,
            operand2: INPUT_COMPATIBLE_T,
            operation: str,
        ):
            self.operand1 = operand1
            self.operand2 = operand2
            self.operation = operation

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

    class random(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class constrainnumber(ThirdBlock):

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

    class lerp_func(ThirdBlock):

        def __init__(
            self,
            operand1: INPUT_COMPATIBLE_T,
            operand2: INPUT_COMPATIBLE_T,
            weight: INPUT_COMPATIBLE_T,
        ):
            self.operand1 = operand1
            self.operand2 = operand2
            self.weight = weight

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

    class gt(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class gtorequal(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class lt(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class ltorequal(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class equals(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class notequal(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class true_boolean(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operators::true", inputs={}, dropdowns={})

    class false_boolean(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operators::false", inputs={}, dropdowns={})

    class and_(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class or_(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class not_(ThirdBlock):

        def __init__(self, operand: INPUT_COMPATIBLE_T):
            self.operand = operand

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

    class new_line(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operators::new line", inputs={}, dropdowns={})

    class tab_character(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&operators::tab character", inputs={}, dropdowns={}
            )

    class join(ThirdBlock):

        def __init__(self, string1: INPUT_COMPATIBLE_T, string2: INPUT_COMPATIBLE_T):
            self.string1 = string1
            self.string2 = string2

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

    class join3(ThirdBlock):

        def __init__(
            self,
            string1: INPUT_COMPATIBLE_T,
            string2: INPUT_COMPATIBLE_T,
            string3: INPUT_COMPATIBLE_T,
        ):
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3

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

    class index_of_text_in_text(ThirdBlock):

        def __init__(self, substring: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T):
            self.substring = substring
            self.text = text

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

    class last_index_of_text_in_text(ThirdBlock):

        def __init__(self, substring: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T):
            self.substring = substring
            self.text = text

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

    class letter_of(ThirdBlock):

        def __init__(self, letter: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T):
            self.letter = letter
            self.string = string

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

    class get_letters_from_index_to_index_in_text(ThirdBlock):

        def __init__(
            self,
            start: INPUT_COMPATIBLE_T,
            stop: INPUT_COMPATIBLE_T,
            text: INPUT_COMPATIBLE_T,
        ):
            self.start = start
            self.stop = stop
            self.text = text

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

    class length(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T):
            self.text = text

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

    class contains(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T, substring: INPUT_COMPATIBLE_T):
            self.text = text
            self.substring = substring

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

    class text_starts_or_ends_with(ThirdBlock):

        def __init__(
            self,
            text: INPUT_COMPATIBLE_T,
            substring: INPUT_COMPATIBLE_T,
            operation: str,
        ):
            self.text = text
            self.substring = substring
            self.operation = operation

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

    class replace_all(ThirdBlock):

        def __init__(
            self,
            text: INPUT_COMPATIBLE_T,
            oldvalue: INPUT_COMPATIBLE_T,
            newvalue: INPUT_COMPATIBLE_T,
        ):
            self.text = text
            self.oldvalue = oldvalue
            self.newvalue = newvalue

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

    class replace_first(ThirdBlock):

        def __init__(
            self,
            text: INPUT_COMPATIBLE_T,
            oldvalue: INPUT_COMPATIBLE_T,
            newvalue: INPUT_COMPATIBLE_T,
        ):
            self.text = text
            self.oldvalue = oldvalue
            self.newvalue = newvalue

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

    class regexmatch(ThirdBlock):

        def __init__(
            self,
            text: INPUT_COMPATIBLE_T,
            regex: INPUT_COMPATIBLE_T,
            modifier: INPUT_COMPATIBLE_T,
        ):
            self.text = text
            self.regex = regex
            self.modifier = modifier

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

    class to_upper_lower_case(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T, case: str):
            self.text = text
            self.case = case

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

    class mod(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class round(ThirdBlock):

        def __init__(self, num: INPUT_COMPATIBLE_T):
            self.num = num

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

    class mathop(ThirdBlock):

        def __init__(self, num: INPUT_COMPATIBLE_T, operation: str):
            self.num = num
            self.operation = operation

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

    class stringify(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

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

    class boolify(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

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

    class expandable_math(ThirdBlock):

        def __init__(self):
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    class expandable_bool(ThirdBlock):

        def __init__(self):
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    class expandable_compare(ThirdBlock):

        def __init__(self):
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    class expandablejoininputs(ThirdBlock):

        def __init__(self):
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

        def to_second(self) -> p.SRBlock:
            raise NotImplementedError(
                "This opcode is not supported yet, because it requires flexible input counts."
            )

    class nand(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class nor(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class xor(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class xnor(ThirdBlock):

        def __init__(self, operand1: INPUT_COMPATIBLE_T, operand2: INPUT_COMPATIBLE_T):
            self.operand1 = operand1
            self.operand2 = operand2

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

    class random_boolean(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&operator::random", inputs={}, dropdowns={})

    class count_appear_times(ThirdBlock):

        def __init__(self, text1: INPUT_COMPATIBLE_T, text2: INPUT_COMPATIBLE_T):
            self.text1 = text1
            self.text2 = text2

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

    class read_line_in_multiline_text(ThirdBlock):

        def __init__(self, line: INPUT_COMPATIBLE_T, text: INPUT_COMPATIBLE_T):
            self.line = line
            self.text = text

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

    class text_includes_letter_from(ThirdBlock):

        def __init__(self, text1: INPUT_COMPATIBLE_T, text2: INPUT_COMPATIBLE_T):
            self.text1 = text1
            self.text2 = text2

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

    class character_to_code(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T):
            self.one = one

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

    class code_to_character(ThirdBlock):

        def __init__(self, one: INPUT_COMPATIBLE_T):
            self.one = one

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
