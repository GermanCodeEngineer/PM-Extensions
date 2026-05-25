from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T
from typing import Self


class gceOOP:

    @grepr_dataclass()
    class temp_block(ThirdBlock):
        OPCODE = "&gceOOP::temp block with (INSTANCE) end"
        instance: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INSTANCE", "instance", p.SRBlockOnlyInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INSTANCE", "instance", p.SRBlockOnlyInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class temp_block2(ThirdBlock):
        OPCODE = "&gceOOP::temp command with (A) and (B)"
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("A", "a", p.SRBlockOnlyInputValue, None),
                    ("B", "b", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("A", "a", p.SRBlockOnlyInputValue, None),
                    ("B", "b", p.SRBlockOnlyInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_class_at(ThirdBlock):
        OPCODE = "&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_subclass_at(ThirdBlock):
        OPCODE = "&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_class_named(ThirdBlock):
        OPCODE = "&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_subclass_named(ThirdBlock):
        OPCODE = "&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class on_class(ThirdBlock):
        OPCODE = "&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}"
        class_: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.current_class,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class current_class(ThirdBlock):
        OPCODE = "&gceOOP::current class"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class is_subclass(ThirdBlock):
        OPCODE = "&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?"
        subclass: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("SUBCLASS", "subclass", p.SRBlockAndTextInputValue, None),
                    ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("SUBCLASS", "subclass", p.SRBlockAndTextInputValue, None),
                    ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_superclass(ThirdBlock):
        OPCODE = "&gceOOP::get superclass of (CLASS)"
        class_: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("CLASS", "class_", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("CLASS", "class_", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class define_instance_method(ThirdBlock):
        OPCODE = "&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class define_special_method(ThirdBlock):
        OPCODE = (
            "&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}"
        )
        special_method: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "SPECIAL_METHOD",
                        "special_method",
                        p.SRBlockAndDropdownInputValue,
                        None,
                    ),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "SPECIAL_METHOD",
                        "special_method",
                        p.SRBlockAndDropdownInputValue,
                        None,
                    ),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class self_value(ThirdBlock):
        OPCODE = "&gceOOP::self"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class call_super_method(ThirdBlock):
        OPCODE = "&gceOOP::call super method (NAME) with positional args (POSARGS)"
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class call_super_init_method(ThirdBlock):
        OPCODE = "&gceOOP::call super init method with positional args (POSARGS)"
        posargs: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class define_getter(ThirdBlock):
        OPCODE = "&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class define_setter(ThirdBlock):
        OPCODE = "&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW1",
                        "shadow1",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    (
                        "SHADOW2",
                        "shadow2",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.define_setter_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    (
                        "SHADOW1",
                        "shadow1",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.self_value,
                    ),
                    (
                        "SHADOW2",
                        "shadow2",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.define_setter_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class define_operator_method(ThirdBlock):
        OPCODE = (
            "&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}"
        )
        operator_kind: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "OPERATOR_KIND",
                        "operator_kind",
                        p.SRBlockAndDropdownInputValue,
                        None,
                    ),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.operator_operator_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "OPERATOR_KIND",
                        "operator_kind",
                        p.SRBlockAndDropdownInputValue,
                        None,
                    ),
                    (
                        "SHADOW",
                        "shadow",
                        p.SREmbeddedBlockInputValue,
                        gceOOP.operator_operator_value,
                    ),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class operator_operator_value(ThirdBlock):
        OPCODE = "&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class set_class_variable(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) set class var (NAME) to (VALUE)"
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_class_variable(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) get class var (NAME)"
        name: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class delete_class_variable(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) delete class var (NAME)"
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class define_static_method(ThirdBlock):
        OPCODE = "&gceOOP::define static method (NAME) {SUBSTACK}"
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("SUBSTACK", "substack", p.SRScriptInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class property_names_of_class(ThirdBlock):
        OPCODE = "&gceOOP::([PROPERTY]) names of class (CLASS)"
        property: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class create_instance(ThirdBlock):
        OPCODE = (
            "&gceOOP::create instance of class (CLASS) with positional args (POSARGS)"
        )
        class_: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class is_instance(ThirdBlock):
        OPCODE = "&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?"
        potential_instance: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    (
                        "POTENTIAL_INSTANCE",
                        "potential_instance",
                        p.SRBlockAndTextInputValue,
                        None,
                    ),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    (
                        "POTENTIAL_INSTANCE",
                        "potential_instance",
                        p.SRBlockAndTextInputValue,
                        None,
                    ),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_class_of_instance(ThirdBlock):
        OPCODE = "&gceOOP::get class of (INSTANCE)"
        instance: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class set_attribute(ThirdBlock):
        OPCODE = "&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)"
        instance: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("VALUE", "value", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_attribute(ThirdBlock):
        OPCODE = "&gceOOP::on (INSTANCE) get attribute (NAME)"
        name: INPUT_COMPATIBLE_T
        instance: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_all_attributes(ThirdBlock):
        OPCODE = "&gceOOP::all attributes of (INSTANCE)"
        instance: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),),
                (),
            )

    @grepr_dataclass()
    class call_method(ThirdBlock):
        OPCODE = (
            "&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)"
        )
        instance: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class call_static_method(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)"
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class get_static_method_func(ThirdBlock):
        OPCODE = "&gceOOP::get static method (NAME) of (CLASS) as function"
        name: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(
                block,
                cls.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(
                self.OPCODE,
                (
                    ("NAME", "name", p.SRBlockAndTextInputValue, None),
                    ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
                ),
                (),
            )

    @grepr_dataclass()
    class define_setter_value(ThirdBlock):
        OPCODE = "&gceOOP::operator value {{id=gceOOP_defineSetterValue}}"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_class_property(ThirdBlock):
        OPCODE = "&gceOOP::#menu:classProperty"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_operator_method(ThirdBlock):
        OPCODE = "&gceOOP::#menu:operatorMethod"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())

    @grepr_dataclass()
    class menu_special_method(ThirdBlock):
        OPCODE = "&gceOOP::#menu:specialMethod"

        @classmethod
        def from_second(cls, block: p.SRBlock) -> Self:
            return cls._from_second_block(block, cls.OPCODE, (), ())

        def to_second(self) -> p.SRBlock:
            return self._to_second_block(self.OPCODE, (), ())
