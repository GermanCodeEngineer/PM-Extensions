from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class sound:

    @grepr_dataclass()
    class playuntildone(ThirdBlock):
        OPCODE: ClassVar = "&sound::play sound ([SOUND]) until done"
        INPUT_SPECS: ClassVar = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class play_at_seconds_until_done(ThirdBlock):
        OPCODE: ClassVar = (
            "&sound::play sound ([SOUND]) starting at (SECONDS) seconds until done"
        )
        INPUT_SPECS: ClassVar = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class play(ThirdBlock):
        OPCODE: ClassVar = "&sound::start sound ([SOUND])"
        INPUT_SPECS: ClassVar = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class play_at_seconds(ThirdBlock):
        OPCODE: ClassVar = "&sound::start sound ([SOUND]) at (SECONDS) seconds"
        INPUT_SPECS: ClassVar = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE: ClassVar = "&sound::stop sound ([SOUND])"
        INPUT_SPECS: ClassVar = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class playallsounds(ThirdBlock):
        OPCODE: ClassVar = "&sound::play all sounds"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class stopallsounds(ThirdBlock):
        OPCODE: ClassVar = "&sound::stop all sounds"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_stop_fadeout_to(ThirdBlock):
        OPCODE: ClassVar = "&sound::set fadeout to (SECONDS) seconds on ([SOUND])"
        INPUT_SPECS: ClassVar = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        seconds: INPUT_COMPATIBLE_T
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_sound_playing(ThirdBlock):
        OPCODE: ClassVar = "&sound::is ([SOUND]) playing?"
        INPUT_SPECS: ClassVar = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_length(ThirdBlock):
        OPCODE: ClassVar = "&sound::length of ([SOUND])?"
        INPUT_SPECS: ClassVar = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        OPCODE: ClassVar = "&sound::change [EFFECT] sound effect by (AMOUNT)"
        INPUT_SPECS: ClassVar = (
            ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
        amount: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        OPCODE: ClassVar = "&sound::set [EFFECT] sound effect to (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
        value: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class cleareffects(ThirdBlock):
        OPCODE: ClassVar = "&sound::clear sound effects"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        OPCODE: ClassVar = "&sounds::[EFFECT] effect"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("EFFECT", "effect"),)
        effect: str

    @grepr_dataclass()
    class changevolumeby(ThirdBlock):
        OPCODE: ClassVar = "&sound::change volume by (AMOUNT)"
        INPUT_SPECS: ClassVar = (
            ("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setvolumeto(ThirdBlock):
        OPCODE: ClassVar = "&sound::set volume to (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class volume(ThirdBlock):
        OPCODE: ClassVar = "&sound::volume"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class sounds_menu(ThirdBlock):
        OPCODE: ClassVar = "&sound::#SOUND MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
