from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class steve0greatnesstimers:

    @staticmethod
    def getter(timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::[TIMER]",
            inputs={},
            dropdowns={"TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer)},
        )

    @staticmethod
    def elapsed(timer: str, units: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::time elapsed for [TIMER] in [UNITS]",
            inputs={},
            dropdowns={
                "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer),
                "UNITS": p.SRDropdownValue(p.DropdownValueKind.STANDARD, units),
            },
        )

    @staticmethod
    def pause(timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::pause [TIMER]",
            inputs={},
            dropdowns={"TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer)},
        )

    @staticmethod
    def toggle(timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::toggle [TIMER]",
            inputs={},
            dropdowns={"TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer)},
        )

    @staticmethod
    def unpause(timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::start [TIMER]",
            inputs={},
            dropdowns={"TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer)},
        )

    @staticmethod
    def is_paused(timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::is [TIMER] paused?",
            inputs={},
            dropdowns={"TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer)},
        )

    @staticmethod
    def restart(timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::restart [TIMER]",
            inputs={},
            dropdowns={"TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer)},
        )

    @staticmethod
    def stop(timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::stop [TIMER]",
            inputs={},
            dropdowns={"TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer)},
        )

    @staticmethod
    def add(time: INPUT_COMPATIBLE_T, units: str, timer: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::add (TIME) [UNITS] to [TIMER]",
            inputs={"TIME": InputValue.try_as_input(time, p.SRBlockAndTextInputValue)},
            dropdowns={
                "UNITS": p.SRDropdownValue(p.DropdownValueKind.STANDARD, units),
                "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer),
            },
        )

    @staticmethod
    def whengt(time: INPUT_COMPATIBLE_T, timer: str, units: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::when [TIMER] > (TIME) [UNITS]",
            inputs={"TIME": InputValue.try_as_input(time, p.SRBlockAndTextInputValue)},
            dropdowns={
                "TIMER": p.SRDropdownValue(p.DropdownValueKind.STANDARD, timer),
                "UNITS": p.SRDropdownValue(p.DropdownValueKind.STANDARD, units),
            },
        )

    @staticmethod
    def menu_timers() -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::#menu:TIMERS", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_units_get() -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::#menu:UNITS_GET", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_units_set() -> p.SRBlock:
        return p.SRBlock(
            opcode="&steve0greatnesstimers::#menu:UNITS_SET", inputs={}, dropdowns={}
        )
