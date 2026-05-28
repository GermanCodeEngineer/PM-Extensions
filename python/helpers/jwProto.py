from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class jwProto:

    @grepr_dataclass()
    class label_function(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::// (LABEL) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        label: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class label_command(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::// (LABEL) {{id=jwProto_labelCommand}}"
        INPUT_SPECS: ClassVar = (("LABEL", "label", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        label: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class label_reporter(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::(VALUE) // (LABEL)"
        INPUT_SPECS: ClassVar = (
            ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class label_boolean(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::<VALUE> // (LABEL)"
        INPUT_SPECS: ClassVar = (
            ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class placeholder_reporter(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::... {{id=jwProto_placeholderReporter}}"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class placeholder_boolean(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::... {{id=jwProto_placeholderBoolean}}"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class label_hat(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::// (LABEL) {{id=jwProto_labelHat}}"
        INPUT_SPECS: ClassVar = (("LABEL", "label", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        label: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class placeholder_command(ThirdBlock):
        OPCODE: ClassVar = "&jwProto::... {{id=jwProto_placeholderCommand}}"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
