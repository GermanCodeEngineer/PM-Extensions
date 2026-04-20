from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class ddeDateFormat:

    @staticmethod
    def current_date() -> p.SRBlock:
        return p.SRBlock(opcode="&ddeDateFormat::current date", inputs={}, dropdowns={})

    @staticmethod
    def create_date(string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::new date from (string)",
            inputs={
                "string": InputValue.try_as_input(string, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def format_date(date: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::format date (date) as (format)",
            inputs={
                "date": InputValue.try_as_input(date, p.SRBlockAndTextInputValue),
                "format": InputValue.try_as_input(format, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def locale_format_date(
        date: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::format date (date) to ([type]) locale",
            inputs={
                "date": InputValue.try_as_input(date, p.SRBlockAndTextInputValue),
                "type": InputValue.try_as_input(type, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def compare_date(
        date1: INPUT_COMPATIBLE_T,
        operation: INPUT_COMPATIBLE_T,
        date2: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::is date (date1) ([operation]) date [date2]?",
            inputs={
                "date1": InputValue.try_as_input(date1, p.SRBlockAndTextInputValue),
                "operation": InputValue.try_as_input(
                    operation, p.SRBlockAndDropdownInputValue
                ),
                "date2": InputValue.try_as_input(date2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_valid(date: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::is date (date) valid?",
            inputs={"date": InputValue.try_as_input(date, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def get_date_part(part: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::get ([part]) of (date)",
            inputs={
                "part": InputValue.try_as_input(part, p.SRBlockAndDropdownInputValue),
                "date": InputValue.try_as_input(date, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def add_time(
        amount: INPUT_COMPATIBLE_T, unit: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::add (amount) ([unit]) to (date)",
            inputs={
                "amount": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue),
                "unit": InputValue.try_as_input(unit, p.SRBlockAndDropdownInputValue),
                "date": InputValue.try_as_input(date, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def diff_date(
        date1: INPUT_COMPATIBLE_T, date2: INPUT_COMPATIBLE_T, unit: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::difference between (date1) and (date2) in ([unit])",
            inputs={
                "date1": InputValue.try_as_input(date1, p.SRBlockAndTextInputValue),
                "date2": InputValue.try_as_input(date2, p.SRBlockAndTextInputValue),
                "unit": InputValue.try_as_input(unit, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_compare_operations() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::#menu:compareOperations", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_date_parts() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::#menu:dateParts", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_time_units() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::#menu:timeUnits", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_locale_length() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormat::#menu:localeLength", inputs={}, dropdowns={}
        )
