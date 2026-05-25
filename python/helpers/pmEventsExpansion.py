from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class pmEventsExpansion:

    @grepr_dataclass()
    class every_other_frame(ThirdBlock):
        OPCODE = "&pmEventsExpansion::every other frame"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class neverr(ThirdBlock):
        OPCODE = "&pmEventsExpansion::never"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class when_sprite_clicked(ThirdBlock):
        OPCODE = "&pmEventsExpansion::when [SPRITE] clicked"
        sprite: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("SPRITE", "sprite"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("SPRITE", "sprite"),))

    @grepr_dataclass()
    class send_with_data(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) with data (DATA)"
        broadcast: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class received_data(ThirdBlock):
        OPCODE = "&pmEventsExpansion::when I receive [BROADCAST] with data"
        broadcast: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("BROADCAST", "broadcast"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("BROADCAST", "broadcast"),))

    @grepr_dataclass()
    class is_broadcast_received(ThirdBlock):
        OPCODE = "&pmEventsExpansion::is message (BROADCAST) received?"
        broadcast: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class recieved_data_reporter(ThirdBlock):
        OPCODE = "&pmEventsExpansion::recieved data"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class broadcast_to_sprite(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) to [SPRITE]"
        broadcast: INPUT_COMPATIBLE_T
        sprite: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (("SPRITE", "sprite"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (("SPRITE", "sprite"),),
            )

    @grepr_dataclass()
    class broadcast_function(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) and wait"
        broadcast: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class return_from_broadcast_func(ThirdBlock):
        OPCODE = "&pmEventsExpansion::return (VALUE)"
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VALUE", "value", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class broadcast_thread_count(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) and get # of blocks started"
        broadcast: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class broadcast_function_args(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) with data (ARGS) and wait"
        broadcast: INPUT_COMPATIBLE_T
        args: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
                    ("ARGS", "args", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_sprite_name(ThirdBlock):
        OPCODE = "&pmEventsExpansion::#menu:spriteName"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_broadcast_menu(ThirdBlock):
        OPCODE = "&pmEventsExpansion::#menu:broadcastMenu"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
