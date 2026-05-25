from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class event:

    @grepr_dataclass()
    class whenflagclicked(ThirdBlock):
        OPCODE = "&events::when green flag clicked"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class whenstopclicked(ThirdBlock):
        OPCODE = "&events::when stop clicked"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class always(ThirdBlock):
        OPCODE = "&events::always"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class whenanything(ThirdBlock):
        OPCODE = "&events::when <CONDITION>"
        condition: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class whenkeypressed(ThirdBlock):
        OPCODE = "&events::when [KEY] key pressed"
        key: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("KEY", "key"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("KEY", "key"),))

    @grepr_dataclass()
    class whenkeyhit(ThirdBlock):
        OPCODE = "&events::when [KEY] key hit"
        key: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("KEY", "key"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("KEY", "key"),))

    @grepr_dataclass()
    class whenmousescrolled(ThirdBlock):
        OPCODE = "&events::when mouse is scrolled [DIRECTION]"
        direction: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("DIRECTION", "direction"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("DIRECTION", "direction"),))

    @grepr_dataclass()
    class whenthisspriteclicked(ThirdBlock):
        OPCODE = "&events::when this sprite clicked"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class whenstageclicked(ThirdBlock):
        OPCODE = "&events::when stage clicked"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class whenbackdropswitchesto(ThirdBlock):
        OPCODE = "&events::when backdrop switches to [BACKDROP]"
        backdrop: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("BACKDROP", "backdrop"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("BACKDROP", "backdrop"),))

    @grepr_dataclass()
    class whengreaterthan(ThirdBlock):
        OPCODE = "&events::when [OPTION] > (VALUE)"
        value: INPUT_COMPATIBLE_T
        option: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("OPTION", "option"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("OPTION", "option"),),
            )

    @grepr_dataclass()
    class whenbroadcastreceived(ThirdBlock):
        OPCODE = "&events::when I receive [MESSAGE]"
        message: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("MESSAGE", "message"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("MESSAGE", "message"),))

    @grepr_dataclass()
    class broadcast(ThirdBlock):
        OPCODE = "&events::broadcast ([MESSAGE])"
        message: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class broadcastandwait(ThirdBlock):
        OPCODE = "&events::broadcast ([MESSAGE]) and wait"
        message: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),),
                (),
            )
