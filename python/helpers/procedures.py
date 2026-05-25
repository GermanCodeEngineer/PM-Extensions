from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class procedures:

    @grepr_dataclass()
    class definition(ThirdBlock):
        OPCODE = "&customblocks::define custom block"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class definition_return(ThirdBlock):
        OPCODE = "&customblocks::define custom block reporter"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class prototype(ThirdBlock):
        OPCODE = "&customblocks::#CUSTOM BLOCK PROTOTYPE"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class call(ThirdBlock):
        OPCODE = "&customblocks::call custom block"
        INPUT_SPECS = None
        DROPDOWN_SPECS = None

    @grepr_dataclass()
    class return_(ThirdBlock):
        OPCODE = "&customblocks::return (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE = "&customblocks::set (PARAM) to (VALUE)"
        INPUT_SPECS = (
            ("PARAM", "param", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        param: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
