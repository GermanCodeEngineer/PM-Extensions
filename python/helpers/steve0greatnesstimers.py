from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class steve0greatnesstimers:

    class getter(ThirdBlock):

        def __init__(self, timer: str):
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::[TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    class elapsed(ThirdBlock):

        def __init__(self, timer: str, units: str):
            self.timer = timer
            self.units = units

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::time elapsed for [TIMER] in [UNITS]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.timer
                    ),
                    "UNITS": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.units
                    ),
                },
            )

    class pause(ThirdBlock):

        def __init__(self, timer: str):
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::pause [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    class toggle(ThirdBlock):

        def __init__(self, timer: str):
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::toggle [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    class unpause(ThirdBlock):

        def __init__(self, timer: str):
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::start [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    class is_paused(ThirdBlock):

        def __init__(self, timer: str):
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::is [TIMER] paused?",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    class restart(ThirdBlock):

        def __init__(self, timer: str):
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::restart [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    class stop(ThirdBlock):

        def __init__(self, timer: str):
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::stop [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    class add(ThirdBlock):

        def __init__(self, time: INPUT_COMPATIBLE_T, units: str, timer: str):
            self.time = time
            self.units = units
            self.timer = timer

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::add (TIME) [UNITS] to [TIMER]",
                inputs={
                    "TIME": ThirdInputValue.as_input(
                        self.time, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "UNITS": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.units
                    ),
                    "TIMER": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.timer
                    ),
                },
            )

    class whengt(ThirdBlock):

        def __init__(self, time: INPUT_COMPATIBLE_T, timer: str, units: str):
            self.time = time
            self.timer = timer
            self.units = units

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::when [TIMER] > (TIME) [UNITS]",
                inputs={
                    "TIME": ThirdInputValue.as_input(
                        self.time, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "TIMER": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.timer
                    ),
                    "UNITS": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.units
                    ),
                },
            )

    class menu_timers(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::#menu:TIMERS", inputs={}, dropdowns={}
            )

    class menu_units_get(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::#menu:UNITS_GET",
                inputs={},
                dropdowns={},
            )

    class menu_units_set(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::#menu:UNITS_SET",
                inputs={},
                dropdowns={},
            )
