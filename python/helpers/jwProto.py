from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwProto:

    class label_function(ThirdBlock):

        def __init__(self, label: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.label = label
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::// (LABEL) {SUBSTACK}",
                inputs={
                    "LABEL": ThirdInputValue.as_input(
                        self.label, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class label_command(ThirdBlock):

        def __init__(self, label: INPUT_COMPATIBLE_T):
            self.label = label

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::// (LABEL) {{id=jwProto_labelCommand}}",
                inputs={
                    "LABEL": ThirdInputValue.as_input(
                        self.label, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class label_reporter(ThirdBlock):

        def __init__(self, label: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.label = label
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::(VALUE) // (LABEL)",
                inputs={
                    "LABEL": ThirdInputValue.as_input(
                        self.label, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class label_boolean(ThirdBlock):

        def __init__(self, label: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T):
            self.label = label
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::<VALUE> // (LABEL)",
                inputs={
                    "LABEL": ThirdInputValue.as_input(
                        self.label, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class placeholder_reporter(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::... {{id=jwProto_placeholderReporter}}",
                inputs={},
                dropdowns={},
            )

    class placeholder_boolean(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::... {{id=jwProto_placeholderBoolean}}",
                inputs={},
                dropdowns={},
            )

    class label_hat(ThirdBlock):

        def __init__(self, label: INPUT_COMPATIBLE_T):
            self.label = label

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::// (LABEL) {{id=jwProto_labelHat}}",
                inputs={
                    "LABEL": ThirdInputValue.as_input(
                        self.label, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class placeholder_command(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::... {{id=jwProto_placeholderCommand}}",
                inputs={},
                dropdowns={},
            )
