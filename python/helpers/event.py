from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class event:

    @grepr_dataclass()
    class whenflagclicked(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when green flag clicked", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class whenstopclicked(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when stop clicked", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class always(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&events::always", inputs={}, dropdowns={})

    @grepr_dataclass()
    class whenanything(ThirdBlock):
        condition: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class whenkeypressed(ThirdBlock):
        key: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when [KEY] key pressed",
                inputs={},
                dropdowns={
                    "KEY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.key)
                },
            )

    @grepr_dataclass()
    class whenkeyhit(ThirdBlock):
        key: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when [KEY] key hit",
                inputs={},
                dropdowns={
                    "KEY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.key)
                },
            )

    @grepr_dataclass()
    class whenmousescrolled(ThirdBlock):
        direction: str

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

    @grepr_dataclass()
    class whenthisspriteclicked(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when this sprite clicked", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class whenstageclicked(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&events::when stage clicked", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class whenbackdropswitchesto(ThirdBlock):
        backdrop: str

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

    @grepr_dataclass()
    class whengreaterthan(ThirdBlock):
        value: INPUT_COMPATIBLE_T
        option: str

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

    @grepr_dataclass()
    class whenbroadcastreceived(ThirdBlock):
        message: str

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

    @grepr_dataclass()
    class broadcast(ThirdBlock):
        message: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class broadcastandwait(ThirdBlock):
        message: INPUT_COMPATIBLE_T

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
