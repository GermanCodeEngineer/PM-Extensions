from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class sound:

    @grepr_dataclass()
    class playuntildone(ThirdBlock):
        sound: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::play sound ([SOUND]) until done",
                inputs={
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class play_at_seconds_until_done(ThirdBlock):
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::play sound ([SOUND]) starting at (SECONDS) seconds until done",
                inputs={
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    ),
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class play(ThirdBlock):
        sound: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::start sound ([SOUND])",
                inputs={
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class play_at_seconds(ThirdBlock):
        sound: INPUT_COMPATIBLE_T
        seconds: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::start sound ([SOUND]) at (SECONDS) seconds",
                inputs={
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    ),
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class stop(ThirdBlock):
        sound: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::stop sound ([SOUND])",
                inputs={
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class playallsounds(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::play all sounds", inputs={}, dropdowns={})

    @grepr_dataclass()
    class stopallsounds(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::stop all sounds", inputs={}, dropdowns={})

    @grepr_dataclass()
    class set_stop_fadeout_to(ThirdBlock):
        seconds: INPUT_COMPATIBLE_T
        sound: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::set fadeout to (SECONDS) seconds on ([SOUND])",
                inputs={
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class is_sound_playing(ThirdBlock):
        sound: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::is ([SOUND]) playing?",
                inputs={
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class get_length(ThirdBlock):
        sound: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::length of ([SOUND])?",
                inputs={
                    "SOUND": ThirdInputValue.as_input(
                        self.sound, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class changeeffectby(ThirdBlock):
        amount: INPUT_COMPATIBLE_T
        effect: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::change [EFFECT] sound effect by (AMOUNT)",
                inputs={
                    "AMOUNT": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "EFFECT": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.effect
                    )
                },
            )

    @grepr_dataclass()
    class seteffectto(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        effect: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::set [EFFECT] sound effect to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "EFFECT": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.effect
                    )
                },
            )

    @grepr_dataclass()
    class cleareffects(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::clear sound effects", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class get_effect_value(ThirdBlock):
        effect: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sounds::[EFFECT] effect",
                inputs={},
                dropdowns={
                    "EFFECT": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.effect
                    )
                },
            )

    @grepr_dataclass()
    class changevolumeby(ThirdBlock):
        amount: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::change volume by (AMOUNT)",
                inputs={
                    "AMOUNT": ThirdInputValue.as_input(
                        self.amount, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class setvolumeto(ThirdBlock):
        value: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::set volume to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class volume(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::volume", inputs={}, dropdowns={})

    @grepr_dataclass()
    class sounds_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::#SOUND MENU", inputs={}, dropdowns={})
