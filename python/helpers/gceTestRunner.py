from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class gceTestRunner:

    @staticmethod
    def test_scope(name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::test scope named (NAME) {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_(condition: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert <CONDITION>",
            inputs={
                "CONDITION": InputValue.try_as_input(
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
                "CONDITION": InputValue.try_as_input(
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
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "MSG": InputValue.try_as_input(msg, p.SRBlockAndTextInputValue),
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
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                ),
                "MSG": InputValue.try_as_input(msg, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_strict_equal(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert typed equality (A) = (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
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
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
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
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
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
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
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
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
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
                "TEXT": InputValue.try_as_input(text, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_type(value: INPUT_COMPATIBLE_T, expected: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert type of (VALUE) is [EXPECTED]",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "EXPECTED": p.SRDropdownValue(p.DropdownValueKind.STANDARD, expected)
            },
        )

    @staticmethod
    def assert_throws(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert throws error {SUBSTACK}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue)
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
                "MSG": InputValue.try_as_input(msg, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_does_not_throw(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert does not throw error {SUBSTACK}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def fail_test(msg: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::fail test with message (MSG)",
            inputs={"MSG": InputValue.try_as_input(msg, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def menu_expected_type() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::#menu:expectedType", inputs={}, dropdowns={}
        )
