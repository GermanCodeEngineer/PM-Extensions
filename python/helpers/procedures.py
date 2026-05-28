from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class procedures:

    @grepr_dataclass()
    class definition(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::define custom block"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class definition_return(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::define custom block reporter"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class prototype(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::#CUSTOM BLOCK PROTOTYPE"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class call(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::call custom block"
        INPUT_SPECS: ClassVar = None
        DROPDOWN_SPECS: ClassVar = None

    @grepr_dataclass()
    class return_(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::return (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set(ThirdBlock):
        OPCODE: ClassVar = "&customblocks::set (PARAM) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("PARAM", "param", p.SRBlockOnlyInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        param: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T
