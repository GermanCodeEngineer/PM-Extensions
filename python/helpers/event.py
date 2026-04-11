from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class event:

    @staticmethod
    def whenflagclicked() -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when green flag clicked", inputs={}, dropdowns={}
        )

    @staticmethod
    def whenstopclicked() -> p.SRBlock:
        return p.SRBlock(opcode="&events::when stop clicked", inputs={}, dropdowns={})

    @staticmethod
    def always() -> p.SRBlock:
        return p.SRBlock(opcode="&events::always", inputs={}, dropdowns={})

    @staticmethod
    def whenanything(condition: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when <CONDITION>",
            inputs={
                "CONDITION": InputValue.try_as_input(
                    condition, p.SRBlockAndBoolInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def whenkeypressed(key: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when [KEY] key pressed",
            inputs={},
            dropdowns={"KEY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, key)},
        )

    @staticmethod
    def whenkeyhit(key: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when [KEY] key hit",
            inputs={},
            dropdowns={"KEY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, key)},
        )

    @staticmethod
    def whenmousescrolled(direction: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when mouse is scrolled [DIRECTION]",
            inputs={},
            dropdowns={
                "DIRECTION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, direction)
            },
        )

    @staticmethod
    def whenthisspriteclicked() -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when this sprite clicked", inputs={}, dropdowns={}
        )

    @staticmethod
    def whenstageclicked() -> p.SRBlock:
        return p.SRBlock(opcode="&events::when stage clicked", inputs={}, dropdowns={})

    @staticmethod
    def whenbackdropswitchesto(backdrop: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when backdrop switches to [BACKDROP]",
            inputs={},
            dropdowns={
                "BACKDROP": p.SRDropdownValue(p.DropdownValueKind.STANDARD, backdrop)
            },
        )

    @staticmethod
    def whengreaterthan(value: INPUT_COMPATIBLE_T, option: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when [OPTION] > (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "OPTION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, option)
            },
        )

    @staticmethod
    def whenbroadcastreceived(message: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::when I receive [MESSAGE]",
            inputs={},
            dropdowns={
                "MESSAGE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, message)
            },
        )

    @staticmethod
    def broadcast(message: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::broadcast ([MESSAGE])",
            inputs={
                "MESSAGE": InputValue.try_as_input(
                    message, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def broadcastandwait(message: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&events::broadcast ([MESSAGE]) and wait",
            inputs={
                "MESSAGE": InputValue.try_as_input(
                    message, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )
