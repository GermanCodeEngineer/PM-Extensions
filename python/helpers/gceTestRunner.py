from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class gceTestRunner:

    @staticmethod
    def describe(name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::describe (NAME) {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def run_test(name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::test (NAME) {SUBSTACK}",
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
    def assert_equal(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert (A) = (B)",
            inputs={
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_throws(
        msg: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert throws (MSG) {SUBSTACK}",
            inputs={
                "MSG": InputValue.try_as_input(msg, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def assert_does_not_throw(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::assert does not throw {SUBSTACK}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def fail(msg: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::fail (MSG)",
            inputs={"MSG": InputValue.try_as_input(msg, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def report_results() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::report results", inputs={}, dropdowns={}
        )

    @staticmethod
    def reset_results() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceTestRunner::reset results", inputs={}, dropdowns={}
        )

    @staticmethod
    def get_passed() -> p.SRBlock:
        return p.SRBlock(opcode="&gceTestRunner::passed", inputs={}, dropdowns={})

    @staticmethod
    def get_failed() -> p.SRBlock:
        return p.SRBlock(opcode="&gceTestRunner::failed", inputs={}, dropdowns={})
