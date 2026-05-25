from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class divIterator:

    @grepr_dataclass()
    class iter_item(ThirdBlock):
        OPCODE = "&divIterator::item"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class iter_acc(ThirdBlock):
        OPCODE = "&divIterator::acc"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class iter_advance(ThirdBlock):
        OPCODE = "&divIterator::advance (ITER)"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_next(ThirdBlock):
        OPCODE = "&divIterator::next item from (ITER)"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_is_iter(ThirdBlock):
        OPCODE = "&divIterator::is (THING) an iterator?"
        thing: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("THING", "thing", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("THING", "thing", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_done(ThirdBlock):
        OPCODE = "&divIterator::(ITER) is done?"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_clone(ThirdBlock):
        OPCODE = "&divIterator::clone (ITER)"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_clonable(ThirdBlock):
        OPCODE = "&divIterator::(ITER) is clonable?"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_branch(ThirdBlock):
        OPCODE = "&divIterator::branch (ITER) into (NUM) branches"
        iter: INPUT_COMPATIBLE_T
        num: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("NUM", "num", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("NUM", "num", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_term_for_each(ThirdBlock):
        OPCODE = "&divIterator::for {:I:} of (ITER) {SUBSTACK}"
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_range(ThirdBlock):
        OPCODE = "&divIterator::range from (START) to (END)"
        start: INPUT_COMPATIBLE_T
        end: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("START", "start", p.SRBlockAndTextInputValue, None),
                    ("END", "end", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("START", "start", p.SRBlockAndTextInputValue, None),
                    ("END", "end", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_iter_over(ThirdBlock):
        OPCODE = "&divIterator::iter over (VAL)"
        val: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("VAL", "val", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("VAL", "val", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_builder(ThirdBlock):
        OPCODE = "&divIterator::iterator builder with {:S:} = (STATE) {SUBSTACK}"
        state: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STATE", "state", p.SRBlockAndTextInputValue, None),
                    (
                        "S",
                        "s",
                        p.SREmbeddedBlockInputValue,
                        divIterator.iter_builder_get_state,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STATE", "state", p.SRBlockAndTextInputValue, None),
                    (
                        "S",
                        "s",
                        p.SREmbeddedBlockInputValue,
                        divIterator.iter_builder_get_state,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_builder_get_state(ThirdBlock):
        OPCODE = "&divIterator::state"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class iter_builder_set_state(ThirdBlock):
        OPCODE = "&divIterator::set state to (STATE)"
        state: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STATE", "state", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("STATE", "state", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_builder_item(ThirdBlock):
        OPCODE = "&divIterator::return item (ITEM)"
        item: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITEM", "item", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITEM", "item", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_builder_done(ThirdBlock):
        OPCODE = "&divIterator::finish iterator"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class iter_adapter_map(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then map {:I:} (MAP)"
        iter: INPUT_COMPATIBLE_T
        map: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("MAP", "map", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("MAP", "map", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_keep(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then keep {:I:} if <PRED>"
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_enum(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then enumerate items"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_adapter_cycle(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then cycle items"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_adapter_take(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then take (COUNT) items"
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("COUNT", "count", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("COUNT", "count", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_skip(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then skip (COUNT) items"
        iter: INPUT_COMPATIBLE_T
        count: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("COUNT", "count", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("COUNT", "count", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_step_by(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then step by (STEP) items"
        iter: INPUT_COMPATIBLE_T
        step: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("STEP", "step", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("STEP", "step", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_chain(ThirdBlock):
        OPCODE = "&divIterator::(ITER1) then chain with (ITER2)"
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                    ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                    ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_zip(ThirdBlock):
        OPCODE = "&divIterator::(ITER1) then zip with (ITER2)"
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                    ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                    ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_cross(ThirdBlock):
        OPCODE = "&divIterator::(ITER1) then cross with (ITER2)"
        iter1: INPUT_COMPATIBLE_T
        iter2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                    ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER1", "iter1", p.SRBlockOnlyInputValue, None),
                    ("ITER2", "iter2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_adapter_inspect(ThirdBlock):
        OPCODE = "&divIterator::(ITER) then inspect {:I:} {SUBSTACK}"
        iter: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_collect_to(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally collect to [TYPE]"
        iter: INPUT_COMPATIBLE_T
        type: str

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (("TYPE", "type"),),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (("TYPE", "type"),),
            )

    @grepr_dataclass()
    class iter_term_count(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally count items"
        iter: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("ITER", "iter", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("ITER", "iter", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class iter_term_fold(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally reduce (INIT) with {:A:} {:I:} (FOLD)"
        iter: INPUT_COMPATIBLE_T
        init: INPUT_COMPATIBLE_T
        fold: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("INIT", "init", p.SRBlockAndTextInputValue, None),
                    ("FOLD", "fold", p.SRBlockAndTextInputValue, None),
                    ("A", "a", p.SREmbeddedBlockInputValue, divIterator.iter_acc),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("INIT", "init", p.SRBlockAndTextInputValue, None),
                    ("FOLD", "fold", p.SRBlockAndTextInputValue, None),
                    ("A", "a", p.SREmbeddedBlockInputValue, divIterator.iter_acc),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_term_any(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally any {:I:} <PRED>"
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                ),
                (),
            )

    @grepr_dataclass()
    class iter_term_all(ThirdBlock):
        OPCODE = "&divIterator::(ITER) finally all {:I:} <PRED>"
        iter: INPUT_COMPATIBLE_T
        pred: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("ITER", "iter", p.SRBlockOnlyInputValue, None),
                    ("PRED", "pred", p.SRBlockAndBoolInputValue, None),
                    ("I", "i", p.SREmbeddedBlockInputValue, divIterator.iter_item),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_from_iter(ThirdBlock):
        OPCODE = "&divIterator::#menu:fromIter"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
