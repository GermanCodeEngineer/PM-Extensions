from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class event:

    class whenflagclicked(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when green flag clicked", inputs={}, dropdowns={}
            )

    class whenstopclicked(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when stop clicked", inputs={}, dropdowns={}
            )

    class always(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&events::always", inputs={}, dropdowns={})

    class whenanything(ThirdBlock):

        def __init__(self, condition: INPUT_COMPATIBLE_T):
            self.condition = condition

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when <CONDITION>",
                inputs={
                    "CONDITION": ThirdInputValue.as_input(
                        self.condition, p.SRBlockAndBoolInputValue
                    )
                },
                dropdowns={},
            )

    class whenkeypressed(ThirdBlock):

        def __init__(self, key: str):
            self.key = key

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when [KEY] key pressed",
                inputs={},
                dropdowns={
                    "KEY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.key)
                },
            )

    class whenkeyhit(ThirdBlock):

        def __init__(self, key: str):
            self.key = key

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when [KEY] key hit",
                inputs={},
                dropdowns={
                    "KEY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.key)
                },
            )

    class whenmousescrolled(ThirdBlock):

        def __init__(self, direction: str):
            self.direction = direction

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when mouse is scrolled [DIRECTION]",
                inputs={},
                dropdowns={
                    "DIRECTION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.direction
                    )
                },
            )

    class whenthisspriteclicked(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when this sprite clicked", inputs={}, dropdowns={}
            )

    class whenstageclicked(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when stage clicked", inputs={}, dropdowns={}
            )

    class whenbackdropswitchesto(ThirdBlock):

        def __init__(self, backdrop: str):
            self.backdrop = backdrop

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when backdrop switches to [BACKDROP]",
                inputs={},
                dropdowns={
                    "BACKDROP": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.backdrop
                    )
                },
            )

    class whengreaterthan(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, option: str):
            self.value = value
            self.option = option

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when [OPTION] > (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "OPTION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.option
                    )
                },
            )

    class whenbroadcastreceived(ThirdBlock):

        def __init__(self, message: str):
            self.message = message

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when I receive [MESSAGE]",
                inputs={},
                dropdowns={
                    "MESSAGE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.message
                    )
                },
            )

    class broadcast(ThirdBlock):

        def __init__(self, message: INPUT_COMPATIBLE_T):
            self.message = message

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::broadcast ([MESSAGE])",
                inputs={
                    "MESSAGE": ThirdInputValue.as_input(
                        self.message, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    class broadcastandwait(ThirdBlock):

        def __init__(self, message: INPUT_COMPATIBLE_T):
            self.message = message

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::broadcast ([MESSAGE]) and wait",
                inputs={
                    "MESSAGE": ThirdInputValue.as_input(
                        self.message, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )
