from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class sound:

    class playuntildone(ThirdBlock):

        def __init__(self, sound: INPUT_COMPATIBLE_T):
            self.sound = sound

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

    class play_at_seconds_until_done(ThirdBlock):

        def __init__(self, sound: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T):
            self.sound = sound
            self.seconds = seconds

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

    class play(ThirdBlock):

        def __init__(self, sound: INPUT_COMPATIBLE_T):
            self.sound = sound

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

    class play_at_seconds(ThirdBlock):

        def __init__(self, sound: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T):
            self.sound = sound
            self.seconds = seconds

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

    class stop(ThirdBlock):

        def __init__(self, sound: INPUT_COMPATIBLE_T):
            self.sound = sound

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

    class playallsounds(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::play all sounds", inputs={}, dropdowns={})

    class stopallsounds(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::stop all sounds", inputs={}, dropdowns={})

    class set_stop_fadeout_to(ThirdBlock):

        def __init__(self, seconds: INPUT_COMPATIBLE_T, sound: INPUT_COMPATIBLE_T):
            self.seconds = seconds
            self.sound = sound

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

    class is_sound_playing(ThirdBlock):

        def __init__(self, sound: INPUT_COMPATIBLE_T):
            self.sound = sound

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

    class get_length(ThirdBlock):

        def __init__(self, sound: INPUT_COMPATIBLE_T):
            self.sound = sound

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

    class changeeffectby(ThirdBlock):

        def __init__(self, amount: INPUT_COMPATIBLE_T, effect: str):
            self.amount = amount
            self.effect = effect

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

    class seteffectto(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, effect: str):
            self.value = value
            self.effect = effect

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

    class cleareffects(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&sound::clear sound effects", inputs={}, dropdowns={}
            )

    class get_effect_value(ThirdBlock):

        def __init__(self, effect: str):
            self.effect = effect

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

    class changevolumeby(ThirdBlock):

        def __init__(self, amount: INPUT_COMPATIBLE_T):
            self.amount = amount

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

    class setvolumeto(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T):
            self.value = value

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

    class volume(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::volume", inputs={}, dropdowns={})

    class sounds_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&sound::#SOUND MENU", inputs={}, dropdowns={})
