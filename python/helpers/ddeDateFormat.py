from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class ddeDateFormat:

    @grepr_dataclass()
    class current_date(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::current date"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class create_date(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::new date from (string)"
        INPUT_SPECS: ClassVar = (
            ("string", "string", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        string: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class format_date(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::format date (date) as (format)"
        INPUT_SPECS: ClassVar = (
            ("date", "date", p.SRBlockAndTextInputValue, None),
            ("format", "format", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        date: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class locale_format_date(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::format date (date) to ([type]) locale"
        INPUT_SPECS: ClassVar = (
            ("date", "date", p.SRBlockAndTextInputValue, None),
            ("type", "type", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class compare_date(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::is date (date1) ([operation]) date [date2]?"
        INPUT_SPECS: ClassVar = (
            ("date1", "date1", p.SRBlockAndTextInputValue, None),
            ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
            ("date2", "date2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        date1: INPUT_COMPATIBLE_T
        operation: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_valid(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::is date (date) valid?"
        INPUT_SPECS: ClassVar = (("date", "date", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_date_part(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::get ([part]) of (date)"
        INPUT_SPECS: ClassVar = (
            ("part", "part", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class add_time(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::add (amount) ([unit]) to (date)"
        INPUT_SPECS: ClassVar = (
            ("amount", "amount", p.SRBlockAndTextInputValue, None),
            ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
            ("date", "date", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        amount: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class diff_date(ThirdBlock):
        OPCODE: ClassVar = (
            "&ddeDateFormat::difference between (date1) and (date2) in ([unit])"
        )
        INPUT_SPECS: ClassVar = (
            ("date1", "date1", p.SRBlockAndTextInputValue, None),
            ("date2", "date2", p.SRBlockAndTextInputValue, None),
            ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        date1: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_compare_operations(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::#menu:compareOperations"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_date_parts(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::#menu:dateParts"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_time_units(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::#menu:timeUnits"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_locale_length(ThirdBlock):
        OPCODE: ClassVar = "&ddeDateFormat::#menu:localeLength"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
