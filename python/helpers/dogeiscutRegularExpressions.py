from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class dogeiscutRegularExpressions:

    @grepr_dataclass()
    class regex(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::regular expression (PATTERN) (FLAGS)"
        pattern: INPUT_COMPATIBLE_T
        flags: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PATTERN", "pattern", p.SRBlockAndTextInputValue, None),
                    ("FLAGS", "flags", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PATTERN", "pattern", p.SRBlockAndTextInputValue, None),
                    ("FLAGS", "flags", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class escape(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::escape (STRING) for regex"
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("STRING", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class source_of(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::source of (REGEX)"
        regex: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("REGEX", "regex", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("REGEX", "regex", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class flags_of(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::flags of (REGEX)"
        regex: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("REGEX", "regex", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("REGEX", "regex", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class test(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::test (STRING) for (REGEX)"
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class search(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::search (STRING) with (REGEX)"
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class replace(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::replace (REGEX) in (A) with (B)"
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class replace_all(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::replace all (REGEX) in (A) with (B)"
        regex: INPUT_COMPATIBLE_T
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("A", "a", p.SRBlockAndTextInputValue, None),
                    ("B", "b", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class split(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::split (STRING) by (REGEX)"
        string: INPUT_COMPATIBLE_T
        regex: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class match(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::match (REGEX) with (STRING)"
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class match_all(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::match all (REGEX) with (STRING)"
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class exec(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::execute (REGEX) on (STRING)"
        regex: INPUT_COMPATIBLE_T
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("STRING", "string", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_last_index(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::get last index of (REGEX)"
        regex: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("REGEX", "regex", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("REGEX", "regex", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class set_last_index(ThirdBlock):
        OPCODE = "&dogeiscutRegularExpressions::set last index of (REGEX) to (INDEX)"
        regex: INPUT_COMPATIBLE_T
        index: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("REGEX", "regex", p.SRBlockOnlyInputValue, None),
                    ("INDEX", "index", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )
