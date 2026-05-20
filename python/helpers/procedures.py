from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class procedures:

    @staticmethod
    def definition() -> p.SRBlock:
        return p.SRBlock(
            opcode="&customblocks::define custom block", inputs={}, dropdowns={}
        )

    @staticmethod
    def definition_return() -> p.SRBlock:
        return p.SRBlock(
            opcode="&customblocks::define custom block reporter",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def prototype() -> p.SRBlock:
        return p.SRBlock(
            opcode="&customblocks::#CUSTOM BLOCK PROTOTYPE", inputs={}, dropdowns={}
        )

    @staticmethod
    def call() -> p.SRBlock:
        raise NotImplementedError(
            "This opcode is not supported yet, because it requires flexible input counts."
        )

    @staticmethod
    def return_(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&customblocks::return (VALUE)",
            inputs={
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def set(param: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&customblocks::set (PARAM) to (VALUE)",
            inputs={
                "PARAM": ThirdInputValue.as_input(param, p.SRBlockOnlyInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )
