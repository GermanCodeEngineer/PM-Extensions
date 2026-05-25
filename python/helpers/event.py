from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class event:

    @grepr_dataclass()
    class whenflagclicked(ThirdBlock):
        OPCODE = "&events::when green flag clicked"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class whenstopclicked(ThirdBlock):
        OPCODE = "&events::when stop clicked"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class always(ThirdBlock):
        OPCODE = "&events::always"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class whenanything(ThirdBlock):
        OPCODE = "&events::when <CONDITION>"
        INPUT_SPECS = (("CONDITION", "condition", p.SRBlockAndBoolInputValue, None),)
        DROPDOWN_SPECS = ()
        condition: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class whenkeypressed(ThirdBlock):
        OPCODE = "&events::when [KEY] key pressed"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("KEY", "key"),)
        key: str

    @grepr_dataclass()
    class whenkeyhit(ThirdBlock):
        OPCODE = "&events::when [KEY] key hit"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("KEY", "key"),)
        key: str

    @grepr_dataclass()
    class whenmousescrolled(ThirdBlock):
        OPCODE = "&events::when mouse is scrolled [DIRECTION]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("DIRECTION", "direction"),)
        direction: str

    @grepr_dataclass()
    class whenthisspriteclicked(ThirdBlock):
        OPCODE = "&events::when this sprite clicked"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class whenstageclicked(ThirdBlock):
        OPCODE = "&events::when stage clicked"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class whenbackdropswitchesto(ThirdBlock):
        OPCODE = "&events::when backdrop switches to [BACKDROP]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("BACKDROP", "backdrop"),)
        backdrop: str

    @grepr_dataclass()
    class whengreaterthan(ThirdBlock):
        OPCODE = "&events::when [OPTION] > (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("OPTION", "option"),)
        value: INPUT_COMPATIBLE_T
        option: str

    @grepr_dataclass()
    class whenbroadcastreceived(ThirdBlock):
        OPCODE = "&events::when I receive [MESSAGE]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("MESSAGE", "message"),)
        message: str

    @grepr_dataclass()
    class broadcast(ThirdBlock):
        OPCODE = "&events::broadcast ([MESSAGE])"
        INPUT_SPECS = (("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        message: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class broadcastandwait(ThirdBlock):
        OPCODE = "&events::broadcast ([MESSAGE]) and wait"
        INPUT_SPECS = (("MESSAGE", "message", p.SRBlockAndDropdownInputValue, None),)
        DROPDOWN_SPECS = ()
        message: INPUT_COMPATIBLE_T
