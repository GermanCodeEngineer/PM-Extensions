from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class jwProto:

    @grepr_dataclass()
    class label_function(ThirdBlock):
        OPCODE = "&jwProto::// (LABEL) {SUBSTACK}"
        INPUT_SPECS = (
            ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        label: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class label_command(ThirdBlock):
        OPCODE = "&jwProto::// (LABEL) {{id=jwProto_labelCommand}}"
        INPUT_SPECS = (("LABEL", "label", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        label: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class label_reporter(ThirdBlock):
        OPCODE = "&jwProto::(VALUE) // (LABEL)"
        INPUT_SPECS = (
            ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class label_boolean(ThirdBlock):
        OPCODE = "&jwProto::<VALUE> // (LABEL)"
        INPUT_SPECS = (
            ("LABEL", "label", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class placeholder_reporter(ThirdBlock):
        OPCODE = "&jwProto::... {{id=jwProto_placeholderReporter}}"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class placeholder_boolean(ThirdBlock):
        OPCODE = "&jwProto::... {{id=jwProto_placeholderBoolean}}"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class label_hat(ThirdBlock):
        OPCODE = "&jwProto::// (LABEL) {{id=jwProto_labelHat}}"
        INPUT_SPECS = (("LABEL", "label", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        label: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class placeholder_command(ThirdBlock):
        OPCODE = "&jwProto::... {{id=jwProto_placeholderCommand}}"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
