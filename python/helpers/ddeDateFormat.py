from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class ddeDateFormat:

    class current_date(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::current date", inputs={}, dropdowns={}
            )

    class create_date(ThirdBlock):

        def __init__(self, string: INPUT_COMPATIBLE_T):
            self.string = string

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::new date from (string)",
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
                opcode="&ddeDateFormat::format date (date) as (format)",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockAndTextInputValue
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
                opcode="&ddeDateFormat::format date (date) to ([type]) locale",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockAndTextInputValue
                    ),
                    "type": ThirdInputValue.as_input(
                        self.type, p.SRBlockAndDropdownInputValue
                    ),
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
                opcode="&ddeDateFormat::is date (date1) ([operation]) date [date2]?",
                inputs={
                    "date1": ThirdInputValue.as_input(
                        self.date1, p.SRBlockAndTextInputValue
                    ),
                    "operation": ThirdInputValue.as_input(
                        self.operation, p.SRBlockAndDropdownInputValue
                    ),
                    "date2": ThirdInputValue.as_input(
                        self.date2, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class is_valid(ThirdBlock):

        def __init__(self, date: INPUT_COMPATIBLE_T):
            self.date = date

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::is date (date) valid?",
                inputs={
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class get_date_part(ThirdBlock):

        def __init__(self, part: INPUT_COMPATIBLE_T, date: INPUT_COMPATIBLE_T):
            self.part = part
            self.date = date

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::get ([part]) of (date)",
                inputs={
                    "part": ThirdInputValue.as_input(
                        self.part, p.SRBlockAndDropdownInputValue
                    ),
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockAndTextInputValue
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
                opcode="&ddeDateFormat::add (amount) ([unit]) to (date)",
                inputs={
                    "amount": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    ),
                    "unit": ThirdInputValue.as_input(
                        self.unit, p.SRBlockAndDropdownInputValue
                    ),
                    "date": ThirdInputValue.as_input(
                        self.date, p.SRBlockAndTextInputValue
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
                opcode="&ddeDateFormat::difference between (date1) and (date2) in ([unit])",
                inputs={
                    "date1": ThirdInputValue.as_input(
                        self.date1, p.SRBlockAndTextInputValue
                    ),
                    "date2": ThirdInputValue.as_input(
                        self.date2, p.SRBlockAndTextInputValue
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
                opcode="&ddeDateFormat::#menu:compareOperations",
                inputs={},
                dropdowns={},
            )

    class menu_date_parts(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::#menu:dateParts", inputs={}, dropdowns={}
            )

    class menu_time_units(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::#menu:timeUnits", inputs={}, dropdowns={}
            )

    class menu_locale_length(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::#menu:localeLength", inputs={}, dropdowns={}
            )
