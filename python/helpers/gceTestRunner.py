from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class gceTestRunner:

    class test_scope(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T):
            self.condition = condition

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert <CONDITION>",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    class assert_not(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T):
            self.condition = condition

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert not <CONDITION>",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    class assert_msg(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T, msg: INPUT_COMPATIBLE_T):
            self.condition = condition
            self.msg = msg

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert <CONDITION> message (MSG)",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_not_msg(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T, msg: INPUT_COMPATIBLE_T):
            self.condition = condition
            self.msg = msg

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert not <CONDITION> message (MSG)",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    ),
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_strict_equal(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert typed equality (A) = (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class assert_strict_not_equal(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert typed inequality (A) != (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class assert_unstrict_equal(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert string equality (A) = (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class assert_unstrict_not_equal(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert string inequality (A) != (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockAndTextInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class assert_text_in_value(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.text = text
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert text (TEXT) in value (VALUE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_text_not_in_value(ThirdBlock):

        def __init__(self, text: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.text = text
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
                inputs={
                    "TEXT": ThirdInputValue.as_input(
                        self.text, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_type(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, expected: INPUT_COMPATIBLE_T):
            self.value = value
            self.expected = expected

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert type of (VALUE) is ([EXPECTED])",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "EXPECTED": ThirdInputValue.as_input(
                        self.expected, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_custom_id_type(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, expected: INPUT_COMPATIBLE_T):
            self.value = value
            self.expected = expected

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert custom id of (VALUE) is (EXPECTED)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                    "EXPECTED": ThirdInputValue.as_input(
                        self.expected, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_throws(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert throws error {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    class assert_throws_contains(ThirdBlock):

        def __init__(self, msg: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.msg = msg
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}",
                inputs={
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class assert_does_not_throw(ThirdBlock):

        def __init__(self, substack: INPUT_COMPATIBLE_T):
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::assert does not throw error {SUBSTACK}",
                inputs={
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    )
                },
                dropdowns={},
            )

    class fail_test(ThirdBlock):

        def __init__(self, msg: INPUT_COMPATIBLE_T):
            self.msg = msg

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::fail test with message (MSG)",
                inputs={
                    "MSG": ThirdInputValue.as_input(
                        self.msg, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class menu_expected_type(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceTestRunner::#menu:expectedType", inputs={}, dropdowns={}
            )
