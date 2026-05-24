from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class ddeDateFormatV2:

    @grepr_dataclass()
    class current_date(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::current date", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class create_date(ThirdBlock):
        string: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class format_date(ThirdBlock):
        date: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class locale_format_date(ThirdBlock):
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class extra_format_date(ThirdBlock):
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iso_format_date(ThirdBlock):
        date: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::format (date) as ISO string",
                inputs={
                    "date": ThirdInputValue.as_input(self.date, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_valid(ThirdBlock):
        date: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::is (date) valid?",
                inputs={
                    "date": ThirdInputValue.as_input(self.date, p.SRBlockOnlyInputValue)
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

    @grepr_dataclass()
    class check_date_property(ThirdBlock):
        date: INPUT_COMPATIBLE_T
        property: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class diff_date(ThirdBlock):
        date1: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get_date_part(ThirdBlock):
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class get_date_part_new(ThirdBlock):
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class set_date_part(ThirdBlock):
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class add_time(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class round_date(ThirdBlock):
        date: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_compare_operations(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:compareOperations",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_date_parts(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:dateParts", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_time_units(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:timeUnits", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_locale_length(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:localeLength", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_date_properties(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:dateProperties", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_extra_formats(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&ddeDateFormatV2::#menu:extraFormats", inputs={}, dropdowns={}
            )
