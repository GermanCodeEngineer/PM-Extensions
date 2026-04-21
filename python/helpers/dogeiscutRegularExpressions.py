from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class dogeiscutRegularExpressions:

    @staticmethod
    def regex(pattern: INPUT_COMPATIBLE_T, flags: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)",
            inputs={
                "PATTERN": InputValue.try_as_input(pattern, p.SRBlockAndTextInputValue),
                "FLAGS": InputValue.try_as_input(flags, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def escape(string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::escape (STRING) for regex",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def source_of(regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::source of (REGEX)",
            inputs={"REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def flags_of(regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::flags of (REGEX)",
            inputs={"REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def test(string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::test (STRING) for (REGEX)",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def search(string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::search (STRING) with (REGEX)",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def replace(
        regex: INPUT_COMPATIBLE_T, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::replace (REGEX) in (A) with (B)",
            inputs={
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def replace_all(
        regex: INPUT_COMPATIBLE_T, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::replace all (REGEX) in (A) with (B)",
            inputs={
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
                "A": InputValue.try_as_input(a, p.SRBlockAndTextInputValue),
                "B": InputValue.try_as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def split(string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::split (STRING) by (REGEX)",
            inputs={
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def match(regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::match (REGEX) with (STRING)",
            inputs={
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def match_all(regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::match all (REGEX) with (STRING)",
            inputs={
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def exec(regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::execute (REGEX) on (STRING)",
            inputs={
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
                "STRING": InputValue.try_as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_last_index(regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::get last index of (REGEX)",
            inputs={"REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def set_last_index(
        regex: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::set last index of (REGEX) to (INDEX)",
            inputs={
                "REGEX": InputValue.try_as_input(regex, p.SRBlockOnlyInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )
