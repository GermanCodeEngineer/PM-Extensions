from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdBlock, INPUT_COMPATIBLE_T
from typing import ClassVar


class gceOOP:

    @grepr_dataclass()
    class temp_block(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::temp block with (INSTANCE) end"
        INPUT_SPECS: ClassVar = (
            ("INSTANCE", "instance", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class temp_block2(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::temp command with (A) and (B)"
        INPUT_SPECS: ClassVar = (
            ("A", "a", p.SRBlockOnlyInputValue, None),
            ("B", "b", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_class_at(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.current_class(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_subclass_at(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.current_class(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_class_named(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.current_class(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_subclass_named(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.current_class(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class on_class(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.current_class(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        class_: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class current_class(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::current class"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class is_subclass(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?"
        INPUT_SPECS: ClassVar = (
            ("SUBCLASS", "subclass", p.SRBlockAndTextInputValue, None),
            ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        subclass: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_superclass(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::get superclass of (CLASS)"
        INPUT_SPECS: ClassVar = (("CLASS", "class_", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS: ClassVar = ()
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_instance_method(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.self_value(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_special_method(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("SPECIAL_METHOD", "special_method", p.SRBlockAndDropdownInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.self_value(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        special_method: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class self_value(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::self"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class call_super_method(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::call super method (NAME) with positional args (POSARGS)"
        )
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_super_init_method(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::call super init method with positional args (POSARGS)"
        )
        INPUT_SPECS: ClassVar = (
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_getter(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.self_value(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_setter(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            (
                "SHADOW1",
                "shadow1",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.self_value(),
            ),
            (
                "SHADOW2",
                "shadow2",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.define_setter_value(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_operator_method(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}"
        )
        INPUT_SPECS: ClassVar = (
            ("OPERATOR_KIND", "operator_kind", p.SRBlockAndDropdownInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                lambda: gceOOP.operator_operator_value(),
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        operator_kind: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class operator_operator_value(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class set_class_variable(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::on (CLASS) set class var (NAME) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_class_variable(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::on (CLASS) get class var (NAME)"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_class_variable(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::on (CLASS) delete class var (NAME)"
        INPUT_SPECS: ClassVar = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_static_method(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::define static method (NAME) {SUBSTACK}"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class property_names_of_class(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::([PROPERTY]) names of class (CLASS)"
        INPUT_SPECS: ClassVar = (
            ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        property: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_instance(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::create instance of class (CLASS) with positional args (POSARGS)"
        )
        INPUT_SPECS: ClassVar = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        class_: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_instance(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?"
        INPUT_SPECS: ClassVar = (
            (
                "POTENTIAL_INSTANCE",
                "potential_instance",
                p.SRBlockAndTextInputValue,
                None,
            ),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        potential_instance: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_class_of_instance(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::get class of (INSTANCE)"
        INPUT_SPECS: ClassVar = (
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_attribute(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)"
        INPUT_SPECS: ClassVar = (
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        instance: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_attribute(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::on (INSTANCE) get attribute (NAME)"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_all_attributes(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::all attributes of (INSTANCE)"
        INPUT_SPECS: ClassVar = (
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_method(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)"
        )
        INPUT_SPECS: ClassVar = (
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        instance: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_static_method(ThirdBlock):
        OPCODE: ClassVar = (
            "&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)"
        )
        INPUT_SPECS: ClassVar = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_static_method_func(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::get static method (NAME) of (CLASS) as function"
        INPUT_SPECS: ClassVar = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS: ClassVar = ()
        name: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_setter_value(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::operator value {{id=gceOOP_defineSetterValue}}"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_class_property(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::#menu:classProperty"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_operator_method(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::#menu:operatorMethod"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()

    @grepr_dataclass()
    class menu_special_method(ThirdBlock):
        OPCODE: ClassVar = "&gceOOP::#menu:specialMethod"
        INPUT_SPECS: ClassVar = ()
        DROPDOWN_SPECS: ClassVar = ()
