from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class gceTestRunner:

    @staticmethod
    def test_scope(name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_(condition: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert <CONDITION>",
            inputs={
                "CONDITION": ThirdInputValue.as_input(
                    condition, p.SRBlockAndBoolInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def assert_not(condition: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert not <CONDITION>",
            inputs={
                "CONDITION": ThirdInputValue.as_input(
                    condition, p.SRBlockAndBoolInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def assert_msg(condition: INPUT_COMPATIBLE_T, msg: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert <CONDITION> message (MSG)",
            inputs={
                "CONDITION": ThirdInputValue.as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "MSG": ThirdInputValue.as_input(msg, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_not_msg(
        condition: INPUT_COMPATIBLE_T, msg: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert not <CONDITION> message (MSG)",
            inputs={
                "CONDITION": ThirdInputValue.as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "MSG": ThirdInputValue.as_input(msg, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_strict_equal(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert typed equality (A) = (B)",
            inputs={
                "A": ThirdInputValue.as_input(a, p.SRBlockAndTextInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_strict_not_equal(
        a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert typed inequality (A) != (B)",
            inputs={
                "A": ThirdInputValue.as_input(a, p.SRBlockAndTextInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_unstrict_equal(
        a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert string equality (A) = (B)",
            inputs={
                "A": ThirdInputValue.as_input(a, p.SRBlockAndTextInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_unstrict_not_equal(
        a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert string inequality (A) != (B)",
            inputs={
                "A": ThirdInputValue.as_input(a, p.SRBlockAndTextInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_text_in_value(
        text: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert text (TEXT) in value (VALUE)",
            inputs={
                "TEXT": ThirdInputValue.as_input(text, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_text_not_in_value(
        text: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert text (TEXT) not in value (VALUE)",
            inputs={
                "TEXT": ThirdInputValue.as_input(text, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_type(
        value: INPUT_COMPATIBLE_T, expected: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert type of (VALUE) is ([EXPECTED])",
            inputs={
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
                "EXPECTED": ThirdInputValue.as_input(
                    expected, p.SRBlockAndDropdownInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_custom_id_type(
        value: INPUT_COMPATIBLE_T, expected: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert custom id of (VALUE) is (EXPECTED)",
            inputs={
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
                "EXPECTED": ThirdInputValue.as_input(
                    expected, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_throws(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert throws error {SUBSTACK}",
            inputs={
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def assert_throws_contains(
        msg: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert throws error containing (MSG) {SUBSTACK}",
            inputs={
                "MSG": ThirdInputValue.as_input(msg, p.SRBlockAndTextInputValue),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_does_not_throw(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert does not throw error {SUBSTACK}",
            inputs={
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def fail_test(msg: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::fail test with message (MSG)",
            inputs={"MSG": ThirdInputValue.as_input(msg, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def menu_expected_type() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::#menu:expectedType", inputs={}, dropdowns={}
        )
