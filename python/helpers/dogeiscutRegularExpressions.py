from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class dogeiscutRegularExpressions:

    @staticmethod
    def regex(pattern: INPUT_COMPATIBLE_T, flags: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)",
            inputs={
                "PATTERN": ThirdInputValue.as_input(
                    pattern, p.SRBlockAndTextInputValue
                ),
                "FLAGS": ThirdInputValue.as_input(flags, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def escape(string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::escape (STRING) for regex",
            inputs={
                "STRING": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def source_of(regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::source of (REGEX)",
            inputs={"REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def flags_of(regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::flags of (REGEX)",
            inputs={"REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def test(string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::test (STRING) for (REGEX)",
            inputs={
                "STRING": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue),
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def search(string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::search (STRING) with (REGEX)",
            inputs={
                "STRING": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue),
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
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
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
                "A": ThirdInputValue.as_input(a, p.SRBlockAndTextInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockAndTextInputValue),
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
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
                "A": ThirdInputValue.as_input(a, p.SRBlockAndTextInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def split(string: INPUT_COMPATIBLE_T, regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::split (STRING) by (REGEX)",
            inputs={
                "STRING": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue),
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def match(regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::match (REGEX) with (STRING)",
            inputs={
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
                "STRING": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def match_all(regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::match all (REGEX) with (STRING)",
            inputs={
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
                "STRING": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def exec(regex: INPUT_COMPATIBLE_T, string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::execute (REGEX) on (STRING)",
            inputs={
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
                "STRING": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_last_index(regex: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::get last index of (REGEX)",
            inputs={"REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def set_last_index(
        regex: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&dogeiscutRegularExpressions::set last index of (REGEX) to (INDEX)",
            inputs={
                "REGEX": ThirdInputValue.as_input(regex, p.SRBlockOnlyInputValue),
                "INDEX": ThirdInputValue.as_input(index, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )
