from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, INPUT_COMPATIBLE_T


class gceOOP:

    @staticmethod
    def temp_block(instance: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::temp block with (INSTANCE) end",
            inputs={
                "INSTANCE": ThirdInputValue.as_input(instance, p.SRBlockOnlyInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def temp_block2(a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::temp command with (A) and (B)",
            inputs={
                "A": ThirdInputValue.as_input(a, p.SRBlockOnlyInputValue),
                "B": ThirdInputValue.as_input(b, p.SRBlockOnlyInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_class_at(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.current_class()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_subclass_at(
        name: INPUT_COMPATIBLE_T,
        superclass: INPUT_COMPATIBLE_T,
        substack: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SUPERCLASS": ThirdInputValue.as_input(
                    superclass, p.SRBlockAndTextInputValue
                ),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.current_class()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_class_named(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.current_class()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_subclass_named(
        name: INPUT_COMPATIBLE_T,
        superclass: INPUT_COMPATIBLE_T,
        substack: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SUPERCLASS": ThirdInputValue.as_input(
                    superclass, p.SRBlockAndTextInputValue
                ),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.current_class()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def on_class(class_: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
            inputs={
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.current_class()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def current_class() -> p.SRBlock:
        return p.SRBlock(opcode="&gceOOP::current class", inputs={}, dropdowns={})

    @staticmethod
    def is_subclass(
        subclass: INPUT_COMPATIBLE_T, superclass: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?",
            inputs={
                "SUBCLASS": ThirdInputValue.as_input(
                    subclass, p.SRBlockAndTextInputValue
                ),
                "SUPERCLASS": ThirdInputValue.as_input(
                    superclass, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def get_superclass(class_: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::get superclass of (CLASS)",
            inputs={
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def define_instance_method(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.self_value()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_special_method(
        special_method: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
            inputs={
                "SPECIAL_METHOD": ThirdInputValue.as_input(
                    special_method, p.SRBlockAndDropdownInputValue
                ),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.self_value()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def self_value() -> p.SRBlock:
        return p.SRBlock(opcode="&gceOOP::self", inputs={}, dropdowns={})

    @staticmethod
    def call_super_method(
        name: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::call super method (NAME) with positional args (POSARGS)",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "POSARGS": ThirdInputValue.as_input(
                    posargs, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def call_super_init_method(posargs: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::call super init method with positional args (POSARGS)",
            inputs={
                "POSARGS": ThirdInputValue.as_input(posargs, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def define_getter(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.self_value()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_setter(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW1": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.self_value()), p.SREmbeddedBlockInputValue
                ),
                "SHADOW2": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.define_setter_value()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_operator_method(
        operator_kind: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
            inputs={
                "OPERATOR_KIND": ThirdInputValue.as_input(
                    operator_kind, p.SRBlockAndDropdownInputValue
                ),
                "SHADOW": ThirdInputValue.as_input(
                    ThirdInputValue(gceOOP.operator_operator_value()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def operator_operator_value() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def set_class_variable(
        class_: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
            inputs={
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_class_variable(
        name: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on (CLASS) get class var (NAME)",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete_class_variable(
        class_: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on (CLASS) delete class var (NAME)",
            inputs={
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_static_method(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::define static method (NAME) {SUBSTACK}",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": ThirdInputValue.as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def property_names_of_class(
        property: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::([PROPERTY]) names of class (CLASS)",
            inputs={
                "PROPERTY": ThirdInputValue.as_input(
                    property, p.SRBlockAndDropdownInputValue
                ),
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_instance(
        class_: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)",
            inputs={
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
                "POSARGS": ThirdInputValue.as_input(
                    posargs, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def is_instance(
        potential_instance: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
            inputs={
                "POTENTIAL_INSTANCE": ThirdInputValue.as_input(
                    potential_instance, p.SRBlockAndTextInputValue
                ),
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_class_of_instance(instance: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::get class of (INSTANCE)",
            inputs={
                "INSTANCE": ThirdInputValue.as_input(
                    instance, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def set_attribute(
        instance: INPUT_COMPATIBLE_T,
        name: INPUT_COMPATIBLE_T,
        value: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
            inputs={
                "INSTANCE": ThirdInputValue.as_input(
                    instance, p.SRBlockAndTextInputValue
                ),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": ThirdInputValue.as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_attribute(
        name: INPUT_COMPATIBLE_T, instance: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on (INSTANCE) get attribute (NAME)",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "INSTANCE": ThirdInputValue.as_input(
                    instance, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def get_all_attributes(instance: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::all attributes of (INSTANCE)",
            inputs={
                "INSTANCE": ThirdInputValue.as_input(
                    instance, p.SRBlockAndTextInputValue
                )
            },
            dropdowns={},
        )

    @staticmethod
    def call_method(
        instance: INPUT_COMPATIBLE_T,
        name: INPUT_COMPATIBLE_T,
        posargs: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
            inputs={
                "INSTANCE": ThirdInputValue.as_input(
                    instance, p.SRBlockAndTextInputValue
                ),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "POSARGS": ThirdInputValue.as_input(
                    posargs, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def call_static_method(
        class_: INPUT_COMPATIBLE_T,
        name: INPUT_COMPATIBLE_T,
        posargs: INPUT_COMPATIBLE_T,
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
            inputs={
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "POSARGS": ThirdInputValue.as_input(
                    posargs, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def get_static_method_func(
        name: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::get static method (NAME) of (CLASS) as function",
            inputs={
                "NAME": ThirdInputValue.as_input(name, p.SRBlockAndTextInputValue),
                "CLASS": ThirdInputValue.as_input(class_, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_setter_value() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::operator value {{id=gceOOP_defineSetterValue}}",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def menu_class_property() -> p.SRBlock:
        return p.SRBlock(opcode="&gceOOP::#menu:classProperty", inputs={}, dropdowns={})

    @staticmethod
    def menu_operator_method() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceOOP::#menu:operatorMethod", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_special_method() -> p.SRBlock:
        return p.SRBlock(opcode="&gceOOP::#menu:specialMethod", inputs={}, dropdowns={})
