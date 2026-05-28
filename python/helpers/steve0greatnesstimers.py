from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class steve0greatnesstimers:

    @grepr_dataclass()
    class getter(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::[TIMER]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class elapsed(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::time elapsed for [TIMER] in [UNITS]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"), ("UNITS", "units"))
        timer: str
        units: str

    @grepr_dataclass()
    class pause(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::pause [TIMER]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class toggle(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::toggle [TIMER]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class unpause(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::start [TIMER]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class is_paused(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::is [TIMER] paused?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class restart(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::restart [TIMER]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::stop [TIMER]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::add (TIME) [UNITS] to [TIMER]"
        INPUT_SPECS: ClassVar = (("TIME", "time", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("UNITS", "units"), ("TIMER", "timer"))
        time: INPUT_COMPATIBLE_T
        units: str
        timer: str

    @grepr_dataclass()
    class whengt(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::when [TIMER] > (TIME) [UNITS]"
        INPUT_SPECS: ClassVar = (("TIME", "time", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("TIMER", "timer"), ("UNITS", "units"))
        time: INPUT_COMPATIBLE_T
        timer: str
        units: str

    @grepr_dataclass()
    class menu_timers(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::#menu:TIMERS"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_units_get(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::#menu:UNITS_GET"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_units_set(ThirdBlock):
        OPCODE: ClassVar = "&steve0greatnesstimers::#menu:UNITS_SET"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
