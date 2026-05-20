from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmEventsExpansion:

    class every_other_frame(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::every other frame", inputs={}, dropdowns={}
            )

    class neverr(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::never", inputs={}, dropdowns={}
            )

    class when_sprite_clicked(ThirdBlock):

        def __init__(self, sprite: str):
            self.sprite = sprite

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

    class send_with_data(ThirdBlock):

        def __init__(self, broadcast: INPUT_COMPATIBLE_T, data: INPUT_COMPATIBLE_T):
            self.broadcast = broadcast
            self.data = data

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

    class received_data(ThirdBlock):

        def __init__(self, broadcast: str):
            self.broadcast = broadcast

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

    class is_broadcast_received(ThirdBlock):

        def __init__(self, broadcast: INPUT_COMPATIBLE_T):
            self.broadcast = broadcast

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

    class recieved_data_reporter(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::recieved data", inputs={}, dropdowns={}
            )

    class broadcast_to_sprite(ThirdBlock):

        def __init__(self, broadcast: INPUT_COMPATIBLE_T, sprite: str):
            self.broadcast = broadcast
            self.sprite = sprite

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

    class broadcast_function(ThirdBlock):

        def __init__(self, broadcast: INPUT_COMPATIBLE_T):
            self.broadcast = broadcast

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

    class return_from_broadcast_func(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

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

    class broadcast_thread_count(ThirdBlock):

        def __init__(self, broadcast: INPUT_COMPATIBLE_T):
            self.broadcast = broadcast

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

    class broadcast_function_args(ThirdBlock):

        def __init__(self, broadcast: INPUT_COMPATIBLE_T, args: INPUT_COMPATIBLE_T):
            self.broadcast = broadcast
            self.args = args

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

    class menu_sprite_name(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::#menu:spriteName", inputs={}, dropdowns={}
            )

    class menu_broadcast_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmEventsExpansion::#menu:broadcastMenu",
                inputs={},
                dropdowns={},
            )
