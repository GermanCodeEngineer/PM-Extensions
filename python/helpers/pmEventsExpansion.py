from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class pmEventsExpansion:

    @staticmethod
    def every_other_frame() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::every other frame", inputs={}, dropdowns={}
        )

    @staticmethod
    def neverr() -> p.SRBlock:
        return p.SRBlock(opcode="&pmEventsExpansion::never", inputs={}, dropdowns={})

    @staticmethod
    def when_sprite_clicked(sprite: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::when [SPRITE] clicked",
            inputs={},
            dropdowns={
                "SPRITE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, sprite)
            },
        )

    @staticmethod
    def send_with_data(
        broadcast: INPUT_COMPATIBLE_T, data: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::broadcast (BROADCAST) with data (DATA)",
            inputs={
                "BROADCAST": InputValue.try_as_input(
                    broadcast, p.SRBlockAndTextInputValue
                ),
                "DATA": InputValue.try_as_input(data, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def received_data(broadcast: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::when I receive [BROADCAST] with data",
            inputs={},
            dropdowns={
                "BROADCAST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, broadcast)
            },
        )

    @staticmethod
    def is_broadcast_received(broadcast: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::is message (BROADCAST) received?",
            inputs={
                "BROADCAST": InputValue.try_as_input(
                    broadcast, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def recieved_data_reporter() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::recieved data", inputs={}, dropdowns={}
        )

    @staticmethod
    def broadcast_to_sprite(broadcast: INPUT_COMPATIBLE_T, sprite: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::broadcast (BROADCAST) to [SPRITE]",
            inputs={
                "BROADCAST": InputValue.try_as_input(
                    broadcast, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={
                "SPRITE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, sprite)
            },
        )

    @staticmethod
    def broadcast_function(broadcast: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::broadcast (BROADCAST) and wait",
            inputs={
                "BROADCAST": InputValue.try_as_input(
                    broadcast, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def return_from_broadcast_func(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::return (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def broadcast_thread_count(broadcast: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::broadcast (BROADCAST) and get # of blocks started",
            inputs={
                "BROADCAST": InputValue.try_as_input(
                    broadcast, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def broadcast_function_args(
        broadcast: INPUT_COMPATIBLE_T, args: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::broadcast (BROADCAST) with data (ARGS) and wait",
            inputs={
                "BROADCAST": InputValue.try_as_input(
                    broadcast, p.SRBlockAndTextInputValue
                ),
                "ARGS": InputValue.try_as_input(args, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_sprite_name() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::#menu:spriteName", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_broadcast_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmEventsExpansion::#menu:broadcastMenu", inputs={}, dropdowns={}
        )
