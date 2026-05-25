from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T


class divIterator:

    @grepr_dataclass()
    class iter_item(ThirdBlock):
        OPCODE = "&divIterator::item"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class iter_acc(ThirdBlock):
        OPCODE = "&divIterator::acc"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class iter_advance(ThirdBlock):
        OPCODE = "&divIterator::advance (ITER)"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_next(ThirdBlock):
        OPCODE = "&divIterator::next item from (ITER)"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_is_iter(ThirdBlock):
        OPCODE = "&divIterator::is (THING) an iterator?"
        INPUT_SPECS = (("THING", "thing", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        thing: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_done(ThirdBlock):
        OPCODE = "&divIterator::(ITER) is done?"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_clone(ThirdBlock):
        OPCODE = "&divIterator::clone (ITER)"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_clonable(ThirdBlock):
        OPCODE = "&divIterator::(ITER) is clonable?"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_branch(ThirdBlock):
        OPCODE = "&divIterator::branch (ITER) into (NUM) branches"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("NUM", "num", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        num: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_for_each(ThirdBlock):
        OPCODE = "&divIterator::for {:I:} of (ITER) {SUBSTACK}"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_range(ThirdBlock):
        OPCODE = "&divIterator::range from (START) to (END)"
        INPUT_SPECS = (
            ("START", "start", p.SRBlockAndTextInputValue, None),
            ("END", "end", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        start: INPUT_COMPATIBLE_T
        end: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_iter_over(ThirdBlock):
        OPCODE = "&divIterator::iter over (VAL)"
        INPUT_SPECS = (("VAL", "val", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        val: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder(ThirdBlock):
        OPCODE = "&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}"
        INPUT_SPECS = (
            ("STATE", "state", p.SRBlockAndTextInputValue, None),
            (
                "S",
                "s",
                p.SREmbeddedBlockInputValue,
                lambda: divIterator.iter_builder_get_state(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        state: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder_get_state(ThirdBlock):
        OPCODE = "&divIterator::state"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class iter_builder_set_state(ThirdBlock):
        OPCODE = "&divIterator::set state to (STATE)"
        INPUT_SPECS = (("STATE", "state", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        state: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder_item(ThirdBlock):
        OPCODE = "&divIterator::return item (ITEM)"
        INPUT_SPECS = (("ITEM", "item", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        item: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_builder_done(ThirdBlock):
        OPCODE = "&divIterator::finish iterator"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class iter_adapter_map(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then map {:I:} (MAP)"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("MAP", "map", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        map: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_keep(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then keep {:I:} if <PRED>"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_enum(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then enumerate items"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_cycle(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then cycle items"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_take(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then take (COUNT) items"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("COUNT", "count", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_skip(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then skip (COUNT) items"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("COUNT", "count", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_step_by(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then step by (STEP) items"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("STEP", "step", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        step: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_chain(ThirdBlock):
        OPCODE = "&divIterator::(ITER1) then chain with (ITER2)"
        INPUT_SPECS = (
            ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
            ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_zip(ThirdBlock):
        OPCODE = "&divIterator::(ITER1) then zip with (ITER2)"
        INPUT_SPECS = (
            ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
            ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_cross(ThirdBlock):
        OPCODE = "&divIterator::(ITER1) then cross with (ITER2)"
        INPUT_SPECS = (
            ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
            ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_adapter_inspect(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then inspect {:I:} {SUBSTACK}"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_collect_to(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally collect to [TYPE]"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = (("TYPE", "type"),)
        iter: INPUT_COMPATIBLE_T
        type: str

    @grepr_dataclass()
    class iter_term_count(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally count items"
        INPUT_SPECS = (("ITER", "iter", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_fold(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally reduce (INIT) with {:A:} {:I:} (FOLD)"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("INIT", "init", p.SRBlockAndTextInputValue, None),
            ("FOLD", "fold", p.SRBlockAndTextInputValue, None),
            ("A", "a", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_acc()),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        init: INPUT_COMPATIBLE_T
        fold: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_any(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally any {:I:} <PRED>"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class iter_term_all(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally all {:I:} <PRED>"
        INPUT_SPECS = (
            ("ITER", "iter", p.SRBlockOnlyInputValue, None),
            ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
            ("I", "i", p.SREmbeddedBlockInputValue, lambda: divIterator.iter_item()),
        )
        DROPDOWN_SPECS = ()
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class menu_from_iter(ThirdBlock):
        OPCODE = "&divIterator::#menu:fromIter"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
