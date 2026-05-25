from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmEventsExpansion:

    @grepr_dataclass()
    class every_other_frame(ThirdBlock):
        OPCODE = "&pmEventsExpansion::every other frame"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class neverr(ThirdBlock):
        OPCODE = "&pmEventsExpansion::never"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class when_sprite_clicked(ThirdBlock):
        OPCODE = "&pmEventsExpansion::when [SPRITE] clicked"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("SPRITE", "sprite"),)
        sprite: str

    @grepr_dataclass()
    class send_with_data(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) with data (DATA)"
        INPUT_SPECS = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            ("DATA", "data", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        broadcast: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class received_data(ThirdBlock):
        OPCODE = "&pmEventsExpansion::when I receive [BROADCAST] with data"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("BROADCAST", "broadcast"),)
        broadcast: str

    @grepr_dataclass()
    class is_broadcast_received(ThirdBlock):
        OPCODE = "&pmEventsExpansion::is message (BROADCAST) received?"
        INPUT_SPECS = (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        broadcast: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class recieved_data_reporter(ThirdBlock):
        OPCODE = "&pmEventsExpansion::recieved data"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class broadcast_to_sprite(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) to [SPRITE]"
        INPUT_SPECS = (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("SPRITE", "sprite"),)
        broadcast: INPUT_COMPATIBLE_T
        sprite: str

    @grepr_dataclass()
    class broadcast_function(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) and wait"
        INPUT_SPECS = (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        broadcast: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class return_from_broadcast_func(ThirdBlock):
        OPCODE = "&pmEventsExpansion::return (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class broadcast_thread_count(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) and get # of blocks started"
        INPUT_SPECS = (("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        broadcast: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class broadcast_function_args(ThirdBlock):
        OPCODE = "&pmEventsExpansion::broadcast (BROADCAST) with data (ARGS) and wait"
        INPUT_SPECS = (
            ("BROADCAST", "broadcast", p.SRBlockAndTextInputValue, None),
            ("ARGS", "args", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        broadcast: INPUT_COMPATIBLE_T
        args: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_sprite_name(ThirdBlock):
        OPCODE = "&pmEventsExpansion::#menu:spriteName"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_broadcast_menu(ThirdBlock):
        OPCODE = "&pmEventsExpansion::#menu:broadcastMenu"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
