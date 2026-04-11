from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class data:

    @staticmethod
    def setvariableto(value: INPUT_COMPATIBLE_T, variable: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&variables::set [VARIABLE] to (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable)
            },
        )

    @staticmethod
    def changevariableby(value: INPUT_COMPATIBLE_T, variable: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&variables::change [VARIABLE] by (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable)
            },
        )

    @staticmethod
    def showvariable(variable: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&variables::show variable [VARIABLE]",
            inputs={},
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable)
            },
        )

    @staticmethod
    def hidevariable(variable: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&variables::hide variable [VARIABLE]",
            inputs={},
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable)
            },
        )

    @staticmethod
    def variable(variable: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&variables::value of [VARIABLE]",
            inputs={},
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable)
            },
        )

    @staticmethod
    def addtolist(item: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::add (ITEM) to [LIST]",
            inputs={"ITEM": InputValue.try_as_input(item, p.SRBlockAndTextInputValue)},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def deleteoflist(index: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::delete (INDEX) of [LIST]",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue)
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def deletealloflist(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::delete all of [LIST]",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def shiftlist(index: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::shift [LIST] by (INDEX)",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue)
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def insertatlist(
        item: INPUT_COMPATIBLE_T, index: INPUT_COMPATIBLE_T, list: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::insert (ITEM) at (INDEX) of [LIST]",
            inputs={
                "ITEM": InputValue.try_as_input(item, p.SRBlockAndTextInputValue),
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def replaceitemoflist(
        index: INPUT_COMPATIBLE_T, item: INPUT_COMPATIBLE_T, list: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::replace item (INDEX) of [LIST] with (ITEM)",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue),
                "ITEM": InputValue.try_as_input(item, p.SRBlockAndTextInputValue),
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def listforeachitem(
        body: INPUT_COMPATIBLE_T, variable: str, list: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::For each item [VARIABLE] in [LIST] {BODY}",
            inputs={"BODY": InputValue.try_as_input(body, p.SRScriptInputValue)},
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable),
                "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list),
            },
        )

    @staticmethod
    def listforeachnum(body: INPUT_COMPATIBLE_T, variable: str, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::For each item # [VARIABLE] in [LIST] {BODY}}",
            inputs={"BODY": InputValue.try_as_input(body, p.SRScriptInputValue)},
            dropdowns={
                "VARIABLE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, variable),
                "LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list),
            },
        )

    @staticmethod
    def itemoflist(index: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::item (INDEX) of [LIST]",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue)
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def itemnumoflist(item: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::item # of (ITEM) in [LIST]",
            inputs={"ITEM": InputValue.try_as_input(item, p.SRBlockAndTextInputValue)},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def amountinlist(value: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::amount of (VALUE) of [LIST]",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def lengthoflist(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::length of [LIST]",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def listcontainsitem(item: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::[LIST] contains (ITEM) ?",
            inputs={"ITEM": InputValue.try_as_input(item, p.SRBlockAndTextInputValue)},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def itemexistslist(index: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::item (INDEX) exists in [LIST] ?",
            inputs={
                "INDEX": InputValue.try_as_input(index, p.SRBlockAndTextInputValue)
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def listisempty(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::is [LIST] empty?",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def reverselist(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::reverse [LIST]",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def filterlist(keep: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::filter [LIST] by (INDEX) (ITEM) <KEEP>",
            inputs={
                "INDEX": InputValue.try_as_input(
                    InputValue(data.filterlistindex()), p.SREmbeddedBlockInputValue
                ),
                "ITEM": InputValue.try_as_input(
                    InputValue(data.filterlistitem()), p.SREmbeddedBlockInputValue
                ),
                "KEEP": InputValue.try_as_input(keep, p.SRBlockAndBoolInputValue),
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def arraylist(value: INPUT_COMPATIBLE_T, list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::set [LIST] to array (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def listarray(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::get list [LIST] as an array",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def showlist(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::show list [LIST]",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def hidelist(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&lists::hide list [LIST]",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def listcontents(list: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&variables::value of [LIST]",
            inputs={},
            dropdowns={"LIST": p.SRDropdownValue(p.DropdownValueKind.STANDARD, list)},
        )

    @staticmethod
    def filterlistindex() -> p.SRBlock:
        return p.SRBlock(opcode="&lists::{{FILTER INDEX}}", inputs={}, dropdowns={})

    @staticmethod
    def filterlistitem() -> p.SRBlock:
        return p.SRBlock(opcode="&lists::{{FILTER ITEM}}", inputs={}, dropdowns={})
