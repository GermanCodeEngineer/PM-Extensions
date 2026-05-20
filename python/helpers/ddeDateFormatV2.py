from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class ddeDateFormatV2:

    @staticmethod
    def current_date() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::current date", inputs={}, dropdowns={}
        )

    @staticmethod
    def create_date(string: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::new date from (string)",
            inputs={
                "string": ThirdInputValue.as_input(string, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def format_date(date: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::format (date) as (format)",
            inputs={
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
                "format": ThirdInputValue.as_input(format, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def locale_format_date(
        date: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::format (date) as ([type]) locale",
            inputs={
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
                "type": ThirdInputValue.as_input(type, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def extra_format_date(
        date: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::format (date) as ([type])",
            inputs={
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
                "type": ThirdInputValue.as_input(type, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iso_format_date(date: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::format (date) as ISO string",
            inputs={"date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def is_valid(date: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::is (date) valid?",
            inputs={"date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def compare_date(
        date1: INPUT_COMPATIBLE_T,
        operation: INPUT_COMPATIBLE_T,
        date2: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::is (date1) ([operation]) [date2]?",
            inputs={
                "date1": ThirdInputValue.as_input(date1, p.SRBlockOnlyInputValue),
                "operation": ThirdInputValue.as_input(
                    operation, p.SRBlockAndDropdownInputValue
                ),
                "date2": ThirdInputValue.as_input(date2, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def check_date_property(
        date: INPUT_COMPATIBLE_T, property: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::is (date) [property]?",
            inputs={
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
                "property": ThirdInputValue.as_input(
                    property, p.SRBlockAndDropdownInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def diff_date(
        date1: INPUT_COMPATIBLE_T, date2: INPUT_COMPATIBLE_T, unit: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::get ([unit]) between (date1) and (date2)",
            inputs={
                "date1": ThirdInputValue.as_input(date1, p.SRBlockOnlyInputValue),
                "date2": ThirdInputValue.as_input(date2, p.SRBlockOnlyInputValue),
                "unit": ThirdInputValue.as_input(unit, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_date_part(part: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::get UTC ([part]) of (date)",
            inputs={
                "part": ThirdInputValue.as_input(part, p.SRBlockAndDropdownInputValue),
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_date_part_new(
        part: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::get ([part]) of (date)",
            inputs={
                "part": ThirdInputValue.as_input(part, p.SRBlockAndDropdownInputValue),
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_date_part(
        part: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::set ([part]) of (date) to (value)",
            inputs={
                "part": ThirdInputValue.as_input(part, p.SRBlockAndDropdownInputValue),
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
                "value": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def add_time(
        amount: INPUT_COMPATIBLE_T, unit: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::add (amount) ([unit]) to (date)",
            inputs={
                "amount": ThirdInputValue.as_input(amount, p.SRBlockAndTextInputValue),
                "unit": ThirdInputValue.as_input(unit, p.SRBlockAndDropdownInputValue),
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def round_date(date: INPUT_COMPATIBLE_T, unit: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::round (date) to nearest ([unit])",
            inputs={
                "date": ThirdInputValue.as_input(date, p.SRBlockOnlyInputValue),
                "unit": ThirdInputValue.as_input(unit, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_compare_operations() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::#menu:compareOperations", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_date_parts() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::#menu:dateParts", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_time_units() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::#menu:timeUnits", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_locale_length() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::#menu:localeLength", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_date_properties() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::#menu:dateProperties", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_extra_formats() -> p.SRBlock:
        return p.SRBlock(
            opcode="&ddeDateFormatV2::#menu:extraFormats", inputs={}, dropdowns={}
        )
