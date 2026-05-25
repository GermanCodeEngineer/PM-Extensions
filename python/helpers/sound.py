from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class sound:

    @grepr_dataclass()
    class playuntildone(ThirdBlock):
        OPCODE = "&sound::play sound ([SOUND]) until done"
        sound: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class play_at_seconds_until_done(ThirdBlock):
        OPCODE = "&sound::play sound ([SOUND]) starting at (SECONDS) seconds until done"
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class play(ThirdBlock):
        OPCODE = "&sound::start sound ([SOUND])"
        sound: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class play_at_seconds(ThirdBlock):
        OPCODE = "&sound::start sound ([SOUND]) at (SECONDS) seconds"
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class stop(ThirdBlock):
        OPCODE = "&sound::stop sound ([SOUND])"
        sound: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class playallsounds(ThirdBlock):
        OPCODE = "&sound::play all sounds"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class stopallsounds(ThirdBlock):
        OPCODE = "&sound::stop all sounds"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_stop_fadeout_to(ThirdBlock):
        OPCODE = "&sound::set fadeout to (SECONDS) seconds on ([SOUND])"
        seconds: INPUT_COMPATIBLE_T
        sound: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_sound_playing(ThirdBlock):
        OPCODE = "&sound::is ([SOUND]) playing?"
        sound: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class get_length(ThirdBlock):
        OPCODE = "&sound::length of ([SOUND])?"
        sound: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("SOUND", "sound", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        OPCODE = "&sound::change [EFFECT] sound effect by (AMOUNT)"
        amount: INPUT_COMPATIBLE_T
        effect: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        OPCODE = "&sound::set [EFFECT] sound effect to (VALUE)"
        value: INPUT_COMPATIBLE_T
        effect: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("VALUE", "value", p.SRBlockAndTextInputValue, None),),
                (("EFFECT", "effect"),),
            )

    @grepr_dataclass()
    class cleareffects(ThirdBlock):
        OPCODE = "&sound::clear sound effects"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        OPCODE = "&sounds::[EFFECT] effect"
        effect: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (), (("EFFECT", "effect"),)
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("EFFECT", "effect"),))

    @grepr_dataclass()
    class changevolumeby(ThirdBlock):
        OPCODE = "&sound::change volume by (AMOUNT)"
        amount: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("AMOUNT", "amount", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class setvolumeto(ThirdBlock):
        OPCODE = "&sound::set volume to (VALUE)"
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
    class volume(ThirdBlock):
        OPCODE = "&sound::volume"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class sounds_menu(ThirdBlock):
        OPCODE = "&sound::#SOUND MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
