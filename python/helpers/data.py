from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class data:

    @grepr_dataclass()
    class setvariableto(ThirdBlock):
        OPCODE: ClassVar = "&variables::set [VARIABLE] to (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
        value: INPUT_COMPATIBLE_T
        variable: str

    @grepr_dataclass()
    class changevariableby(ThirdBlock):
        OPCODE: ClassVar = "&variables::change [VARIABLE] by (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
        value: INPUT_COMPATIBLE_T
        variable: str

    @grepr_dataclass()
    class showvariable(ThirdBlock):
        OPCODE: ClassVar = "&variables::show variable [VARIABLE]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
        variable: str

    @grepr_dataclass()
    class hidevariable(ThirdBlock):
        OPCODE: ClassVar = "&variables::hide variable [VARIABLE]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
        variable: str

    @grepr_dataclass()
    class variable(ThirdBlock):
        OPCODE: ClassVar = "&variables::value of [VARIABLE]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"),)
        variable: str

    @grepr_dataclass()
    class addtolist(ThirdBlock):
        OPCODE: ClassVar = "&lists::add (ITEM) to [LIST]"
        INPUT_SPECS: ClassVar = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class deleteoflist(ThirdBlock):
        OPCODE: ClassVar = "&lists::delete (INDEX) of [LIST]"
        INPUT_SPECS: ClassVar = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class deletealloflist(ThirdBlock):
        OPCODE: ClassVar = "&lists::delete all of [LIST]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class shiftlist(ThirdBlock):
        OPCODE: ClassVar = "&lists::shift [LIST] by (INDEX)"
        INPUT_SPECS: ClassVar = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class insertatlist(ThirdBlock):
        OPCODE: ClassVar = "&lists::insert (ITEM) at (INDEX) of [LIST]"
        INPUT_SPECS: ClassVar = (
            ("ITEM", "item", p.SRBlockAndTextInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class replaceitemoflist(ThirdBlock):
        OPCODE: ClassVar = "&lists::replace item (INDEX) of [LIST] with (ITEM)"
        INPUT_SPECS: ClassVar = (
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ITEM", "item", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class listforeachitem(ThirdBlock):
        OPCODE: ClassVar = "&lists::For each item [VARIABLE] in [LIST] {BODY}"
        INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"), ("LIST", "list"))
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

    @grepr_dataclass()
    class listforeachnum(ThirdBlock):
        OPCODE: ClassVar = "&lists::For each item # [VARIABLE] in [LIST] {BODY}}"
        INPUT_SPECS: ClassVar = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("VARIABLE", "variable"), ("LIST", "list"))
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

    @grepr_dataclass()
    class itemoflist(ThirdBlock):
        OPCODE: ClassVar = "&lists::item (INDEX) of [LIST]"
        INPUT_SPECS: ClassVar = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class itemnumoflist(ThirdBlock):
        OPCODE: ClassVar = "&lists::item # of (ITEM) in [LIST]"
        INPUT_SPECS: ClassVar = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class amountinlist(ThirdBlock):
        OPCODE: ClassVar = "&lists::amount of (VALUE) of [LIST]"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        value: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class lengthoflist(ThirdBlock):
        OPCODE: ClassVar = "&lists::length of [LIST]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class listcontainsitem(ThirdBlock):
        OPCODE: ClassVar = "&lists::[LIST] contains (ITEM) ?"
        INPUT_SPECS: ClassVar = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class itemexistslist(ThirdBlock):
        OPCODE: ClassVar = "&lists::item (INDEX) exists in [LIST] ?"
        INPUT_SPECS: ClassVar = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class listisempty(ThirdBlock):
        OPCODE: ClassVar = "&lists::is [LIST] empty?"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class reverselist(ThirdBlock):
        OPCODE: ClassVar = "&lists::reverse [LIST]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class filterlist(ThirdBlock):
        OPCODE: ClassVar = "&lists::filter [LIST] by (INDEX) (ITEM) <KEEP>"
        INPUT_SPECS: ClassVar = (
            (
                "INDEX",
                "index",
                p.SREmbeddedBlockInputValue,
                lambda: data.filterlistindex(),
            ),
            (
                "ITEM",
                "item",
                p.SREmbeddedBlockInputValue,
                lambda: data.filterlistitem(),
            ),
            ("KEEP", "keep", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        keep: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class arraylist(ThirdBlock):
        OPCODE: ClassVar = "&lists::set [LIST] to array (VALUE)"
        INPUT_SPECS: ClassVar = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        value: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class listarray(ThirdBlock):
        OPCODE: ClassVar = "&lists::get list [LIST] as an array"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class showlist(ThirdBlock):
        OPCODE: ClassVar = "&lists::show list [LIST]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class hidelist(ThirdBlock):
        OPCODE: ClassVar = "&lists::hide list [LIST]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class listcontents(ThirdBlock):
        OPCODE: ClassVar = "&variables::value of [LIST]"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class filterlistindex(ThirdBlock):
        OPCODE: ClassVar = "&lists::{{FILTER INDEX}}"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class filterlistitem(ThirdBlock):
        OPCODE: ClassVar = "&lists::{{FILTER ITEM}}"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
