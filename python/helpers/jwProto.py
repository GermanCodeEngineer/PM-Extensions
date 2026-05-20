from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class jwProto:

    @staticmethod
    def label_function(
        label: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::// (LABEL) {SUBSTACK}",
            inputs={
                "LABEL": ThirdInputValue.as_input(label, p.SRBlockAndTextInputValue),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def label_command(label: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&jwProto::// (LABEL) {{id=jwProto_labelCommand}}",
            inputs={
                "LABEL": ThirdInputValue.as_input(label, p.SRBlockAndTextInputValue)
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
                "LABEL": ThirdInputValue.as_input(label, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
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
                "LABEL": ThirdInputValue.as_input(label, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndBoolInputValue),
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
                "LABEL": ThirdInputValue.as_input(label, p.SRBlockAndTextInputValue)
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
