from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class event:

    @grepr_dataclass()
    class whenflagclicked(ThirdBlock):
        OPCODE: ClassVar = "&events::when green flag clicked"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class whenstopclicked(ThirdBlock):
        OPCODE: ClassVar = "&events::when stop clicked"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class always(ThirdBlock):
        OPCODE: ClassVar = "&events::always"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class whenanything(ThirdBlock):
        OPCODE: ClassVar = "&events::when <CONDITION>"
        INPUT_SPECS: ClassVar = (
            ("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class whenkeypressed(ThirdBlock):
        OPCODE: ClassVar = "&events::when [KEY] key pressed"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("KEY", "key"),)
        key: str

    @grepr_dataclass()
    class whenkeyhit(ThirdBlock):
        OPCODE: ClassVar = "&events::when [KEY] key hit"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("KEY", "key"),)
        key: str

    @grepr_dataclass()
    class whenmousescrolled(ThirdBlock):
        OPCODE: ClassVar = "&events::when mouse is scrolled [DIRECTION]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("DIRECTION", "direction"),)
        direction: str

    @grepr_dataclass()
    class whenthisspriteclicked(ThirdBlock):
        OPCODE: ClassVar = "&events::when this sprite clicked"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class whenstageclicked(ThirdBlock):
        OPCODE: ClassVar = "&events::when stage clicked"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class whenbackdropswitchesto(ThirdBlock):
        OPCODE: ClassVar = "&events::when backdrop switches to [BACKDROP]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("BACKDROP", "backdrop"),)
        backdrop: str

    @grepr_dataclass()
    class whengreaterthan(ThirdBlock):
        OPCODE: ClassVar = "&events::when [OPTION] > (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("OPTION", "option"),)
        value: INPUT_COMPATIBLE_T
        option: str

    @grepr_dataclass()
    class whenbroadcastreceived(ThirdBlock):
        OPCODE: ClassVar = "&events::when I receive [MESSAGE]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("MESSAGE", "message"),)
        message: str

    @grepr_dataclass()
    class broadcast(ThirdBlock):
        OPCODE: ClassVar = "&events::broadcast ([MESSAGE])"
        INPUT_SPECS: ClassVar = (
            ("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        message: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class broadcastandwait(ThirdBlock):
        OPCODE: ClassVar = "&events::broadcast ([MESSAGE]) and wait"
        INPUT_SPECS: ClassVar = (
            ("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        message: INPUT_COMPATIBLE_T
