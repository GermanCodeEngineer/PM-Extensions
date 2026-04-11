from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class pmMotionExpansion:

    @staticmethod
    def rotation_style() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::rotation style", inputs={}, dropdowns={}
        )

    @staticmethod
    def fence() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::manually fence", inputs={}, dropdowns={}
        )

    @staticmethod
    def steptowards(
        steps: INPUT_COMPATIBLE_T, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::move (STEPS) steps towards x: (X) y: (Y)",
            inputs={
                "STEPS": InputValue.try_as_input(steps, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def tweentowards(
        percent: INPUT_COMPATIBLE_T, x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::move [PERCENT]% of the way to x: (X) y: (Y)",
            inputs={
                "PERCENT": InputValue.try_as_input(percent, p.SRBlockAndTextInputValue),
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def touchingxy(x: INPUT_COMPATIBLE_T, y: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::touching x: (X) y: [Y]?",
            inputs={
                "X": InputValue.try_as_input(x, p.SRBlockAndTextInputValue),
                "Y": InputValue.try_as_input(y, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def touchingrect(
        x1: INPUT_COMPATIBLE_T,
        y1: INPUT_COMPATIBLE_T,
        x2: INPUT_COMPATIBLE_T,
        y2: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::touching rectangle x1: (X1) y1: (Y1) x2: (X2) y2: [Y2]?",
            inputs={
                "X1": InputValue.try_as_input(x1, p.SRBlockAndTextInputValue),
                "Y1": InputValue.try_as_input(y1, p.SRBlockAndTextInputValue),
                "X2": InputValue.try_as_input(x2, p.SRBlockAndTextInputValue),
                "Y2": InputValue.try_as_input(y2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def set_home() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::set my home", inputs={}, dropdowns={}
        )

    @staticmethod
    def goto_home() -> p.SRBlock:
        return p.SRBlock(
            opcode="&pmMotionExpansion::go to home", inputs={}, dropdowns={}
        )
