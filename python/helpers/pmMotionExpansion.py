from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class pmMotionExpansion:

    @grepr_dataclass()
    class rotation_style(ThirdBlock):
        OPCODE: ClassVar = "&pmMotionExpansion::rotation style"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class fence(ThirdBlock):
        OPCODE: ClassVar = "&pmMotionExpansion::manually fence"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class steptowards(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmMotionExpansion::move (STEPS) steps towards x: (X) y: (Y)"
        )
        INPUT_SPECS: ClassVar = (
            ("STEPS", "steps", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        steps: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class tweentowards(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmMotionExpansion::move [PERCENT]% of the way to x: (X) y: (Y)"
        )
        INPUT_SPECS: ClassVar = (
            ("PERCENT", "percent", p.SRBlockAndTextInputValue, None),
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        percent: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class touchingxy(ThirdBlock):
        OPCODE: ClassVar = "&pmMotionExpansion::touching x: (X) y: [Y]?"
        INPUT_SPECS: ClassVar = (
            ("X", "x", p.SRBlockAndTextInputValue, None),
            ("Y", "y", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class touchingrect(ThirdBlock):
        OPCODE: ClassVar = (
            "&pmMotionExpansion::touching rectangle x1: (X1) y1: (Y1) x2: (X2) y2: [Y2]?"
        )
        INPUT_SPECS: ClassVar = (
            ("X1", "x1", p.SRBlockAndTextInputValue, None),
            ("Y1", "y1", p.SRBlockAndTextInputValue, None),
            ("X2", "x2", p.SRBlockAndTextInputValue, None),
            ("Y2", "y2", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_home(ThirdBlock):
        OPCODE: ClassVar = "&pmMotionExpansion::set my home"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class goto_home(ThirdBlock):
        OPCODE: ClassVar = "&pmMotionExpansion::go to home"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
