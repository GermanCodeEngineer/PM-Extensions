from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class data:

    @grepr_dataclass()
    class setvariableto(ThirdBlock):
        OPCODE = "&variables::set [VARIABLE] to (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("VARIABLE", "variable"),)
        value: INPUT_COMPATIBLE_T
        variable: str

    @grepr_dataclass()
    class changevariableby(ThirdBlock):
        OPCODE = "&variables::change [VARIABLE] by (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("VARIABLE", "variable"),)
        value: INPUT_COMPATIBLE_T
        variable: str

    @grepr_dataclass()
    class showvariable(ThirdBlock):
        OPCODE = "&variables::show variable [VARIABLE]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("VARIABLE", "variable"),)
        variable: str

    @grepr_dataclass()
    class hidevariable(ThirdBlock):
        OPCODE = "&variables::hide variable [VARIABLE]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("VARIABLE", "variable"),)
        variable: str

    @grepr_dataclass()
    class variable(ThirdBlock):
        OPCODE = "&variables::value of [VARIABLE]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("VARIABLE", "variable"),)
        variable: str

    @grepr_dataclass()
    class addtolist(ThirdBlock):
        OPCODE = "&lists::add (ITEM) to [LIST]"
        INPUT_SPECS = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class deleteoflist(ThirdBlock):
        OPCODE = "&lists::delete (INDEX) of [LIST]"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class deletealloflist(ThirdBlock):
        OPCODE = "&lists::delete all of [LIST]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class shiftlist(ThirdBlock):
        OPCODE = "&lists::shift [LIST] by (INDEX)"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class insertatlist(ThirdBlock):
        OPCODE = "&lists::insert (ITEM) at (INDEX) of [LIST]"
        INPUT_SPECS = (
            ("ITEM", "item", p.SRBlockAndTextInputValue, None),
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class replaceitemoflist(ThirdBlock):
        OPCODE = "&lists::replace item (INDEX) of [LIST] with (ITEM)"
        INPUT_SPECS = (
            ("INDEX", "index", p.SRBlockAndTextInputValue, None),
            ("ITEM", "item", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class listforeachitem(ThirdBlock):
        OPCODE = "&lists::For each item [VARIABLE] in [LIST] {BODY}"
        INPUT_SPECS = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = (("VARIABLE", "variable"), ("LIST", "list"))
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

    @grepr_dataclass()
    class listforeachnum(ThirdBlock):
        OPCODE = "&lists::For each item # [VARIABLE] in [LIST] {BODY}}"
        INPUT_SPECS = (("BODY", "body", p.SRScriptInputValue, None),)
        DROPDOWN_SPECS = (("VARIABLE", "variable"), ("LIST", "list"))
        body: INPUT_COMPATIBLE_T
        variable: str
        list: str

    @grepr_dataclass()
    class itemoflist(ThirdBlock):
        OPCODE = "&lists::item (INDEX) of [LIST]"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class itemnumoflist(ThirdBlock):
        OPCODE = "&lists::item # of (ITEM) in [LIST]"
        INPUT_SPECS = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class amountinlist(ThirdBlock):
        OPCODE = "&lists::amount of (VALUE) of [LIST]"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        value: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class lengthoflist(ThirdBlock):
        OPCODE = "&lists::length of [LIST]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class listcontainsitem(ThirdBlock):
        OPCODE = "&lists::[LIST] contains (ITEM) ?"
        INPUT_SPECS = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        item: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class itemexistslist(ThirdBlock):
        OPCODE = "&lists::item (INDEX) exists in [LIST] ?"
        INPUT_SPECS = (("INDEX", "index", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        index: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class listisempty(ThirdBlock):
        OPCODE = "&lists::is [LIST] empty?"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class reverselist(ThirdBlock):
        OPCODE = "&lists::reverse [LIST]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class filterlist(ThirdBlock):
        OPCODE = "&lists::filter [LIST] by (INDEX) (ITEM) <KEEP>"
        INPUT_SPECS = (
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
        DROPDOWN_SPECS = (("LIST", "list"),)
        keep: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class arraylist(ThirdBlock):
        OPCODE = "&lists::set [LIST] to array (VALUE)"
        INPUT_SPECS = (("VALUE", "value", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = (("LIST", "list"),)
        value: INPUT_COMPATIBLE_T
        list: str

    @grepr_dataclass()
    class listarray(ThirdBlock):
        OPCODE = "&lists::get list [LIST] as an array"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class showlist(ThirdBlock):
        OPCODE = "&lists::show list [LIST]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class hidelist(ThirdBlock):
        OPCODE = "&lists::hide list [LIST]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class listcontents(ThirdBlock):
        OPCODE = "&variables::value of [LIST]"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = (("LIST", "list"),)
        list: str

    @grepr_dataclass()
    class filterlistindex(ThirdBlock):
        OPCODE = "&lists::{{FILTER INDEX}}"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class filterlistitem(ThirdBlock):
        OPCODE = "&lists::{{FILTER ITEM}}"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
