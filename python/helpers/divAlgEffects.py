from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class divAlgEffects:

    @grepr_dataclass()
    class eff_perform_ret(ThirdBlock):
        OPCODE = "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerformRet}}"
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class eff_handle(ThirdBlock):
        OPCODE = "&divAlgEffects::handle in {SUBSTACK} effects {SUBSTACK2}"
        substack: INPUT_COMPATIBLE_T
        substack2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                    ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                    ("SUBSTACK2", "substack2", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class eff_handler_case(ThirdBlock):
        OPCODE = "&divAlgEffects::effect (EFF) with {:DATA:} {SUBSTACK}"
        eff: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                    (
                        "DATA",
                        "data",
                        p.SREmbeddedBlockInputValue,
                        divAlgEffects.eff_data,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                    (
                        "DATA",
                        "data",
                        p.SREmbeddedBlockInputValue,
                        divAlgEffects.eff_data,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class eff_recurse_handler(ThirdBlock):
        OPCODE = "&divAlgEffects::recursively handle {SUBSTACK}"
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("SUBSTACK", "substack", p.SRScriptInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("SUBSTACK", "substack", p.SRScriptInputValue, None),), ()
            )

    @grepr_dataclass()
    class eff_resume_ret(ThirdBlock):
        OPCODE = "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeRet}}"
        data: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DATA", "data", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("DATA", "data", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class eff_resume_tail(ThirdBlock):
        OPCODE = "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResumeTail}}"
        data: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DATA", "data", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("DATA", "data", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class eff_data(ThirdBlock):
        OPCODE = "&divAlgEffects::data"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class eff_continuation(ThirdBlock):
        OPCODE = "&divAlgEffects::continuation"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class eff_cont_has_resumed(ThirdBlock):
        OPCODE = "&divAlgEffects::has (CONT) resumed?"
        cont: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CONT", "cont", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("CONT", "cont", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class eff_perform(ThirdBlock):
        OPCODE = (
            "&divAlgEffects::perform (EFF) with (DATA) {{id=divAlgEffects_effPerform}}"
        )
        eff: INPUT_COMPATIBLE_T
        data: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("EFF", "eff", p.SRBlockAndTextInputValue, None),
                    ("DATA", "data", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class eff_resume(ThirdBlock):
        OPCODE = "&divAlgEffects::resume with (DATA) {{id=divAlgEffects_effResume}}"
        data: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("DATA", "data", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("DATA", "data", p.SRBlockAndTextInputValue, None),), ()
            )
