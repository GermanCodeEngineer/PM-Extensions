from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwProto:

    @grepr_dataclass()
    class label_function(ThirdBlock):
        label: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class label_command(ThirdBlock):
        label: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class label_reporter(ThirdBlock):
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class label_boolean(ThirdBlock):
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class placeholder_reporter(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::... {{id=jwProto_placeholderReporter}}",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class placeholder_boolean(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::... {{id=jwProto_placeholderBoolean}}",
                inputs={},
                dropdowns={},
            )

    @grepr_dataclass()
    class label_hat(ThirdBlock):
        label: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class placeholder_command(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&jwProto::... {{id=jwProto_placeholderCommand}}",
                inputs={},
                dropdowns={},
            )
