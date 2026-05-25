from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class pmMotionExpansion:

    @grepr_dataclass()
    class rotation_style(ThirdBlock):
        OPCODE = "&pmMotionExpansion::rotation style"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class fence(ThirdBlock):
        OPCODE = "&pmMotionExpansion::manually fence"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class steptowards(ThirdBlock):
        OPCODE = "&pmMotionExpansion::move (STEPS) steps towards x: (X) y: (Y)"
        INPUT_SPECS = (
            ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        steps: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class tweentowards(ThirdBlock):
        OPCODE = "&pmMotionExpansion::move [PERCENT]% of the way to x: (X) y: (Y)"
        INPUT_SPECS = (
            ("PERCENT", "percent", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        percent: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class touchingxy(ThirdBlock):
        OPCODE = "&pmMotionExpansion::touching x: (X) y: [Y]?"
        INPUT_SPECS = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class touchingrect(ThirdBlock):
        OPCODE = "&pmMotionExpansion::touching rectangle x1: (X1) y1: (Y1) x2: (X2) y2: [Y2]?"
        INPUT_SPECS = (
            ("X1", "x1", p.SRBlockAndTextInputValue, None),
            ("Y1", "y1", p.SRBlockAndTextInputValue, None),
            ("X2", "x2", p.SRBlockAndTextInputValue, None),
            ("Y2", "y2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_home(ThirdBlock):
        OPCODE = "&pmMotionExpansion::set my home"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class goto_home(ThirdBlock):
        OPCODE = "&pmMotionExpansion::go to home"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
