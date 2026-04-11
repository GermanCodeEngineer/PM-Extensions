from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class motion:

    @staticmethod
    def movesteps(steps: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::move (STEPS) steps",
            inputs={
                "STEPS": InputValue.try_as_input(steps, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def movebacksteps(steps: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::move back (STEPS) steps",
            inputs={
                "STEPS": InputValue.try_as_input(steps, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def moveupdownsteps(steps: INPUT_COMPATIBLE_T, direction: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::move [DIRECTION] (STEPS) steps",
            inputs={
                "STEPS": InputValue.try_as_input(steps, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "DIRECTION": p.SRDropdownValue(p.DropdownValueKind.STANDARD, direction)
            },
        )

    @staticmethod
    def turnright(degrees: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::turn clockwise (DEGREES) degrees",
            inputs={
                "DEGREES": InputValue.try_as_input(degrees, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def turnleft(degrees: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::turn counterclockwise (DEGREES) degrees",
            inputs={
                "DEGREES": InputValue.try_as_input(degrees, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def goto(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::go to ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def gotoxy(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::go to x: (X) y: (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def changebyxy(dx: INPUT_COMPATIBLE_T, dy: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::change by x: (DX) y: (DY)",
            inputs={
                "DX": InputValue.try_as_input(dx, p.SRBlockAndTextInputValue),
                "DY": InputValue.try_as_input(dy, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def glideto(seconds: INPUT_COMPATIBLE_T, target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::glide (SECONDS) secs to ([TARGET])",
            inputs={
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def glidesecstoxy(
        seconds: INPUT_COMPATIBLE_T, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::glide (SECONDS) secs to x: (X) y: (Y)",
            inputs={
                "SECONDS": InputValue.try_as_input(seconds, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def pointindirection(direction: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::point in direction (DIRECTION)",
            inputs={
                "DIRECTION": InputValue.try_as_input(
                    direction, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def pointtowards(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::point towards ([TARGET])",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def pointtowardsxy(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::point towards x: (X) y: (Y)",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def turnaround() -> p.SRBlock:
        return p.SRBlock(opcode="&motion::turn around", inputs={}, dropdowns={})

    @staticmethod
    def changexby(dx: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::change x by (DX)",
            inputs={"DX": InputValue.try_as_input(dx, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def setx(x: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::set x to (X)",
            inputs={"X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def changeyby(dy: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::change y by (DY)",
            inputs={"DY": InputValue.try_as_input(dy, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def sety(y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::set y to (Y)",
            inputs={"Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def ifonedgebounce() -> p.SRBlock:
        return p.SRBlock(opcode="&motion::if on edge, bounce", inputs={}, dropdowns={})

    @staticmethod
    def ifonspritebounce(target: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::if touching ([TARGET]), bounce",
            inputs={
                "TARGET": InputValue.try_as_input(
                    target, p.SRBlockAndDropdownInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def setrotationstyle(style: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::set rotation style [STYLE]",
            inputs={},
            dropdowns={"STYLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, style)},
        )

    @staticmethod
    def move_sprite_to_scene_side(zone: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::move to stage [ZONE]",
            inputs={},
            dropdowns={"ZONE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, zone)},
        )

    @staticmethod
    def xposition() -> p.SRBlock:
        return p.SRBlock(opcode="&motion::x position", inputs={}, dropdowns={})

    @staticmethod
    def yposition() -> p.SRBlock:
        return p.SRBlock(opcode="&motion::y position", inputs={}, dropdowns={})

    @staticmethod
    def direction() -> p.SRBlock:
        return p.SRBlock(opcode="&motion::direction", inputs={}, dropdowns={})

    @staticmethod
    def goto_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::#REACHABLE TARGET MENU (GO)", inputs={}, dropdowns={}
        )

    @staticmethod
    def glideto_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::#REACHABLE TARGET MENU (GLIDE)", inputs={}, dropdowns={}
        )

    @staticmethod
    def pointtowards_menu() -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::#OBSERVABLE TARGET MENU", inputs={}, dropdowns={}
        )

    @staticmethod
    def turnrightaroundxy(
        degrees: INPUT_COMPATIBLE_T, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::turn clockwise (DEGREES) around x: (X) y: (Y)",
            inputs={
                "DEGREES": InputValue.try_as_input(degrees, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def turnleftaroundxy(
        degrees: INPUT_COMPATIBLE_T, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::turn counterclockwise (DEGREES) around x: (X) y: (Y)",
            inputs={
                "DEGREES": InputValue.try_as_input(degrees, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def ifonxybounce(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&motion::if touching x: (X) y: [Y], bounce",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )
