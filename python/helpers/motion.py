from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class motion:

    @grepr_dataclass()
    class movesteps(ThirdBlock):
        steps: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::move (STEPS) steps",
                inputs={
                    "STEPS": ThirdInputValue.as_input(
                        self.steps, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class movebacksteps(ThirdBlock):
        steps: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::move back (STEPS) steps",
                inputs={
                    "STEPS": ThirdInputValue.as_input(
                        self.steps, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class moveupdownsteps(ThirdBlock):
        steps: INPUT_COMPATIBLE_T
        direction: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::move [DIRECTION] (STEPS) steps",
                inputs={
                    "STEPS": ThirdInputValue.as_input(
                        self.steps, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "DIRECTION": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.direction
                    )
                },
            )

    @grepr_dataclass()
    class turnright(ThirdBlock):
        degrees: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::turn clockwise (DEGREES) degrees",
                inputs={
                    "DEGREES": ThirdInputValue.as_input(
                        self.degrees, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class turnleft(ThirdBlock):
        degrees: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::turn counterclockwise (DEGREES) degrees",
                inputs={
                    "DEGREES": ThirdInputValue.as_input(
                        self.degrees, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class goto(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::go to ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class gotoxy(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::go to x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class changebyxy(ThirdBlock):
        dx: INPUT_COMPATIBLE_T
        dy: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::change by x: (DX) y: (DY)",
                inputs={
                    "DX": ThirdInputValue.as_input(self.dx, p.SRBlockAndTextInputValue),
                    "DY": ThirdInputValue.as_input(self.dy, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class glideto(ThirdBlock):
        seconds: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::glide (SECONDS) secs to ([TARGET])",
                inputs={
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    ),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class glidesecstoxy(ThirdBlock):
        seconds: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::glide (SECONDS) secs to x: (X) y: (Y)",
                inputs={
                    "SECONDS": ThirdInputValue.as_input(
                        self.seconds, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class pointindirection(ThirdBlock):
        direction: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::point in direction (DIRECTION)",
                inputs={
                    "DIRECTION": ThirdInputValue.as_input(
                        self.direction, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class pointtowards(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::point towards ([TARGET])",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class pointtowardsxy(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::point towards x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class turnaround(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::turn around", inputs={}, dropdowns={})

    @grepr_dataclass()
    class changexby(ThirdBlock):
        dx: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::change x by (DX)",
                inputs={
                    "DX": ThirdInputValue.as_input(self.dx, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class setx(ThirdBlock):
        x: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::set x to (X)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class changeyby(ThirdBlock):
        dy: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::change y by (DY)",
                inputs={
                    "DY": ThirdInputValue.as_input(self.dy, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class sety(ThirdBlock):
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::set y to (Y)",
                inputs={
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class ifonedgebounce(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::if on edge, bounce", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class ifonspritebounce(ThirdBlock):
        target: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::if touching ([TARGET]), bounce",
                inputs={
                    "TARGET": ThirdInputValue.as_input(
                        self.target, p.SRBlockAndDropdownInputValue
                    )
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class setrotationstyle(ThirdBlock):
        style: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::set rotation style [STYLE]",
                inputs={},
                dropdowns={
                    "STYLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.style)
                },
            )

    @grepr_dataclass()
    class move_sprite_to_scene_side(ThirdBlock):
        zone: str

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::move to stage [ZONE]",
                inputs={},
                dropdowns={
                    "ZONE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.zone)
                },
            )

    @grepr_dataclass()
    class xposition(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::x position", inputs={}, dropdowns={})

    @grepr_dataclass()
    class yposition(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::y position", inputs={}, dropdowns={})

    @grepr_dataclass()
    class direction(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::direction", inputs={}, dropdowns={})

    @grepr_dataclass()
    class goto_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::#REACHABLE TARGET MENU (GO)", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class glideto_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::#REACHABLE TARGET MENU (GLIDE)",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class pointtowards_menu(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::#OBSERVABLE TARGET MENU", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class turnrightaroundxy(ThirdBlock):
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::turn clockwise (DEGREES) around x: (X) y: (Y)",
                inputs={
                    "DEGREES": ThirdInputValue.as_input(
                        self.degrees, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class turnleftaroundxy(ThirdBlock):
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::turn counterclockwise (DEGREES) around x: (X) y: (Y)",
                inputs={
                    "DEGREES": ThirdInputValue.as_input(
                        self.degrees, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class ifonxybounce(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::if touching x: (X) y: [Y], bounce",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )
