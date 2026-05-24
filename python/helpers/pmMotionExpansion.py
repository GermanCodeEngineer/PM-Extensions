from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class pmMotionExpansion:

    @grepr_dataclass()
    class rotation_style(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::rotation style", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class fence(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::manually fence", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class steptowards(ThirdBlock):
        steps: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::move (STEPS) steps towards x: (X) y: (Y)",
                inputs={
                    "STEPS": ThirdInputValue.as_input(
                        self.steps, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class tweentowards(ThirdBlock):
        percent: INPUT_COMPATIBLE_T
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::move [PERCENT]% of the way to x: (X) y: (Y)",
                inputs={
                    "PERCENT": ThirdInputValue.as_input(
                        self.percent, p.SRBlockAndTextInputValue
                    ),
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class touchingxy(ThirdBlock):
        x: INPUT_COMPATIBLE_T
        y: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::touching x: (X) y: [Y]?",
                inputs={
                    "X": ThirdInputValue.as_input(self.x, p.SRBlockAndTextInputValue),
                    "Y": ThirdInputValue.as_input(self.y, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class touchingrect(ThirdBlock):
        x1: INPUT_COMPATIBLE_T
        y1: INPUT_COMPATIBLE_T
        x2: INPUT_COMPATIBLE_T
        y2: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::touching rectangle x1: (X1) y1: (Y1) x2: (X2) y2: [Y2]?",
                inputs={
                    "X1": ThirdInputValue.as_input(self.x1, p.SRBlockAndTextInputValue),
                    "Y1": ThirdInputValue.as_input(self.y1, p.SRBlockAndTextInputValue),
                    "X2": ThirdInputValue.as_input(self.x2, p.SRBlockAndTextInputValue),
                    "Y2": ThirdInputValue.as_input(self.y2, p.SRBlockAndTextInputValue),
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class set_home(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::set my home", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class goto_home(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&pmMotionExpansion::go to home", inputs={}, dropdowns={}
            )
