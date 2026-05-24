from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class divIterator:

    @grepr_dataclass()
    class iter_item(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divIterator::item", inputs={}, dropdowns={})

    @grepr_dataclass()
    class iter_acc(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divIterator::acc", inputs={}, dropdowns={})

    @grepr_dataclass()
    class iter_advance(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::advance (ITER)",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_next(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::next item from (ITER)",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_is_iter(ThirdBlock):
        thing: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_done(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) is done?",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_clone(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::clone (ITER)",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_clonable(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) is clonable?",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_branch(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        num: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_term_for_each(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_range(ThirdBlock):
        start: INPUT_COMPATIBLE_T
        end: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_iter_over(ThirdBlock):
        val: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_builder(ThirdBlock):
        state: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_builder_get_state(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&divIterator::state", inputs={}, dropdowns={})

    @grepr_dataclass()
    class iter_builder_set_state(ThirdBlock):
        state: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_builder_item(ThirdBlock):
        item: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_builder_done(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::finish iterator", inputs={}, dropdowns={}
            )

    @grepr_dataclass()
    class iter_adapter_map(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        map: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_keep(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_enum(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then enumerate items",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_adapter_cycle(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) then cycle items",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_adapter_take(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_skip(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_step_by(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        step: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_chain(ThirdBlock):
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_zip(ThirdBlock):
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_cross(ThirdBlock):
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_adapter_inspect(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_collect_to(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        type: str

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

    @grepr_dataclass()
    class iter_term_count(ThirdBlock):
        iter: INPUT_COMPATIBLE_T

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::(ITER) finally count items",
                inputs={
                    "ITER": ThirdInputValue.as_input(self.iter, p.SRBlockOnlyInputValue)
                },
                dropdowns={},
            )

    @grepr_dataclass()
    class iter_term_fold(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        init: INPUT_COMPATIBLE_T
        fold: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_term_any(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class iter_term_all(ThirdBlock):
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

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

    @grepr_dataclass()
    class menu_from_iter(ThirdBlock):

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&divIterator::#menu:fromIter", inputs={}, dropdowns={}
            )
