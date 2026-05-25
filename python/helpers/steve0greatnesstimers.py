from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class steve0greatnesstimers:

    @grepr_dataclass()
    class getter(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::[TIMER]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class elapsed(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::time elapsed for [TIMER] in [UNITS]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"), ("UNITS", "units"))
        timer: str
        units: str

    @grepr_dataclass()
    class pause(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::pause [TIMER]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class toggle(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::toggle [TIMER]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class unpause(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::start [TIMER]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class is_paused(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::is [TIMER] paused?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class restart(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::restart [TIMER]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::stop [TIMER]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("TIMER", "timer"),)
        timer: str

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::add (TIME) [UNITS] to [TIMER]"
        INPUT_SPECS = (("TIME", "time", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("UNITS", "units"), ("TIMER", "timer"))
        time: INPUT_COMPATIBLE_T
        units: str
        timer: str

    @grepr_dataclass()
    class whengt(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::when [TIMER] > (TIME) [UNITS]"
        INPUT_SPECS = (("TIME", "time", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("TIMER", "timer"), ("UNITS", "units"))
        time: INPUT_COMPATIBLE_T
        timer: str
        units: str

    @grepr_dataclass()
    class menu_timers(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::#menu:TIMERS"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_units_get(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::#menu:UNITS_GET"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_units_set(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::#menu:UNITS_SET"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
