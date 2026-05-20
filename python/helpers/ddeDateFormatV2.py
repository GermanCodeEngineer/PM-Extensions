from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class ddeDateFormatV2:

    class current_date(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::current date", inputs={}, dropdowns={}
            )

    class create_date(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T):
            self.string = string

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::new date from (string)",
                inputs={
                    "string": ThirdInputValue.as_input(
                        self.string, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class format_date(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T, format: INPUT_COMPATIBLE_T):
            self.date = date
            self.format = format

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::format (date) as (format)",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                    "format": ThirdInputValue.as_input(
                        self.format, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class locale_format_date(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T):
            self.date = date
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::format (date) as ([type]) locale",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                    "type": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class extra_format_date(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T, type: INPUT_COMPATIBLE_T):
            self.date = date
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::format (date) as ([type])",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                    "type": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class iso_format_date(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T):
            self.date = date

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::format (date) as ISO string",
                inputs={
                    "date": ThirdInputValue.as_input(self.date, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class is_valid(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T):
            self.date = date

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::is (date) valid?",
                inputs={
                    "date": ThirdInputValue.as_input(self.date, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class compare_date(ThirdBlock):

        def __init__(
            self,
            date1: INPUT_COMPATIBLE_T,
            operation: INPUT_COMPATIBLE_T,
            date2: INPUT_COMPATIBLE_T,
        ):
            self.date1 = date1
            self.operation = operation
            self.date2 = date2

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::is (date1) ([operation]) [date2]?",
                inputs={
                    "date1": ThirdInputValue.as_input(
                        self.date1, p.SRBlockOnlyInputValue
                    ),
                    "operation": ThirdInputValue.as_input(
                        self.operation, p.SRBlockAndDropdownInputValue
                    ),
                    "date2": ThirdInputValue.as_input(
                        self.date2, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class check_date_property(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T, property: INPUT_COMPATIBLE_T):
            self.date = date
            self.property = property

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::is (date) [property]?",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                    "property": ThirdInputValue.as_input(
                        self.property, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class diff_date(ThirdBlock):

        def __init__(
            self,
            date1: INPUT_COMPATIBLE_T,
            date2: INPUT_COMPATIBLE_T,
            unit: INPUT_COMPATIBLE_T,
        ):
            self.date1 = date1
            self.date2 = date2
            self.unit = unit

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::get ([unit]) between (date1) and (date2)",
                inputs={
                    "date1": ThirdInputValue.as_input(
                        self.date1, p.SRBlockOnlyInputValue
                    ),
                    "date2": ThirdInputValue.as_input(
                        self.date2, p.SRBlockOnlyInputValue
                    ),
                    "unit": ThirdInputValue.as_input(
                        self.unit, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class get_date_part(ThirdBlock):

        def __init__(self, part: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T):
            self.part = part
            self.date = date

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::get UTC ([part]) of (date)",
                inputs={
                    "part": ThirdInputValue.as_input(
                        self.part, p.SRBlockAndDropdownInputValue
                    ),
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class get_date_part_new(ThirdBlock):

        def __init__(self, part: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T):
            self.part = part
            self.date = date

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::get ([part]) of (date)",
                inputs={
                    "part": ThirdInputValue.as_input(
                        self.part, p.SRBlockAndDropdownInputValue
                    ),
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class set_date_part(ThirdBlock):

        def __init__(
            self,
            part: INPUT_COMPATIBLE_T,
            date: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.part = part
            self.date = date
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::set ([part]) of (date) to (value)",
                inputs={
                    "part": ThirdInputValue.as_input(
                        self.part, p.SRBlockAndDropdownInputValue
                    ),
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                    "value": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class add_time(ThirdBlock):

        def __init__(
            self,
            amount: INPUT_COMPATIBLE_T,
            unit: INPUT_COMPATIBLE_T,
            date: INPUT_COMPATIBLE_T,
        ):
            self.amount = amount
            self.unit = unit
            self.date = date

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::add (amount) ([unit]) to (date)",
                inputs={
                    "amount": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    ),
                    "unit": ThirdInputValue.as_input(
                        self.unit, p.SRBlockAndDropdownInputValue
                    ),
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class round_date(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T, unit: INPUT_COMPATIBLE_T):
            self.date = date
            self.unit = unit

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::round (date) to nearest ([unit])",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockOnlyInputValue
                    ),
                    "unit": ThirdInputValue.as_input(
                        self.unit, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    class menu_compare_operations(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:compareOperations",
                inputs={},
                dropdowns={},
            )

    class menu_date_parts(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:dateParts", inputs={}, dropdowns={}
            )

    class menu_time_units(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:timeUnits", inputs={}, dropdowns={}
            )

    class menu_locale_length(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:localeLength", inputs={}, dropdowns={}
            )

    class menu_date_properties(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:dateProperties", inputs={}, dropdowns={}
            )

    class menu_extra_formats(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:extraFormats", inputs={}, dropdowns={}
            )
