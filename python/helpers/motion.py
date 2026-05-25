from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class motion:

    @grepr_dataclass()
    class movesteps(ThirdBlock):
        OPCODE = "&motion::move (STEPS) steps"
        steps: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STEPS", "steps", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("STEPS", "steps", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class movebacksteps(ThirdBlock):
        OPCODE = "&motion::move back (STEPS) steps"
        steps: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STEPS", "steps", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("STEPS", "steps", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class moveupdownsteps(ThirdBlock):
        OPCODE = "&motion::move [DIRECTION] (STEPS) steps"
        steps: INPUT_COMPATIBLE_T
        direction: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STEPS", "steps", p.SRBlockAndTextInputValue, None),),
                (("DIRECTION", "direction"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("STEPS", "steps", p.SRBlockAndTextInputValue, None),),
                (("DIRECTION", "direction"),),
            )

    @grepr_dataclass()
    class turnright(ThirdBlock):
        OPCODE = "&motion::turn clockwise (DEGREES) degrees"
        degrees: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class turnleft(ThirdBlock):
        OPCODE = "&motion::turn counterclockwise (DEGREES) degrees"
        degrees: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class goto(ThirdBlock):
        OPCODE = "&motion::go to ([TARGET])"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class gotoxy(ThirdBlock):
        OPCODE = "&motion::go to x: (X) y: (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class changebyxy(ThirdBlock):
        OPCODE = "&motion::change by x: (DX) y: (DY)"
        dx: INPUT_COMPATIBLE_T
        dy: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("DX", "dx", p.SRBlockAndTextInputValue, None),
                    ("DY", "dy", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("DX", "dx", p.SRBlockAndTextInputValue, None),
                    ("DY", "dy", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class glideto(ThirdBlock):
        OPCODE = "&motion::glide (SECONDS) secs to ([TARGET])"
        seconds: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class glidesecstoxy(ThirdBlock):
        OPCODE = "&motion::glide (SECONDS) secs to x: (X) y: (Y)"
        seconds: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class pointindirection(ThirdBlock):
        OPCODE = "&motion::point in direction (DIRECTION)"
        direction: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DIRECTION", "direction", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("DIRECTION", "direction", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class pointtowards(ThirdBlock):
        OPCODE = "&motion::point towards ([TARGET])"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class pointtowardsxy(ThirdBlock):
        OPCODE = "&motion::point towards x: (X) y: (Y)"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class turnaround(ThirdBlock):
        OPCODE = "&motion::turn around"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class changexby(ThirdBlock):
        OPCODE = "&motion::change x by (DX)"
        dx: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("DX", "dx", p.SRBlockAndTextInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("DX", "dx", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class setx(ThirdBlock):
        OPCODE = "&motion::set x to (X)"
        x: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("X", "x", p.SRBlockAndTextInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("X", "x", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class changeyby(ThirdBlock):
        OPCODE = "&motion::change y by (DY)"
        dy: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("DY", "dy", p.SRBlockAndTextInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("DY", "dy", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class sety(ThirdBlock):
        OPCODE = "&motion::set y to (Y)"
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block, cls.OPCODE, (("Y", "y", p.SRBlockAndTextInputValue, None),), ()
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("Y", "y", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class ifonedgebounce(ThirdBlock):
        OPCODE = "&motion::if on edge, bounce"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class ifonspritebounce(ThirdBlock):
        OPCODE = "&motion::if touching ([TARGET]), bounce"
        target: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class setrotationstyle(ThirdBlock):
        OPCODE = "&motion::set rotation style [STYLE]"
        style: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("STYLE", "style"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("STYLE", "style"),))

    @grepr_dataclass()
    class move_sprite_to_scene_side(ThirdBlock):
        OPCODE = "&motion::move to stage [ZONE]"
        zone: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), (("ZONE", "zone"),))

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), (("ZONE", "zone"),))

    @grepr_dataclass()
    class xposition(ThirdBlock):
        OPCODE = "&motion::x position"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class yposition(ThirdBlock):
        OPCODE = "&motion::y position"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class direction(ThirdBlock):
        OPCODE = "&motion::direction"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class goto_menu(ThirdBlock):
        OPCODE = "&motion::#REACHABLE TARGET MENU (GO)"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class glideto_menu(ThirdBlock):
        OPCODE = "&motion::#REACHABLE TARGET MENU (GLIDE)"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class pointtowards_menu(ThirdBlock):
        OPCODE = "&motion::#OBSERVABLE TARGET MENU"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class turnrightaroundxy(ThirdBlock):
        OPCODE = "&motion::turn clockwise (DEGREES) around x: (X) y: (Y)"
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class turnleftaroundxy(ThirdBlock):
        OPCODE = "&motion::turn counterclockwise (DEGREES) around x: (X) y: (Y)"
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class ifonxybounce(ThirdBlock):
        OPCODE = "&motion::if touching x: (X) y: [Y], bounce"
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("X", "x", p.SRBlockAndTextInputValue, None),
                    ("Y", "y", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )
