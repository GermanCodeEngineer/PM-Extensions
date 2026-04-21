from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class jwProto:

    @staticmethod
    def label_function(
        label: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::// (LABEL) {SUBSTACK}",
            inputs={
                "LABEL": InputValue.try_as_input(label, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def label_command(label: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::// (LABEL) {{id=jwProto_labelCommand}}",
            inputs={
                "LABEL": InputValue.try_as_input(label, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def label_reporter(
        label: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::(VALUE) // (LABEL)",
            inputs={
                "LABEL": InputValue.try_as_input(label, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def label_boolean(
        label: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::<VALUE> // (LABEL)",
            inputs={
                "LABEL": InputValue.try_as_input(label, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def placeholder_reporter() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::... {{id=jwProto_placeholderReporter}}",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def placeholder_boolean() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::... {{id=jwProto_placeholderBoolean}}",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def label_hat(label: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::// (LABEL) {{id=jwProto_labelHat}}",
            inputs={
                "LABEL": InputValue.try_as_input(label, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def placeholder_command() -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::... {{id=jwProto_placeholderCommand}}",
            inputs={},
            dropdowns={},
        )
