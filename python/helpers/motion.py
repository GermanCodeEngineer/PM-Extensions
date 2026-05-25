from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class motion:

    @grepr_dataclass()
    class movesteps(ThirdBlock):
        OPCODE = "&motion::move (STEPS) steps"
        INPUT_SPECS = (("STEPS", "steps", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        steps: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class movebacksteps(ThirdBlock):
        OPCODE = "&motion::move back (STEPS) steps"
        INPUT_SPECS = (("STEPS", "steps", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        steps: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class moveupdownsteps(ThirdBlock):
        OPCODE = "&motion::move [DIRECTION] (STEPS) steps"
        INPUT_SPECS = (("STEPS", "steps", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("DIRECTION", "direction"),)
        steps: INPUT_COMPATIBLE_T
        direction: str

    @grepr_dataclass()
    class turnright(ThirdBlock):
        OPCODE = "&motion::turn clockwise (DEGREES) degrees"
        INPUT_SPECS = (("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        degrees: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class turnleft(ThirdBlock):
        OPCODE = "&motion::turn counterclockwise (DEGREES) degrees"
        INPUT_SPECS = (("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        degrees: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class goto(ThirdBlock):
        OPCODE = "&motion::go to ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class gotoxy(ThirdBlock):
        OPCODE = "&motion::go to x: (X) y: (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changebyxy(ThirdBlock):
        OPCODE = "&motion::change by x: (DX) y: (DY)"
        INPUT_SPECS = (
            ("DX", "dx", p.SRBlockAndTextInputValue, None),
            ("DY", "dy", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        dx: INPUT_COMPATIBLE_T
        dy: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class glideto(ThirdBlock):
        OPCODE = "&motion::glide (SECONDS) secs to ([TARGET])"
        INPUT_SPECS = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("TARGET", "target", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS = ()
        seconds: INPUT_COMPATIBLE_T
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class glidesecstoxy(ThirdBlock):
        OPCODE = "&motion::glide (SECONDS) secs to x: (X) y: (Y)"
        INPUT_SPECS = (
            ("SECONDS", "seconds", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        seconds: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointindirection(ThirdBlock):
        OPCODE = "&motion::point in direction (DIRECTION)"
        INPUT_SPECS = (("DIRECTION", "direction", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        direction: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointtowards(ThirdBlock):
        OPCODE = "&motion::point towards ([TARGET])"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class pointtowardsxy(ThirdBlock):
        OPCODE = "&motion::point towards x: (X) y: (Y)"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class turnaround(ThirdBlock):
        OPCODE = "&motion::turn around"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class changexby(ThirdBlock):
        OPCODE = "&motion::change x by (DX)"
        INPUT_SPECS = (("DX", "dx", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        dx: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setx(ThirdBlock):
        OPCODE = "&motion::set x to (X)"
        INPUT_SPECS = (("X", "x", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class changeyby(ThirdBlock):
        OPCODE = "&motion::change y by (DY)"
        INPUT_SPECS = (("DY", "dy", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        dy: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class sety(ThirdBlock):
        OPCODE = "&motion::set y to (Y)"
        INPUT_SPECS = (("Y", "y", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ifonedgebounce(ThirdBlock):
        OPCODE = "&motion::if on edge, bounce"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class ifonspritebounce(ThirdBlock):
        OPCODE = "&motion::if touching ([TARGET]), bounce"
        INPUT_SPECS = (("TARGET", "target", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        target: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class setrotationstyle(ThirdBlock):
        OPCODE = "&motion::set rotation style [STYLE]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("STYLE", "style"),)
        style: str

    @grepr_dataclass()
    class move_sprite_to_scene_side(ThirdBlock):
        OPCODE = "&motion::move to stage [ZONE]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("ZONE", "zone"),)
        zone: str

    @grepr_dataclass()
    class xposition(ThirdBlock):
        OPCODE = "&motion::x position"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class yposition(ThirdBlock):
        OPCODE = "&motion::y position"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class direction(ThirdBlock):
        OPCODE = "&motion::direction"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class goto_menu(ThirdBlock):
        OPCODE = "&motion::#REACHABLE TARGET MENU (GO)"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class glideto_menu(ThirdBlock):
        OPCODE = "&motion::#REACHABLE TARGET MENU (GLIDE)"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class pointtowards_menu(ThirdBlock):
        OPCODE = "&motion::#OBSERVABLE TARGET MENU"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class turnrightaroundxy(ThirdBlock):
        OPCODE = "&motion::turn clockwise (DEGREES) around x: (X) y: (Y)"
        INPUT_SPECS = (
            ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class turnleftaroundxy(ThirdBlock):
        OPCODE = "&motion::turn counterclockwise (DEGREES) around x: (X) y: (Y)"
        INPUT_SPECS = (
            ("DEGREES", "degrees", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        degrees: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class ifonxybounce(ThirdBlock):
        OPCODE = "&motion::if touching x: (X) y: [Y], bounce"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T
