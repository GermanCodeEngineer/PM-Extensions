from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class pmEventsExpansion:

    @grepr_dataclass()
    class every_other_frame(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::every other frame"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class neverr(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::never"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class when_sprite_clicked(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::when [SPRITE] clicked"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("SPRITE", "sprite"),)
        sprite: str

    @grepr_dataclass()
    class send_with_data(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::broadcast (BROADCAST) with data (DATA)"
        INPUT_SPECS: ClassVar = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        broadcast: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class received_data(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::when I receive [BROADCAST] with data"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("BROADCAST", "broadcast"),)
        broadcast: str

    @grepr_dataclass()
    class is_broadcast_received(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::is message (BROADCAST) received?"
        INPUT_SPECS: ClassVar = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        broadcast: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class recieved_data_reporter(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::recieved data"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class broadcast_to_sprite(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::broadcast (BROADCAST) to [SPRITE]"
        INPUT_SPECS: ClassVar = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("SPRITE", "sprite"),)
        broadcast: INPUT_COMPATIBLE_T
        sprite: str

    @grepr_dataclass()
    class broadcast_function(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::broadcast (BROADCAST) and wait"
        INPUT_SPECS: ClassVar = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        broadcast: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class return_from_broadcast_func(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::return (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class broadcast_thread_count(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmEventsExpansion::broadcast (BROADCAST) and get # of blocks started"
        )
        INPUT_SPECS: ClassVar = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        broadcast: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class broadcast_function_args(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmEventsExpansion::broadcast (BROADCAST) with data (ARGS) and wait"
        )
        INPUT_SPECS: ClassVar = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            ("ARGS", "args", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        broadcast: INPUT_COMPATIBLE_T
        args: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_sprite_name(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::#menu:spriteName"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_broadcast_menu(ThirdBlock):
        OPCODE: ClassVar = "&pmEventsExpansion::#menu:broadcastMenu"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
