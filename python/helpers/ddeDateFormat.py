from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class ddeDateFormat:

    @grepr_dataclass()
    class current_date(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::current date", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class create_date(ThirdBlock):
        string: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class format_date(ThirdBlock):
        date: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class locale_format_date(ThirdBlock):
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class compare_date(ThirdBlock):
        date1: INPUT_COMPATIBLE_T
        operation: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class is_valid(ThirdBlock):
        date: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get_date_part(ThirdBlock):
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class add_time(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class diff_date(ThirdBlock):
        date1: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_compare_operations(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::#menu:compareOperations",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_date_parts(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::#menu:dateParts", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_time_units(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::#menu:timeUnits", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_locale_length(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormat::#menu:localeLength", inputs={}, dropdowns={}
            )
