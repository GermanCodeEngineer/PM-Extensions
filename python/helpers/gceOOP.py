from __future__ import annotations
from gceutils import grepr_dataclass
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class gceOOP:

    @grepr_dataclass()
    class temp_block(ThirdBlock):
        OPCODE = "&gceOOP::temp block with (INSTANCE) end"
        INPUT_SPECS = (("INSTANCE", "instance", p.SRBlockOnlyInputValue, None),)
        DROPDOWN_SPECS = ()
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class temp_block2(ThirdBlock):
        OPCODE = "&gceOOP::temp command with (A) and (B)"
        INPUT_SPECS = (
            ("A", "a", p.SRBlockOnlyInputValue, None),
            ("B", "b", p.SRBlockOnlyInputValue, None),
        )
        DROPDOWN_SPECS = ()
        a: INPUT_COMPATIBLE_T
        b: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_class_at(ThirdBlock):
        OPCODE = "&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.current_class),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_subclass_at(ThirdBlock):
        OPCODE = "&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.current_class),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_class_named(ThirdBlock):
        OPCODE = "&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.current_class),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_subclass_named(ThirdBlock):
        OPCODE = "&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.current_class),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class on_class(ThirdBlock):
        OPCODE = "&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.current_class),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        class_: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class current_class(ThirdBlock):
        OPCODE = "&gceOOP::current class"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class is_subclass(ThirdBlock):
        OPCODE = "&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?"
        INPUT_SPECS = (
            ("SUBCLASS", "subclass", p.SRBlockAndTextInputValue, None),
            ("SUPERCLASS", "superclass", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        subclass: INPUT_COMPATIBLE_T
        superclass: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_superclass(ThirdBlock):
        OPCODE = "&gceOOP::get superclass of (CLASS)"
        INPUT_SPECS = (("CLASS", "class_", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_instance_method(ThirdBlock):
        OPCODE = "&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.self_value),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_special_method(ThirdBlock):
        OPCODE = (
            "&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}"
        )
        INPUT_SPECS = (
            ("SPECIAL_METHOD", "special_method", p.SRBlockAndDropdownInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.self_value),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        special_method: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class self_value(ThirdBlock):
        OPCODE = "&gceOOP::self"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class call_super_method(ThirdBlock):
        OPCODE = "&gceOOP::call super method (NAME) with positional args (POSARGS)"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_super_init_method(ThirdBlock):
        OPCODE = "&gceOOP::call super init method with positional args (POSARGS)"
        INPUT_SPECS = (("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_getter(ThirdBlock):
        OPCODE = "&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SHADOW", "shadow", p.SREmbeddedBlockInputValue, gceOOP.self_value),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_setter(ThirdBlock):
        OPCODE = "&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SHADOW1", "shadow1", p.SREmbeddedBlockInputValue, gceOOP.self_value),
            (
                "SHADOW2",
                "shadow2",
                p.SREmbeddedBlockInputValue,
                gceOOP.define_setter_value,
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_operator_method(ThirdBlock):
        OPCODE = (
            "&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}"
        )
        INPUT_SPECS = (
            ("OPERATOR_KIND", "operator_kind", p.SRBlockAndDropdownInputValue, None),
            (
                "SHADOW",
                "shadow",
                p.SREmbeddedBlockInputValue,
                gceOOP.operator_operator_value,
            ),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        operator_kind: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class operator_operator_value(ThirdBlock):
        OPCODE = "&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class set_class_variable(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) set class var (NAME) to (VALUE)"
        INPUT_SPECS = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_class_variable(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) get class var (NAME)"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class delete_class_variable(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) delete class var (NAME)"
        INPUT_SPECS = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_static_method(ThirdBlock):
        OPCODE = "&gceOOP::define static method (NAME) {SUBSTACK}"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("SUBSTACK", "substack", p.SRScriptInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        substack: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class property_names_of_class(ThirdBlock):
        OPCODE = "&gceOOP::([PROPERTY]) names of class (CLASS)"
        INPUT_SPECS = (
            ("PROPERTY", "property", p.SRBlockAndDropdownInputValue, None),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        property: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class create_instance(ThirdBlock):
        OPCODE = (
            "&gceOOP::create instance of class (CLASS) with positional args (POSARGS)"
        )
        INPUT_SPECS = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        class_: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class is_instance(ThirdBlock):
        OPCODE = "&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?"
        INPUT_SPECS = (
            (
                "POTENTIAL_INSTANCE",
                "potential_instance",
                p.SRBlockAndTextInputValue,
                None,
            ),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        potential_instance: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_class_of_instance(ThirdBlock):
        OPCODE = "&gceOOP::get class of (INSTANCE)"
        INPUT_SPECS = (("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class set_attribute(ThirdBlock):
        OPCODE = "&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)"
        INPUT_SPECS = (
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("VALUE", "value", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        instance: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        value: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_attribute(ThirdBlock):
        OPCODE = "&gceOOP::on (INSTANCE) get attribute (NAME)"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_all_attributes(ThirdBlock):
        OPCODE = "&gceOOP::all attributes of (INSTANCE)"
        INPUT_SPECS = (("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),)
        DROPDOWN_SPECS = ()
        instance: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_method(ThirdBlock):
        OPCODE = (
            "&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)"
        )
        INPUT_SPECS = (
            ("INSTANCE", "instance", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        instance: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class call_static_method(ThirdBlock):
        OPCODE = "&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)"
        INPUT_SPECS = (
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("POSARGS", "posargs", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        class_: INPUT_COMPATIBLE_T
        name: INPUT_COMPATIBLE_T
        posargs: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class get_static_method_func(ThirdBlock):
        OPCODE = "&gceOOP::get static method (NAME) of (CLASS) as function"
        INPUT_SPECS = (
            ("NAME", "name", p.SRBlockAndTextInputValue, None),
            ("CLASS", "class_", p.SRBlockAndTextInputValue, None),
        )
        DROPDOWN_SPECS = ()
        name: INPUT_COMPATIBLE_T
        class_: INPUT_COMPATIBLE_T

    @grepr_dataclass()
    class define_setter_value(ThirdBlock):
        OPCODE = "&gceOOP::operator value {{id=gceOOP_defineSetterValue}}"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_class_property(ThirdBlock):
        OPCODE = "&gceOOP::#menu:classProperty"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_operator_method(ThirdBlock):
        OPCODE = "&gceOOP::#menu:operatorMethod"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()

    @grepr_dataclass()
    class menu_special_method(ThirdBlock):
        OPCODE = "&gceOOP::#menu:specialMethod"
        INPUT_SPECS = ()
        DROPDOWN_SPECS = ()
