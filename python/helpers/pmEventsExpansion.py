from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmEventsExpansion:

    @grepr_dataclass()
    class every_other_frame(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::every other frame", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class neverr(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::never", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class when_sprite_clicked(ThirdBlock):
        sprite: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::when [SPRITE] clicked",
                inputs={},
                dropdowns={
                    "SPRITE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.sprite
                    )
                },
            )

    @grepr_dataclass()
    class send_with_data(ThirdBlock):
        broadcast: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::broadcast (BROADCAST) with data (DATA)",
                inputs={
                    "BROADCAST": ThirdInputValue.as_input(
                        self.broadcast, p.SRBlockAndTextInputValue
                    ),
                    "DATA": ThirdInputValue.as_input(
                        self.data, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class received_data(ThirdBlock):
        broadcast: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::when I receive [BROADCAST] with data",
                inputs={},
                dropdowns={
                    "BROADCAST": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.broadcast
                    )
                },
            )

    @grepr_dataclass()
    class is_broadcast_received(ThirdBlock):
        broadcast: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::is message (BROADCAST) received?",
                inputs={
                    "BROADCAST": ThirdInputValue.as_input(
                        self.broadcast, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class recieved_data_reporter(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::recieved data", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class broadcast_to_sprite(ThirdBlock):
        broadcast: INPUT_COMPATIBLE_T
        sprite: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::broadcast (BROADCAST) to [SPRITE]",
                inputs={
                    "BROADCAST": ThirdInputValue.as_input(
                        self.broadcast, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "SPRITE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.sprite
                    )
                },
            )

    @grepr_dataclass()
    class broadcast_function(ThirdBlock):
        broadcast: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::broadcast (BROADCAST) and wait",
                inputs={
                    "BROADCAST": ThirdInputValue.as_input(
                        self.broadcast, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class return_from_broadcast_func(ThirdBlock):
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::return (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class broadcast_thread_count(ThirdBlock):
        broadcast: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::broadcast (BROADCAST) and get # of blocks started",
                inputs={
                    "BROADCAST": ThirdInputValue.as_input(
                        self.broadcast, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class broadcast_function_args(ThirdBlock):
        broadcast: INPUT_COMPATIBLE_T
        args: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::broadcast (BROADCAST) with data (ARGS) and wait",
                inputs={
                    "BROADCAST": ThirdInputValue.as_input(
                        self.broadcast, p.SRBlockAndTextInputValue
                    ),
                    "ARGS": ThirdInputValue.as_input(
                        self.args, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class menu_sprite_name(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::#menu:spriteName", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class menu_broadcast_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::#menu:broadcastMenu",
                inputs={},
                dropdowns={},
            )
