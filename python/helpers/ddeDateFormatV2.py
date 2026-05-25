from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class ddeDateFormatV2:

    @grepr_dataclass()
    class current_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::current date"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class create_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::new date from (string)"
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
        OPCODE = "&ddeDateFormatV2::format (date) as (format)"
        date: INPUT_COMPATIBLE_T
        format: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("format", "format", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("format", "format", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class locale_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::format (date) as ([type]) locale"
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("type", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("type", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class extra_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::format (date) as ([type])"
        date: INPUT_COMPATIBLE_T
        type: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("type", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("type", "type", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class iso_format_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::format (date) as ISO string"
        date: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("date", "date", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("date", "date", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class is_valid(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::is (date) valid?"
        date: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("date", "date", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE, (("date", "date", p.SRBlockOnlyInputValue, None),), ()
            )

    @grepr_dataclass()
    class compare_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::is (date1) ([operation]) [date2]?"
        date1: INPUT_COMPATIBLE_T
        operation: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date1", "date1", p.SRBlockOnlyInputValue, None),
                    ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
                    ("date2", "date2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date1", "date1", p.SRBlockOnlyInputValue, None),
                    ("operation", "operation", p.SRBlockAndDropdownInputValue, None),
                    ("date2", "date2", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class check_date_property(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::is (date) [property]?"
        date: INPUT_COMPATIBLE_T
        property: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("property", "property", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("property", "property", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class diff_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::get ([unit]) between (date1) and (date2)"
        date1: INPUT_COMPATIBLE_T
        date2: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date1", "date1", p.SRBlockOnlyInputValue, None),
                    ("date2", "date2", p.SRBlockOnlyInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date1", "date1", p.SRBlockOnlyInputValue, None),
                    ("date2", "date2", p.SRBlockOnlyInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_date_part(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::get UTC ([part]) of (date)"
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_date_part_new(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::get ([part]) of (date)"
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class set_date_part(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::set ([part]) of (date) to (value)"
        part: INPUT_COMPATIBLE_T
        date: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("value", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("part", "part", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("value", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class add_time(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::add (amount) ([unit]) to (date)"
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
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("amount", "amount", p.SRBlockAndTextInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class round_date(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::round (date) to nearest ([unit])"
        date: INPUT_COMPATIBLE_T
        unit: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("date", "date", p.SRBlockOnlyInputValue, None),
                    ("unit", "unit", p.SRBlockAndDropdownInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class menu_compare_operations(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:compareOperations"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_date_parts(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:dateParts"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_time_units(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:timeUnits"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_locale_length(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:localeLength"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_date_properties(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:dateProperties"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_extra_formats(ThirdBlock):
        OPCODE = "&ddeDateFormatV2::#menu:extraFormats"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
