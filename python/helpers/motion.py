from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class motion:

    class movesteps(ThirdBlock):

        def __init__(self, steps: INPUT_COMPATIBLE_T):
            self.steps = steps

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

    class movebacksteps(ThirdBlock):

        def __init__(self, steps: INPUT_COMPATIBLE_T):
            self.steps = steps

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

    class moveupdownsteps(ThirdBlock):

        def __init__(self, steps: INPUT_COMPATIBLE_T, direction: str):
            self.steps = steps
            self.direction = direction

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

    class turnright(ThirdBlock):

        def __init__(self, degrees: INPUT_COMPATIBLE_T):
            self.degrees = degrees

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

    class turnleft(ThirdBlock):

        def __init__(self, degrees: INPUT_COMPATIBLE_T):
            self.degrees = degrees

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

    class goto(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class gotoxy(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::go to x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class changebyxy(ThirdBlock):

        def __init__(self, dx: INPUT_COMPATIBLE_T, dy: INPUT_COMPATIBLE_T):
            self.dx = dx
            self.dy = dy

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::change by x: (DX) y: (DY)",
                inputs={
                    "DX": ThirdInputValue.as_input(self.dx, p.SRBlockAndTextInputValue),
                    "DY": ThirdInputValue.as_input(self.dy, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class glideto(ThirdBlock):

        def __init__(self, seconds: INPUT_COMPATIBLE_T, target: INPUT_COMPATIBLE_T):
            self.seconds = seconds
            self.target = target

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

    class glidesecstoxy(ThirdBlock):

        def __init__(
            self,
            seconds: INPUT_COMPATIBLE_T,
            x: INPUT_COMPATIBLE_T,
            y: INPUT_COMPATIBLE_T,
        ):
            self.seconds = seconds
            self.x = x
            self.y = y

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

    class pointindirection(ThirdBlock):

        def __init__(self, direction: INPUT_COMPATIBLE_T):
            self.direction = direction

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

    class pointtowards(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class pointtowardsxy(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::point towards x: (X) y: (Y)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    class turnaround(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::turn around", inputs={}, dropdowns={})

    class changexby(ThirdBlock):

        def __init__(self, dx: INPUT_COMPATIBLE_T):
            self.dx = dx

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::change x by (DX)",
                inputs={
                    "DX": ThirdInputValue.as_input(self.dx, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class setx(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T):
            self.x = x

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::set x to (X)",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class changeyby(ThirdBlock):

        def __init__(self, dy: INPUT_COMPATIBLE_T):
            self.dy = dy

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::change y by (DY)",
                inputs={
                    "DY": ThirdInputValue.as_input(self.dy, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class sety(ThirdBlock):

        def __init__(self, y: INPUT_COMPATIBLE_T):
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::set y to (Y)",
                inputs={
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue)
                },
                dropdowns={},
            )

    class ifonedgebounce(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::if on edge, bounce", inputs={}, dropdowns={}
            )

    class ifonspritebounce(ThirdBlock):

        def __init__(self, target: INPUT_COMPATIBLE_T):
            self.target = target

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

    class setrotationstyle(ThirdBlock):

        def __init__(self, style: str):
            self.style = style

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::set rotation style [STYLE]",
                inputs={},
                dropdowns={
                    "STYLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.style)
                },
            )

    class move_sprite_to_scene_side(ThirdBlock):

        def __init__(self, zone: str):
            self.zone = zone

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::move to stage [ZONE]",
                inputs={},
                dropdowns={
                    "ZONE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.zone)
                },
            )

    class xposition(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::x position", inputs={}, dropdowns={})

    class yposition(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::y position", inputs={}, dropdowns={})

    class direction(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&motion::direction", inputs={}, dropdowns={})

    class goto_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::#REACHABLE TARGET MENU (GO)", inputs={}, dropdowns={}
            )

    class glideto_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::#REACHABLE TARGET MENU (GLIDE)",
                inputs={},
                dropdowns={},
            )

    class pointtowards_menu(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::#OBSERVABLE TARGET MENU", inputs={}, dropdowns={}
            )

    class turnrightaroundxy(ThirdBlock):

        def __init__(
            self,
            degrees: INPUT_COMPATIBLE_T,
            x: INPUT_COMPATIBLE_T,
            y: INPUT_COMPATIBLE_T,
        ):
            self.degrees = degrees
            self.x = x
            self.y = y

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

    class turnleftaroundxy(ThirdBlock):

        def __init__(
            self,
            degrees: INPUT_COMPATIBLE_T,
            x: INPUT_COMPATIBLE_T,
            y: INPUT_COMPATIBLE_T,
        ):
            self.degrees = degrees
            self.x = x
            self.y = y

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

    class ifonxybounce(ThirdBlock):

        def __init__(self, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T):
            self.x = x
            self.y = y

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&motion::if touching x: (X) y: [Y], bounce",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )
