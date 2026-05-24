from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class steve0greatnesstimers:

    @grepr_dataclass()
    class getter(ThirdBlock):
        timer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::[TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    @grepr_dataclass()
    class elapsed(ThirdBlock):
        timer: str
        units: str

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

    @grepr_dataclass()
    class pause(ThirdBlock):
        timer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::pause [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    @grepr_dataclass()
    class toggle(ThirdBlock):
        timer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::toggle [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    @grepr_dataclass()
    class unpause(ThirdBlock):
        timer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::start [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    @grepr_dataclass()
    class is_paused(ThirdBlock):
        timer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::is [TIMER] paused?",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    @grepr_dataclass()
    class restart(ThirdBlock):
        timer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::restart [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    @grepr_dataclass()
    class stop(ThirdBlock):
        timer: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::stop [TIMER]",
                inputs={},
                dropdowns={
                    "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.timer)
                },
            )

    @grepr_dataclass()
    class add(ThirdBlock):
        time: INPUT_COMPATIBLE_T
        units: str
        timer: str

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

    @grepr_dataclass()
    class whengt(ThirdBlock):
        time: INPUT_COMPATIBLE_T
        timer: str
        units: str

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

    @grepr_dataclass()
    class menu_timers(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::#menu:TIMERS", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_units_get(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::#menu:UNITS_GET",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_units_set(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&steve0greatnesstimers::#menu:UNITS_SET",
                inputs={},
                dropdowns={},
            )
