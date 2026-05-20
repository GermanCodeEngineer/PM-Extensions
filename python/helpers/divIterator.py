from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class divIterator:

    class iter_item(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divIterator::item", inputs={}, dropdowns={})

    class iter_acc(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divIterator::acc", inputs={}, dropdowns={})

    class iter_advance(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::advance (ITER)",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_next(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::next item from (ITER)",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_is_iter(ThirdBlock):

        def __init__(self, thing: INPUT_COMPATIBLE_T):
            self.thing = thing

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::is (THING) an iterator?",
                inputs={
                    "THING": ThirdInputValue.as_input(
                        self.thing, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class iter_done(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) is done?",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_clone(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::clone (ITER)",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_clonable(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) is clonable?",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_branch(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, num: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.num = num

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::branch (ITER) into (NUM) branches",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "NUM": ThirdInputValue.as_input(
                        self.num, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_term_for_each(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::for {:I:} of (ITER) {SUBSTACK}",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_item()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_range(ThirdBlock):

        def __init__(self, start: INPUT_COMPATIBLE_T, end: INPUT_COMPATIBLE_T):
            self.start = start
            self.end = end

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::range from (START) to (END)",
                inputs={
                    "START": ThirdInputValue.as_input(
                        self.start, p.SRBlockAndTextInputValue
                    ),
                    "END": ThirdInputValue.as_input(
                        self.end, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_iter_over(ThirdBlock):

        def __init__(self, val: INPUT_COMPATIBLE_T):
            self.val = val

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::iter over (VAL)",
                inputs={
                    "VAL": ThirdInputValue.as_input(
                        self.val, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class iter_builder(ThirdBlock):

        def __init__(self, state: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.state = state
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}",
                inputs={
                    "STATE": ThirdInputValue.as_input(
                        self.state, p.SRBlockAndTextInputValue
                    ),
                    "S": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_builder_get_state()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_builder_get_state(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divIterator::state", inputs={}, dropdowns={})

    class iter_builder_set_state(ThirdBlock):

        def __init__(self, state: INPUT_COMPATIBLE_T):
            self.state = state

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::set state to (STATE)",
                inputs={
                    "STATE": ThirdInputValue.as_input(
                        self.state, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class iter_builder_item(ThirdBlock):

        def __init__(self, item: INPUT_COMPATIBLE_T):
            self.item = item

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::return item (ITEM)",
                inputs={
                    "ITEM": ThirdInputValue.as_input(
                        self.item, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class iter_builder_done(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::finish iterator", inputs={}, dropdowns={}
            )

    class iter_adapter_map(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, map: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.map = map

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then map {:I:} (MAP)",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_item()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "MAP": ThirdInputValue.as_input(
                        self.map, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_keep(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.pred = pred

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then keep {:I:} if <PRED>",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_item()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "PRED": ThirdInputValue.as_input(
                        self.pred, p.SRBlockAndBoolInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_enum(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then enumerate items",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_adapter_cycle(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then cycle items",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_adapter_take(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, count: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.count = count

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then take (COUNT) items",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "COUNT": ThirdInputValue.as_input(
                        self.count, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_skip(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, count: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.count = count

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then skip (COUNT) items",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "COUNT": ThirdInputValue.as_input(
                        self.count, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_step_by(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, step: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.step = step

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then step by (STEP) items",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "STEP": ThirdInputValue.as_input(
                        self.step, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_chain(ThirdBlock):

        def __init__(self, iter1: INPUT_COMPATIBLE_T, iter2: INPUT_COMPATIBLE_T):
            self.iter1 = iter1
            self.iter2 = iter2

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER1) then chain with (ITER2)",
                inputs={
                    "ITER1": ThirdInputValue.as_input(
                        self.iter1, p.SRBlockOnlyInputValue
                    ),
                    "ITER2": ThirdInputValue.as_input(
                        self.iter2, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_zip(ThirdBlock):

        def __init__(self, iter1: INPUT_COMPATIBLE_T, iter2: INPUT_COMPATIBLE_T):
            self.iter1 = iter1
            self.iter2 = iter2

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER1) then zip with (ITER2)",
                inputs={
                    "ITER1": ThirdInputValue.as_input(
                        self.iter1, p.SRBlockOnlyInputValue
                    ),
                    "ITER2": ThirdInputValue.as_input(
                        self.iter2, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_cross(ThirdBlock):

        def __init__(self, iter1: INPUT_COMPATIBLE_T, iter2: INPUT_COMPATIBLE_T):
            self.iter1 = iter1
            self.iter2 = iter2

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER1) then cross with (ITER2)",
                inputs={
                    "ITER1": ThirdInputValue.as_input(
                        self.iter1, p.SRBlockOnlyInputValue
                    ),
                    "ITER2": ThirdInputValue.as_input(
                        self.iter2, p.SRBlockOnlyInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_adapter_inspect(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then inspect {:I:} {SUBSTACK}",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_item()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class iter_collect_to(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, type: str):
            self.iter = iter
            self.type = type

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) finally collect to [TYPE]",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={
                    "TYPE": p.SRDropdownValue(p.DropdownValueKind.STANDARD, self.type)
                },
            )

    class iter_term_count(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T):
            self.iter = iter

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) finally count items",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    class iter_term_fold(ThirdBlock):

        def __init__(
            self,
            iter: INPUT_COMPATIBLE_T,
            init: INPUT_COMPATIBLE_T,
            fold: INPUT_COMPATIBLE_T,
        ):
            self.iter = iter
            self.init = init
            self.fold = fold

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) finally reduce (INIT) with {:A:} {:I:} (FOLD)",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "INIT": ThirdInputValue.as_input(
                        self.init, p.SRBlockAndTextInputValue
                    ),
                    "FOLD": ThirdInputValue.as_input(
                        self.fold, p.SRBlockAndTextInputValue
                    ),
                    "A": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_acc()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_item()),
                        p.SREmbeddedBlockInputValue,
                    ),
                },
                dropdowns={},
            )

    class iter_term_any(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.pred = pred

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) finally any {:I:} <PRED>",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "PRED": ThirdInputValue.as_input(
                        self.pred, p.SRBlockAndBoolInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_item()),
                        p.SREmbeddedBlockInputValue,
                    ),
                },
                dropdowns={},
            )

    class iter_term_all(ThirdBlock):

        def __init__(self, iter: INPUT_COMPATIBLE_T, pred: INPUT_COMPATIBLE_T):
            self.iter = iter
            self.pred = pred

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) finally all {:I:} <PRED>",
                inputs={
                    "ITER": ThirdInputValue.as_input(
                        self.iter, p.SRBlockOnlyInputValue
                    ),
                    "PRED": ThirdInputValue.as_input(
                        self.pred, p.SRBlockAndBoolInputValue
                    ),
                    "I": ThirdInputValue.as_input(
                        ThirdInputValue(divIterator.iter_item()),
                        p.SREmbeddedBlockInputValue,
                    ),
                },
                dropdowns={},
            )

    class menu_from_iter(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::#menu:fromIter", inputs={}, dropdowns={}
            )
