from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class ddeDateFormat:

    @grepr_dataclass()
    class current_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::current date"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class create_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::new date from (string)"
        INPUT_SPECS = (("string", "string", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class format_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::format date (date) as (format)"
        INPUT_SPECS = (
            ("date", "date", p.SRBlockAndTextInputValue, None),
            ("format", "format", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class locale_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::format date (date) to ([type]) locale"
        INPUT_SPECS = (
            ("date", "date", p.SRBlockAndTextInputValue, None),
            ("type", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class compare_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::is date (date1) ([operation]) date [date2]?"
        INPUT_SPECS = (
            ("date1", "date1", p.SRBlockAndTextInputValue, None),
            ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
            ("date2", "date2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date1: INPUT_COMPATIBLE_T
        operation: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_valid(ThirdBlock):
        OPCODE = "&ddeDateFormat::is date (date) valid?"
        INPUT_SPECS = (("date", "date", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_date_part(ThirdBlock):
        OPCODE = "&ddeDateFormat::get ([part]) of (date)"
        INPUT_SPECS = (
            ("part", "part", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add_time(ThirdBlock):
        OPCODE = "&ddeDateFormat::add (amount) ([unit]) to (date)"
        INPUT_SPECS = (
            ("amount", "amount", p.SRBlockAndTextInputValue, None),
            ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        amount: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class diff_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::difference between (date1) and (date2) in ([unit])"
        INPUT_SPECS = (
            ("date1", "date1", p.SRBlockAndTextInputValue, None),
            ("date2", "date2", p.SRBlockAndTextInputValue, None),
            ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        date1: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_compare_operations(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:compareOperations"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_date_parts(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:dateParts"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_time_units(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:timeUnits"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_locale_length(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:localeLength"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
