from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


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
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_next(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::next item from (ITER)",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_is_iter(thing: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::is (THING) an iterator?",
            inputs={
                "THING": ThirdInputValue.as_input(thing, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def iter_done(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) is done?",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_clone(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::clone (ITER)",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_clonable(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) is clonable?",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_branch(iter: INPUT_COMPATIBLE_T, num: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::branch (ITER) into (NUM) branches",
            inputs={
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "NUM": ThirdInputValue.as_input(num, p.SRBlockAndTextInputValue),
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
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "I": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_item()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_range(start: INPUT_COMPATIBLE_T, end: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::range from (START) to (END)",
            inputs={
                "START": ThirdInputValue.as_input(start, p.SRBlockAndTextInputValue),
                "END": ThirdInputValue.as_input(end, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_iter_over(val: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::iter over (VAL)",
            inputs={"VAL": ThirdInputValue.as_input(val, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_builder(
        state: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}",
            inputs={
                "STATE": ThirdInputValue.as_input(state, p.SRBlockAndTextInputValue),
                "S": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_builder_get_state()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
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
                "STATE": ThirdInputValue.as_input(state, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def iter_builder_item(item: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::return item (ITEM)",
            inputs={"ITEM": ThirdInputValue.as_input(item, p.SRBlockAndTextInputValue)},
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
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "I": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_item()),
                    p.SREmbeddedBlockInputValue,
                ),
                "MAP": ThirdInputValue.as_input(map, p.SRBlockAndTextInputValue),
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
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "I": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_item()),
                    p.SREmbeddedBlockInputValue,
                ),
                "PRED": ThirdInputValue.as_input(pred, p.SRBlockAndBoolInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_enum(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then enumerate items",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_cycle(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then cycle items",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_adapter_take(
        iter: INPUT_COMPATIBLE_T, count: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) then take (COUNT) items",
            inputs={
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "COUNT": ThirdInputValue.as_input(count, p.SRBlockAndTextInputValue),
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
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "COUNT": ThirdInputValue.as_input(count, p.SRBlockAndTextInputValue),
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
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "STEP": ThirdInputValue.as_input(step, p.SRBlockAndTextInputValue),
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
                "ITER1": ThirdInputValue.as_input(iter1, p.SRBlockOnlyInputValue),
                "ITER2": ThirdInputValue.as_input(iter2, p.SRBlockOnlyInputValue),
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
                "ITER1": ThirdInputValue.as_input(iter1, p.SRBlockOnlyInputValue),
                "ITER2": ThirdInputValue.as_input(iter2, p.SRBlockOnlyInputValue),
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
                "ITER1": ThirdInputValue.as_input(iter1, p.SRBlockOnlyInputValue),
                "ITER2": ThirdInputValue.as_input(iter2, p.SRBlockOnlyInputValue),
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
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "I": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_item()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_collect_to(iter: INPUT_COMPATIBLE_T, type: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally collect to [TYPE]",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={"TYPE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, type)},
        )

    @staticmethod
    def iter_term_count(iter: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally count items",
            inputs={"ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue)},
            dropdowns={},
        )

    @staticmethod
    def iter_term_fold(
        iter: INPUT_COMPATIBLE_T, init: INPUT_COMPATIBLE_T, fold: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally reduce (INIT) with {:A:} {:I:} (FOLD)",
            inputs={
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "INIT": ThirdInputValue.as_input(init, p.SRBlockAndTextInputValue),
                "FOLD": ThirdInputValue.as_input(fold, p.SRBlockAndTextInputValue),
                "A": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_acc()), p.SREmbeddedBlockInputValue
                ),
                "I": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_item()),
                    p.SREmbeddedBlockInputValue,
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_term_any(iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally any {:I:} <PRED>",
            inputs={
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "PRED": ThirdInputValue.as_input(pred, p.SRBlockAndBoolInputValue),
                "I": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_item()),
                    p.SREmbeddedBlockInputValue,
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def iter_term_all(iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&divIterator::(ITER) finally all {:I:} <PRED>",
            inputs={
                "ITER": ThirdInputValue.as_input(iter, p.SRBlockOnlyInputValue),
                "PRED": ThirdInputValue.as_input(pred, p.SRBlockAndBoolInputValue),
                "I": ThirdInputValue.as_input(
                    ThirdInputValue(divIterator.iter_item()),
                    p.SREmbeddedBlockInputValue,
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def menu_from_iter() -> p.SRBlock:
        return p.SRBlock(opcode="&divIterator::#menu:fromIter", inputs={}, dropdowns={})
