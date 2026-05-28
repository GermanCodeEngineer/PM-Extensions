from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class motion:

    @grepr_dataclass()
    class movesteps(ThirdBlock):
        OPCODE: ClassVar = "&motion::move (STEPS) steps"
        INPUT_SPECS: ClassVar = (("STEPS", "steps", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        steps: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class movebacksteps(ThirdBlock):
        OPCODE: ClassVar = "&motion::move back (STEPS) steps"
        INPUT_SPECS: ClassVar = (("STEPS", "steps", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        steps: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class moveupdownsteps(ThirdBlock):
        OPCODE: ClassVar = "&motion::move [DIRECTION] (STEPS) steps"
        INPUT_SPECS: ClassVar = (("STEPS", "steps", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("DIRECTION", "direction"),)
        steps: INPUT_COMPATIBLE_T
        direction: str

    @grepr_dataclass()
    class turnright(ThirdBlock):
        OPCODE: ClassVar = "&motion::turn clockwise (DEGREES) degrees"
        INPUT_SPECS: ClassVar = (
            ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        degrees: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class turnleft(ThirdBlock):
        OPCODE: ClassVar = "&motion::turn counterclockwise (DEGREES) degrees"
        INPUT_SPECS: ClassVar = (
            ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        degrees: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class goto(ThirdBlock):
        OPCODE: ClassVar = "&motion::go to ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gotoxy(ThirdBlock):
        OPCODE: ClassVar = "&motion::go to x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changebyxy(ThirdBlock):
        OPCODE: ClassVar = "&motion::change by x: (DX) y: (DY)"
        INPUT_SPECS: ClassVar = (
            ("DX", "dx", p.SRBlockAndTextInputValue, None),
            ("DY", "dy", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        dx: INPUT_COMPATIBLE_T
        dy: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class glideto(ThirdBlock):
        OPCODE: ClassVar = "&motion::glide (SECONDS) secs to ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        seconds: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class glidesecstoxy(ThirdBlock):
        OPCODE: ClassVar = "&motion::glide (SECONDS) secs to x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        seconds: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointindirection(ThirdBlock):
        OPCODE: ClassVar = "&motion::point in direction (DIRECTION)"
        INPUT_SPECS: ClassVar = (
            ("DIRECTION", "direction", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        direction: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointtowards(ThirdBlock):
        OPCODE: ClassVar = "&motion::point towards ([TARGET])"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointtowardsxy(ThirdBlock):
        OPCODE: ClassVar = "&motion::point towards x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class turnaround(ThirdBlock):
        OPCODE: ClassVar = "&motion::turn around"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class changexby(ThirdBlock):
        OPCODE: ClassVar = "&motion::change x by (DX)"
        INPUT_SPECS: ClassVar = (("DX", "dx", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        dx: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setx(ThirdBlock):
        OPCODE: ClassVar = "&motion::set x to (X)"
        INPUT_SPECS: ClassVar = (("X", "x", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changeyby(ThirdBlock):
        OPCODE: ClassVar = "&motion::change y by (DY)"
        INPUT_SPECS: ClassVar = (("DY", "dy", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        dy: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sety(ThirdBlock):
        OPCODE: ClassVar = "&motion::set y to (Y)"
        INPUT_SPECS: ClassVar = (("Y", "y", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ifonedgebounce(ThirdBlock):
        OPCODE: ClassVar = "&motion::if on edge, bounce"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class ifonspritebounce(ThirdBlock):
        OPCODE: ClassVar = "&motion::if touching ([TARGET]), bounce"
        INPUT_SPECS: ClassVar = (
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setrotationstyle(ThirdBlock):
        OPCODE: ClassVar = "&motion::set rotation style [STYLE]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("STYLE", "style"),)
        style: str

    @grepr_dataclass()
    class move_sprite_to_scene_side(ThirdBlock):
        OPCODE: ClassVar = "&motion::move to stage [ZONE]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("ZONE", "zone"),)
        zone: str

    @grepr_dataclass()
    class xposition(ThirdBlock):
        OPCODE: ClassVar = "&motion::x position"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class yposition(ThirdBlock):
        OPCODE: ClassVar = "&motion::y position"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class direction(ThirdBlock):
        OPCODE: ClassVar = "&motion::direction"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class goto_menu(ThirdBlock):
        OPCODE: ClassVar = "&motion::#REACHABLE TARGET MENU (GO)"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class glideto_menu(ThirdBlock):
        OPCODE: ClassVar = "&motion::#REACHABLE TARGET MENU (GLIDE)"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class pointtowards_menu(ThirdBlock):
        OPCODE: ClassVar = "&motion::#OBSERVABLE TARGET MENU"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class turnrightaroundxy(ThirdBlock):
        OPCODE: ClassVar = "&motion::turn clockwise (DEGREES) around x: (X) y: (Y)"
        INPUT_SPECS: ClassVar = (
            ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class turnleftaroundxy(ThirdBlock):
        OPCODE: ClassVar = (
            "&motion::turn counterclockwise (DEGREES) around x: (X) y: (Y)"
        )
        INPUT_SPECS: ClassVar = (
            ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ifonxybounce(ThirdBlock):
        OPCODE: ClassVar = "&motion::if touching x: (X) y: [Y], bounce"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
