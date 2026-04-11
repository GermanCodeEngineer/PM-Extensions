from __future__ import annotations
import pmp_manip as p
from utils import InputValue, INPUT_COMPATIBLE_T


class gceClassesOOP:

    @staticmethod
    def log_stacks() -> p.SRBlock:
        return p.SRBlock(opcode="&gceClassesOOP::logStacks", inputs={}, dropdowns={})

    @staticmethod
    def set_scope_var(name: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::set var (NAME) to (VALUE) in current scope",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_scope_var(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::get var (NAME)",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def scope_var_exists(name: INPUT_COMPATIBLE_T, kind: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::var (NAME) exists in [KIND]?",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={"KIND": p.SRDropdownValue(p.DropdownValueKind.STANDARD, kind)},
        )

    @staticmethod
    def delete_scope_var(name: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::delete var (NAME) in current scope",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def all_variables(kind: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::all variables in [KIND]",
            inputs={},
            dropdowns={"KIND": p.SRDropdownValue(p.DropdownValueKind.STANDARD, kind)},
        )

    @staticmethod
    def create_var_scope(substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::create local variable scope {SUBSTACK}",
            inputs={
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def bind_var_to_scope(name: INPUT_COMPATIBLE_T, kind: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::bind [KIND] variable (NAME) to current scope",
            inputs={"NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue)},
            dropdowns={"KIND": p.SRDropdownValue(p.DropdownValueKind.STANDARD, kind)},
        )

    @staticmethod
    def create_class_at(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.class_being_created()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
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
            opcode="&gceClassesOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUPERCLASS": InputValue.try_as_input(
                    superclass, p.SRBlockAndTextInputValue
                ),
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.class_being_created()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_class_named(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.class_being_created()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
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
            opcode="&gceClassesOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUPERCLASS": InputValue.try_as_input(
                    superclass, p.SRBlockAndTextInputValue
                ),
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.class_being_created()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def on_class(class_: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
            inputs={
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.class_being_created()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def class_being_created() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::class being created", inputs={}, dropdowns={}
        )

    @staticmethod
    def is_subclass(
        subclass: INPUT_COMPATIBLE_T, superclass: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?",
            inputs={
                "SUBCLASS": InputValue.try_as_input(
                    subclass, p.SRBlockAndTextInputValue
                ),
                "SUPERCLASS": InputValue.try_as_input(
                    superclass, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def get_superclass(class_: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::get superclass of (CLASS)",
            inputs={
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def define_instance_method(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.self()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_special_method(
        substack: INPUT_COMPATIBLE_T, special_method: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::define [SPECIAL_METHOD] instance method {:SHADOW:} {SUBSTACK}",
            inputs={
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.self()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={
                "SPECIAL_METHOD": p.SRDropdownValue(
                    p.DropdownValueKind.STANDARD, special_method
                )
            },
        )

    @staticmethod
    def self() -> p.SRBlock:
        return p.SRBlock(opcode="&gceClassesOOP::self", inputs={}, dropdowns={})

    @staticmethod
    def call_super_method(
        name: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::call super method (NAME) with positional args (POSARGS)",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "POSARGS": InputValue.try_as_input(posargs, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def call_super_init_method(posargs: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::call super init method with positional args (POSARGS)",
            inputs={
                "POSARGS": InputValue.try_as_input(posargs, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def define_getter(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::define getter (NAME) {:SHADOW:} {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.self()), p.SREmbeddedBlockInputValue
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_setter(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::define setter (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SHADOW1": InputValue.try_as_input(
                    InputValue(gceClassesOOP.self()), p.SREmbeddedBlockInputValue
                ),
                "SHADOW2": InputValue.try_as_input(
                    InputValue(gceClassesOOP.define_setter_value()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_setter_value() -> p.SRBlock:
        return p.SRBlock(opcode="&gceClassesOOP::value", inputs={}, dropdowns={})

    @staticmethod
    def define_operator_method(
        substack: INPUT_COMPATIBLE_T, operator_kind: str
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::define operator method [OPERATOR_KIND] {:SHADOW:} {SUBSTACK}",
            inputs={
                "SHADOW": InputValue.try_as_input(
                    InputValue(gceClassesOOP.operator_other_value()),
                    p.SREmbeddedBlockInputValue,
                ),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={
                "OPERATOR_KIND": p.SRDropdownValue(
                    p.DropdownValueKind.STANDARD, operator_kind
                )
            },
        )

    @staticmethod
    def operator_other_value() -> p.SRBlock:
        return p.SRBlock(opcode="&gceClassesOOP::other value", inputs={}, dropdowns={})

    @staticmethod
    def set_class_variable(
        class_: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T, value: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::on (CLASS) set class variable (NAME) to (VALUE)",
            inputs={
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_class_variable(
        name: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::get class variable (NAME) of (CLASS)",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def delete_class_variable(
        class_: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::on (CLASS) delete class variable (NAME)",
            inputs={
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def define_static_method(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::define static method (NAME) {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def property_names_of_class(class_: INPUT_COMPATIBLE_T, property: str) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::[PROPERTY] names of class (CLASS)",
            inputs={
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue)
            },
            dropdowns={
                "PROPERTY": p.SRDropdownValue(p.DropdownValueKind.STANDARD, property)
            },
        )

    @staticmethod
    def create_instance(
        class_: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::create instance of class (CLASS) with positional args (POSARGS)",
            inputs={
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
                "POSARGS": InputValue.try_as_input(posargs, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def is_instance(
        instance: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::is (INSTANCE) an instance of (CLASS) ?",
            inputs={
                "INSTANCE": InputValue.try_as_input(
                    instance, p.SRBlockAndTextInputValue
                ),
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_class_of_instance(instance: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::get class of (INSTANCE)",
            inputs={
                "INSTANCE": InputValue.try_as_input(
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
            opcode="&gceClassesOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
            inputs={
                "INSTANCE": InputValue.try_as_input(
                    instance, p.SRBlockAndTextInputValue
                ),
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_attribute(
        name: INPUT_COMPATIBLE_T, instance: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::attribute (NAME) of (INSTANCE)",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "INSTANCE": InputValue.try_as_input(
                    instance, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def get_all_attributes(instance: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::all attributes of (INSTANCE)",
            inputs={
                "INSTANCE": InputValue.try_as_input(
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
            opcode="&gceClassesOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
            inputs={
                "INSTANCE": InputValue.try_as_input(
                    instance, p.SRBlockAndTextInputValue
                ),
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "POSARGS": InputValue.try_as_input(posargs, p.SRBlockAndTextInputValue),
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
            opcode="&gceClassesOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
            inputs={
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "POSARGS": InputValue.try_as_input(posargs, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def get_static_method_func(
        name: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::get static method (NAME) of (CLASS) as function",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "CLASS": InputValue.try_as_input(class_, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def configure_next_function_args(
        argnames: INPUT_COMPATIBLE_T, argdefaults: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::configure next function: argument names (ARGNAMES) defaults (ARGDEFAULTS)",
            inputs={
                "ARGNAMES": InputValue.try_as_input(
                    argnames, p.SRBlockAndTextInputValue
                ),
                "ARGDEFAULTS": InputValue.try_as_input(
                    argdefaults, p.SRBlockAndTextInputValue
                ),
            },
            dropdowns={},
        )

    @staticmethod
    def create_function_at(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::create function at var (NAME) {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def create_function_named(
        name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::create function named (NAME) {SUBSTACK}",
            inputs={
                "NAME": InputValue.try_as_input(name, p.SRBlockAndTextInputValue),
                "SUBSTACK": InputValue.try_as_input(substack, p.SRScriptInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def return_(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::return (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def call_function(
        func: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::call function (FUNC) with positional args (POSARGS)",
            inputs={
                "FUNC": InputValue.try_as_input(func, p.SRBlockAndTextInputValue),
                "POSARGS": InputValue.try_as_input(posargs, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def object_as_string(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::(VALUE) as string",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def typeof(value: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::typeof (VALUE)",
            inputs={
                "VALUE": InputValue.try_as_input(value, p.SRBlockAndTextInputValue)
            },
            dropdowns={},
        )

    @staticmethod
    def check_identity(
        value1: INPUT_COMPATIBLE_T, value2: INPUT_COMPATIBLE_T
    ) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::(VALUE1) is (VALUE2) ?",
            inputs={
                "VALUE1": InputValue.try_as_input(value1, p.SRBlockAndTextInputValue),
                "VALUE2": InputValue.try_as_input(value2, p.SRBlockAndTextInputValue),
            },
            dropdowns={},
        )

    @staticmethod
    def nothing() -> p.SRBlock:
        return p.SRBlock(opcode="&gceClassesOOP::Nothing", inputs={}, dropdowns={})

    @staticmethod
    def execute_expression(expr: INPUT_COMPATIBLE_T) -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::execute expression (EXPR)",
            inputs={"EXPR": InputValue.try_as_input(expr, p.SRBlockAndTextInputValue)},
            dropdowns={},
        )

    @staticmethod
    def menu_variable_available_kind() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::#menu:variableAvailableKind",
            inputs={},
            dropdowns={},
        )

    @staticmethod
    def menu_bind_var_origin_kind() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::#menu:bindVarOriginKind", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_class_property() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::#menu:classProperty", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_operator_method() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::#menu:operatorMethod", inputs={}, dropdowns={}
        )

    @staticmethod
    def menu_special_method() -> p.SRBlock:
        return p.SRBlock(
            opcode="&gceClassesOOP::#menu:specialMethod", inputs={}, dropdowns={}
        )
