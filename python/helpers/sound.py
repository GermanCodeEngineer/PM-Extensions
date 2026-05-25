from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class sound:

    @grepr_dataclass()
    class playuntildone(ThirdBlock):
        OPCODE = "&sound::play sound ([SOUND]) until done"
        INPUT_SPECS = (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class play_at_seconds_until_done(ThirdBlock):
        OPCODE = "&sound::play sound ([SOUND]) starting at (SECONDS) seconds until done"
        INPUT_SPECS = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class play(ThirdBlock):
        OPCODE = "&sound::start sound ([SOUND])"
        INPUT_SPECS = (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class play_at_seconds(ThirdBlock):
        OPCODE = "&sound::start sound ([SOUND]) at (SECONDS) seconds"
        INPUT_SPECS = (
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE = "&sound::stop sound ([SOUND])"
        INPUT_SPECS = (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class playallsounds(ThirdBlock):
        OPCODE = "&sound::play all sounds"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class stopallsounds(ThirdBlock):
        OPCODE = "&sound::stop all sounds"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_stop_fadeout_to(ThirdBlock):
        OPCODE = "&sound::set fadeout to (SECONDS) seconds on ([SOUND])"
        INPUT_SPECS = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        seconds: INPUT_COMPATIBLE_T
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_sound_playing(ThirdBlock):
        OPCODE = "&sound::is ([SOUND]) playing?"
        INPUT_SPECS = (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_length(ThirdBlock):
        OPCODE = "&sound::length of ([SOUND])?"
        INPUT_SPECS = (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        sound: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        OPCODE = "&sound::change [EFFECT] sound effect by (AMOUNT)"
        INPUT_SPECS = (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("EFFECT", "effect"),)
        amount: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        OPCODE = "&sound::set [EFFECT] sound effect to (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("EFFECT", "effect"),)
        value: INPUT_COMPATIBLE_T
        effect: str

    @grepr_dataclass()
    class cleareffects(ThirdBlock):
        OPCODE = "&sound::clear sound effects"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        OPCODE = "&sounds::[EFFECT] effect"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("EFFECT", "effect"),)
        effect: str

    @grepr_dataclass()
    class changevolumeby(ThirdBlock):
        OPCODE = "&sound::change volume by (AMOUNT)"
        INPUT_SPECS = (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        amount: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setvolumeto(ThirdBlock):
        OPCODE = "&sound::set volume to (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class volume(ThirdBlock):
        OPCODE = "&sound::volume"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class sounds_menu(ThirdBlock):
        OPCODE = "&sound::#SOUND MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
