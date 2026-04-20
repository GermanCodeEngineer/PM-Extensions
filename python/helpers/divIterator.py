from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class divIterator:

    @staticmethod
    def iter_item() -> p.SRBlock:
        return p.SRBlock(opcode="&divIterator::item", inputs={}, dropdowns={})

    @staticmethod
    def iter_acc() -> p.SRBlock:
        return p.SRBlock(opcode="&divIterator::acc", inputs={}, dropdowns={})

    @staticmethod
    def iter_advance(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::advance (ITER)",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_next(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::next item from (ITER)",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_is_iter(thing: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::is (THING) an iterator?",
            inputs={
                "THING": InputValue.try_as_input(thing, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def iter_done(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) is done?",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_clone(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::clone (ITER)",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_clonable(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) is clonable?",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_branch(iter: INPUT_COMPATIBLE_T, num: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::branch (ITER) into (NUM) branches",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "NUM": InputValue.try_as_input(num, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_term_for_each(
        iter: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::for {:I:} of (ITER) {SUBSTACK}",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "I": InputValue.try_as_input(
                    InputValue(divIterator.iter_item()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_range(start: INPUT_COMPATIBLE_T, end: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::range from (START) to (END)",
            inputs={
                "START": InputValue.try_as_input(start, p.SRBlockAndTextInputValue),
                "END": InputValue.try_as_input(end, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_iter_over(val: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::iter over (VAL)",
            inputs={"VAL": InputValue.try_as_input(val, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_builder(
        state: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}",
            inputs={
                "STATE": InputValue.try_as_input(state, p.SRBlockAndTextInputValue),
                "S": InputValue.try_as_input(
                    InputValue(divIterator.iter_builder_get_state()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_builder_get_state() -> p.SRBlock:
        return p.SRBlock(opcode="&divIterator::state", inputs={}, dropdowns={})

    @staticmethod
    def iter_builder_set_state(state: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::set state to (STATE)",
            inputs={
                "STATE": InputValue.try_as_input(state, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def iter_builder_item(item: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::return item (ITEM)",
            inputs={"ITEM": InputValue.try_as_input(item, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_builder_done() -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::finish iterator", inputs={}, dropdowns={}
        )

    @staticmethod
    def iter_adapter_map(
        iter: INPUT_COMPATIBLE_T, map: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then map {:I:} (MAP)",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "I": InputValue.try_as_input(
                    InputValue(divIterator.iter_item()), p.SREmbeddedBlockInputValue
                ),
                "MAP": InputValue.try_as_input(map, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_keep(
        iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then keep {:I:} if <PRED>",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "I": InputValue.try_as_input(
                    InputValue(divIterator.iter_item()), p.SREmbeddedBlockInputValue
                ),
                "PRED": InputValue.try_as_input(pred, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_enum(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then enumerate items",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_cycle(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then cycle items",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_take(
        iter: INPUT_COMPATIBLE_T, count: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then take (COUNT) items",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "COUNT": InputValue.try_as_input(count, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_skip(
        iter: INPUT_COMPATIBLE_T, count: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then skip (COUNT) items",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "COUNT": InputValue.try_as_input(count, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_step_by(
        iter: INPUT_COMPATIBLE_T, step: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then step by (STEP) items",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "STEP": InputValue.try_as_input(step, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_chain(
        iter1: INPUT_COMPATIBLE_T, iter2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER1) then chain with (ITER2)",
            inputs={
                "ITER1": InputValue.try_as_input(iter1, p.SRBlockAndTextInputValue),
                "ITER2": InputValue.try_as_input(iter2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_zip(
        iter1: INPUT_COMPATIBLE_T, iter2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER1) then zip with (ITER2)",
            inputs={
                "ITER1": InputValue.try_as_input(iter1, p.SRBlockAndTextInputValue),
                "ITER2": InputValue.try_as_input(iter2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_cross(
        iter1: INPUT_COMPATIBLE_T, iter2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER1) then cross with (ITER2)",
            inputs={
                "ITER1": InputValue.try_as_input(iter1, p.SRBlockAndTextInputValue),
                "ITER2": InputValue.try_as_input(iter2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_inspect(
        iter: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then inspect {:I:} {SUBSTACK}",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "I": InputValue.try_as_input(
                    InputValue(divIterator.iter_item()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_collect_to(iter: INPUT_COMPATIBLE_T, type: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally collect to [TYPE]",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={"TYPE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, type)},
        )

    @staticmethod
    def iter_term_count(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally count items",
            inputs={"ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_term_fold(
        iter: INPUT_COMPATIBLE_T, init: INPUT_COMPATIBLE_T, fold: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally reduce (INIT) with {:A:} {:I:} (FOLD)",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "INIT": InputValue.try_as_input(init, p.SRBlockAndTextInputValue),
                "FOLD": InputValue.try_as_input(fold, p.SRBlockAndTextInputValue),
                "A": InputValue.try_as_input(
                    InputValue(divIterator.iter_acc()), p.SREmbeddedBlockInputValue
                ),
                "I": InputValue.try_as_input(
                    InputValue(divIterator.iter_item()), p.SREmbeddedBlockInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_term_any(iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally any {:I:} <PRED>",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "PRED": InputValue.try_as_input(pred, p.SRBlockAndBoolInputValue),
                "I": InputValue.try_as_input(
                    InputValue(divIterator.iter_item()), p.SREmbeddedBlockInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_term_all(iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally all {:I:} <PRED>",
            inputs={
                "ITER": InputValue.try_as_input(iter, p.SRBlockAndTextInputValue),
                "PRED": InputValue.try_as_input(pred, p.SRBlockAndBoolInputValue),
                "I": InputValue.try_as_input(
                    InputValue(divIterator.iter_item()), p.SREmbeddedBlockInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_from_iter() -> p.SRBlock:
        return p.SRBlock(opcode="&divIterator::#menu:fromIter", inputs={}, dropdowns={})
