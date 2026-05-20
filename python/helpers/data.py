from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class data:

    class setvariableto(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, variable: str):
            self.value = value
            self.variable = variable

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::set [VARIABLE] to (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    class changevariableby(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, variable: str):
            self.value = value
            self.variable = variable

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::change [VARIABLE] by (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    class showvariable(ThirdBlock):

        def __init__(self, variable: str):
            self.variable = variable

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::show variable [VARIABLE]",
                inputs={},
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    class hidevariable(ThirdBlock):

        def __init__(self, variable: str):
            self.variable = variable

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::hide variable [VARIABLE]",
                inputs={},
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    class variable(ThirdBlock):

        def __init__(self, variable: str):
            self.variable = variable

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::value of [VARIABLE]",
                inputs={},
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    )
                },
            )

    class addtolist(ThirdBlock):

        def __init__(self, item: INPUT_COMPATIBLE_T, list: str):
            self.item = item
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::add (ITEM) to [LIST]",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class deleteoflist(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T, list: str):
            self.index = index
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::delete (INDEX) of [LIST]",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class deletealloflist(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::delete all of [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class shiftlist(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T, list: str):
            self.index = index
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::shift [LIST] by (INDEX)",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class insertatlist(ThirdBlock):

        def __init__(
            self, item: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T, list: str
        ):
            self.item = item
            self.index = index
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::insert (ITEM) at (INDEX) of [LIST]",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    ),
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class replaceitemoflist(ThirdBlock):

        def __init__(
            self, index: INPUT_COMPATIBLE_T, item: INPUT_COMPATIBLE_T, list: str
        ):
            self.index = index
            self.item = item
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::replace item (INDEX) of [LIST] with (ITEM)",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    ),
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class listforeachitem(ThirdBlock):

        def __init__(self, body: INPUT_COMPATIBLE_T, variable: str, list: str):
            self.body = body
            self.variable = variable
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::For each item [VARIABLE] in [LIST] {BODY}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    ),
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list),
                },
            )

    class listforeachnum(ThirdBlock):

        def __init__(self, body: INPUT_COMPATIBLE_T, variable: str, list: str):
            self.body = body
            self.variable = variable
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::For each item # [VARIABLE] in [LIST] {BODY}}",
                inputs={
                    "BODY": ThirdInputValue.as_input(self.body, p.SRScriptInputValue)
                },
                dropdowns={
                    "VARIABLE": p.SRDropdownValue(
                        p.DropdownValueKind.STANDARD, self.variable
                    ),
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list),
                },
            )

    class itemoflist(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T, list: str):
            self.index = index
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::item (INDEX) of [LIST]",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class itemnumoflist(ThirdBlock):

        def __init__(self, item: INPUT_COMPATIBLE_T, list: str):
            self.item = item
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::item # of (ITEM) in [LIST]",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class amountinlist(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, list: str):
            self.value = value
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::amount of (VALUE) of [LIST]",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class lengthoflist(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::length of [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class listcontainsitem(ThirdBlock):

        def __init__(self, item: INPUT_COMPATIBLE_T, list: str):
            self.item = item
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::[LIST] contains (ITEM) ?",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class itemexistslist(ThirdBlock):

        def __init__(self, index: INPUT_COMPATIBLE_T, list: str):
            self.index = index
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::item (INDEX) exists in [LIST] ?",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        self.index, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class listisempty(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::is [LIST] empty?",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class reverselist(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::reverse [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class filterlist(ThirdBlock):

        def __init__(self, keep: INPUT_COMPATIBLE_T, list: str):
            self.keep = keep
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::filter [LIST] by (INDEX) (ITEM) <KEEP>",
                inputs={
                    "INDEX": ThirdInputValue.as_input(
                        ThirdInputValue(data.filterlistindex()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "ITEM": ThirdInputValue.as_input(
                        ThirdInputValue(data.filterlistitem()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "KEEP": ThirdInputValue.as_input(
                        self.keep, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class arraylist(ThirdBlock):

        def __init__(self, value: INPUT_COMPATIBLE_T, list: str):
            self.value = value
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::set [LIST] to array (VALUE)",
                inputs={
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class listarray(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::get list [LIST] as an array",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class showlist(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::show list [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class hidelist(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&lists::hide list [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class listcontents(ThirdBlock):

        def __init__(self, list: str):
            self.list = list

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&variables::value of [LIST]",
                inputs={},
                dropdowns={
                    "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.list)
                },
            )

    class filterlistindex(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&lists::{{FILTER INDEX}}", inputs={}, dropdowns={})

    class filterlistitem(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&lists::{{FILTER ITEM}}", inputs={}, dropdowns={})
