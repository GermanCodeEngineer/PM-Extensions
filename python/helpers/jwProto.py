from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class jwProto:

    @grepr_dataclass()
    class label_function(ThirdBlock):
        OPCODE = "&jwProto::// (LABEL) {SUBSTACK}"
        label: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class label_command(ThirdBlock):
        OPCODE = "&jwProto::// (LABEL) {{id=jwProto_labelCommand}}"
        label: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LABEL", "label", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("LABEL", "label", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class label_reporter(ThirdBlock):
        OPCODE = "&jwProto::(VALUE) // (LABEL)"
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class label_boolean(ThirdBlock):
        OPCODE = "&jwProto::<VALUE> // (LABEL)"
        label: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("LABEL", "label", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndBoolInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class placeholder_reporter(ThirdBlock):
        OPCODE = "&jwProto::... {{id=jwProto_placeholderReporter}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class placeholder_boolean(ThirdBlock):
        OPCODE = "&jwProto::... {{id=jwProto_placeholderBoolean}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class label_hat(ThirdBlock):
        OPCODE = "&jwProto::// (LABEL) {{id=jwProto_labelHat}}"
        label: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("LABEL", "label", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("LABEL", "label", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class placeholder_command(ThirdBlock):
        OPCODE = "&jwProto::... {{id=jwProto_placeholderCommand}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
