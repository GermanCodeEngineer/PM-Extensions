from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class ddeDateFormatV2:

    @grepr_dataclass()
    class current_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::current date"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class create_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::new date from (string)"
        INPUT_SPECS = (("string", "string", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class format_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::format (date) as (format)"
        INPUT_SPECS = (
            ("date", "date", p.SRBlockOnlyInputValue, None),
            ("format", "format", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class locale_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::format (date) as ([type]) locale"
        INPUT_SPECS = (
            ("date", "date", p.SRBlockOnlyInputValue, None),
            ("type", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class extra_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::format (date) as ([type])"
        INPUT_SPECS = (
            ("date", "date", p.SRBlockOnlyInputValue, None),
            ("type", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iso_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::format (date) as ISO string"
        INPUT_SPECS = (("date", "date", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_valid(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::is (date) valid?"
        INPUT_SPECS = (("date", "date", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class compare_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::is (date1) ([operation]) [date2]?"
        INPUT_SPECS = (
            ("date1", "date1", p.SRBlockOnlyInputValue, None),
            ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
            ("date2", "date2", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date1: INPUT_COMPATIBLE_T
        operation: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class check_date_property(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::is (date) [property]?"
        INPUT_SPECS = (
            ("date", "date", p.SRBlockOnlyInputValue, None),
            ("property", "property", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T
        property: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class diff_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::get ([unit]) between (date1) and (date2)"
        INPUT_SPECS = (
            ("date1", "date1", p.SRBlockOnlyInputValue, None),
            ("date2", "date2", p.SRBlockOnlyInputValue, None),
            ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date1: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_date_part(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::get UTC ([part]) of (date)"
        INPUT_SPECS = (
            ("part", "part", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_date_part_new(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::get ([part]) of (date)"
        INPUT_SPECS = (
            ("part", "part", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_date_part(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::set ([part]) of (date) to (value)"
        INPUT_SPECS = (
            ("part", "part", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockOnlyInputValue, None),
            ("value", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add_time(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::add (amount) ([unit]) to (date)"
        INPUT_SPECS = (
            ("amount", "amount", p.SRBlockAndTextInputValue, None),
            ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        amount: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class round_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::round (date) to nearest ([unit])"
        INPUT_SPECS = (
            ("date", "date", p.SRBlockOnlyInputValue, None),
            ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_compare_operations(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:compareOperations"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_date_parts(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:dateParts"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_time_units(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:timeUnits"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_locale_length(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:localeLength"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_date_properties(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:dateProperties"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_extra_formats(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:extraFormats"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
