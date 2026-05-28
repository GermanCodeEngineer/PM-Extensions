from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class divIterator:

    @grepr_dataclass()
    class iter_item(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::item"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class iter_acc(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::acc"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class iter_advance(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::advance (ITER)"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_next(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::next item from (ITER)"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_is_iter(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::is (THING) an iterator?"
        INPUT_SPECS: ClassVar = (("THING", "thing", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        thing: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_done(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) is done?"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_clone(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::clone (ITER)"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_clonable(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) is clonable?"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_branch(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::branch (ITER) into (NUM) branches"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("NUM", "num", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_for_each(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::for {:I:} of (ITER) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_range(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::range from (START) to (END)"
        INPUT_SPECS: ClassVar = (
            ("START", "start", p.SRBlockAndTextInputValue, None),
            ("END", "end", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        start: INPUT_COMPATIBLE_T
        end: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_iter_over(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::iter over (VAL)"
        INPUT_SPECS: ClassVar = (("VAL", "val", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        val: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder(ThirdBlock):
        OPCODE: ClassVar = (
            "&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("STATE", "state", p.SRBlockAndTextInputValue, None),
            (
                "S",
                "s",
                p.SREmbeddedBlockInputValue,
                lambda: divIterator.iter_builder_get_state(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        state: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder_get_state(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::state"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class iter_builder_set_state(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::set state to (STATE)"
        INPUT_SPECS: ClassVar = (("STATE", "state", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        state: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder_item(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::return item (ITEM)"
        INPUT_SPECS: ClassVar = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        item: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder_done(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::finish iterator"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class iter_adapter_map(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then map {:I:} (MAP)"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("MAP", "map", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        map: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_keep(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then keep {:I:} if <PRED>"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_enum(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then enumerate items"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_cycle(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then cycle items"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_take(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then take (COUNT) items"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("COUNT", "count", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_skip(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then skip (COUNT) items"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("COUNT", "count", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_step_by(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then step by (STEP) items"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("STEP", "step", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        step: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_chain(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER1) then chain with (ITER2)"
        INPUT_SPECS: ClassVar = (
            ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
            ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_zip(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER1) then zip with (ITER2)"
        INPUT_SPECS: ClassVar = (
            ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
            ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_cross(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER1) then cross with (ITER2)"
        INPUT_SPECS: ClassVar = (
            ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
            ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_inspect(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) then inspect {:I:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_collect_to(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) finally collect to [TYPE]"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = (("TYPE", "type"),)
        iter: INPUT_COMPATIBLE_T
        type: str

    @grepr_dataclass()
    class iter_term_count(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) finally count items"
        INPUT_SPECS: ClassVar = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_fold(ThirdBlock):
        OPCODE: ClassVar = (
            "&divIterator::(ITER) finally reduce (INIT) with {:A:} {:I:} (FOLD)"
        )
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("INIT", "init", p.SRBlockAndTextInputValue, None),
            ("FOLD", "fold", p.SRBlockAndTextInputValue, None),
            ("A", "a", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_acc()),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        init: INPUT_COMPATIBLE_T
        fold: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_any(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) finally any {:I:} <PRED>"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_all(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::(ITER) finally all {:I:} <PRED>"
        INPUT_SPECS: ClassVar = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
        )
        DROPDOWN_SPECS: ClassVar = ()
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_from_iter(ThirdBlock):
        OPCODE: ClassVar = "&divIterator::#menu:fromIter"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
