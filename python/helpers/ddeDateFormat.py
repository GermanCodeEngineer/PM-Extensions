from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class ddeDateFormat:

    @grepr_dataclass()
    class current_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::current date"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class create_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::new date from (string)"
        string: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("string", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("string", "string", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class format_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::format date (date) as (format)"
        date: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                    ("format", "format", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                    ("format", "format", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class locale_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::format date (date) to ([type]) locale"
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                    ("type", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                    ("type", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class compare_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::is date (date1) ([operation]) date [date2]?"
        date1: INPUT_COMPATIBLE_T
        operation: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date1", "date1", p.SRBlockAndTextInputValue, None),
                    ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
                    ("date2", "date2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date1", "date1", p.SRBlockAndTextInputValue, None),
                    ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
                    ("date2", "date2", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_valid(ThirdBlock):
        OPCODE = "&ddeDateFormat::is date (date) valid?"
        date: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("date", "date", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("date", "date", p.SRBlockAndTextInputValue, None),), ()
            )

    @grepr_dataclass()
    class get_date_part(ThirdBlock):
        OPCODE = "&ddeDateFormat::get ([part]) of (date)"
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class add_time(ThirdBlock):
        OPCODE = "&ddeDateFormat::add (amount) ([unit]) to (date)"
        amount: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("amount", "amount", p.SRBlockAndTextInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("amount", "amount", p.SRBlockAndTextInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class diff_date(ThirdBlock):
        OPCODE = "&ddeDateFormat::difference between (date1) and (date2) in ([unit])"
        date1: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date1", "date1", p.SRBlockAndTextInputValue, None),
                    ("date2", "date2", p.SRBlockAndTextInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date1", "date1", p.SRBlockAndTextInputValue, None),
                    ("date2", "date2", p.SRBlockAndTextInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_compare_operations(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:compareOperations"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_date_parts(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:dateParts"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_time_units(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:timeUnits"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_locale_length(ThirdBlock):
        OPCODE = "&ddeDateFormat::#menu:localeLength"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
