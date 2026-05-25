from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class steve0greatnesstimers:

    @grepr_dataclass()
    class getter(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::[TIMER]"
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("TIMER", "timer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TIMER", "timer"),))

    @grepr_dataclass()
    class elapsed(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::time elapsed for [TIMER] in [UNITS]"
        timer: str
        units: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("TIMER", "timer"), ("UNITS", "units"))
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (), (("TIMER", "timer"), ("UNITS", "units"))
            )

    @grepr_dataclass()
    class pause(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::pause [TIMER]"
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("TIMER", "timer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TIMER", "timer"),))

    @grepr_dataclass()
    class toggle(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::toggle [TIMER]"
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("TIMER", "timer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TIMER", "timer"),))

    @grepr_dataclass()
    class unpause(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::start [TIMER]"
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("TIMER", "timer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TIMER", "timer"),))

    @grepr_dataclass()
    class is_paused(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::is [TIMER] paused?"
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("TIMER", "timer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TIMER", "timer"),))

    @grepr_dataclass()
    class restart(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::restart [TIMER]"
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("TIMER", "timer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TIMER", "timer"),))

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::stop [TIMER]"
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("TIMER", "timer"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("TIMER", "timer"),))

    @grepr_dataclass()
    class add(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::add (TIME) [UNITS] to [TIMER]"
        time: INPUT_COMPATIBLE_T
        units: str
        timer: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TIME", "time", p.SRBlockAndTextInputValue, None),),
                (("UNITS", "units"), ("TIMER", "timer")),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TIME", "time", p.SRBlockAndTextInputValue, None),),
                (("UNITS", "units"), ("TIMER", "timer")),
            )

    @grepr_dataclass()
    class whengt(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::when [TIMER] > (TIME) [UNITS]"
        time: INPUT_COMPATIBLE_T
        timer: str
        units: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TIME", "time", p.SRBlockAndTextInputValue, None),),
                (("TIMER", "timer"), ("UNITS", "units")),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TIME", "time", p.SRBlockAndTextInputValue, None),),
                (("TIMER", "timer"), ("UNITS", "units")),
            )

    @grepr_dataclass()
    class menu_timers(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::#menu:TIMERS"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_units_get(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::#menu:UNITS_GET"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_units_set(ThirdBlock):
        OPCODE = "&steve0greatnesstimers::#menu:UNITS_SET"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
