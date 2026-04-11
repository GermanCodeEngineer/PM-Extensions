from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class sound:

    @staticmethod
    def playuntildone(sound: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::play sound ([SOUND]) until done",
            inputs={
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def play_at_seconds_until_done(
        sound: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::play sound ([SOUND]) starting at (SECONDS) seconds until done",
            inputs={
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue),
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def play(sound: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::start sound ([SOUND])",
            inputs={
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def play_at_seconds(
        sound: INPUT_COMPATIBLE_T, seconds: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::start sound ([SOUND]) at (SECONDS) seconds",
            inputs={
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue),
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def stop(sound: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::stop sound ([SOUND])",
            inputs={
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def playallsounds() -> p.SRBlock:
        return p.SRBlock(opcode="&sound::play all sounds", inputs={}, dropdowns={})

    @staticmethod
    def stopallsounds() -> p.SRBlock:
        return p.SRBlock(opcode="&sound::stop all sounds", inputs={}, dropdowns={})

    @staticmethod
    def set_stop_fadeout_to(
        seconds: INPUT_COMPATIBLE_T, sound: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::set fadeout to (SECONDS) seconds on ([SOUND])",
            inputs={
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_sound_playing(sound: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::is ([SOUND]) playing?",
            inputs={
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def get_length(sound: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::length of ([SOUND])?",
            inputs={
                "SOUND": InputValue.try_as_input(sound, p.SRBlockAndDropdownInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def changeeffectby(amount: INPUT_COMPATIBLE_T, effect: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::change [EFFECT] sound effect by (AMOUNT)",
            inputs={
                "AMOUNT": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "EFFECT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, effect)
            },
        )

    @staticmethod
    def seteffectto(value: INPUT_COMPATIBLE_T, effect: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::set [EFFECT] sound effect to (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "EFFECT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, effect)
            },
        )

    @staticmethod
    def cleareffects() -> p.SRBlock:
        return p.SRBlock(opcode="&sound::clear sound effects", inputs={}, dropdowns={})

    @staticmethod
    def get_effect_value(effect: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sounds::[EFFECT] effect",
            inputs={},
            dropdowns={
                "EFFECT": p.SRDropdownValue(p.DropdownValueKind.STANDARD, effect)
            },
        )

    @staticmethod
    def changevolumeby(amount: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::change volume by (AMOUNT)",
            inputs={
                "AMOUNT": InputValue.try_as_input(amount, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def setvolumeto(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&sound::set volume to (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def volume() -> p.SRBlock:
        return p.SRBlock(opcode="&sound::volume", inputs={}, dropdowns={})

    @staticmethod
    def sounds_menu() -> p.SRBlock:
        return p.SRBlock(opcode="&sound::#SOUND MENU", inputs={}, dropdowns={})
