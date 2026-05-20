from __future__ import annotations
import pmp_manip as p
from third import ThirdInputValue, ThirdBlock, INPUT_COMPATIBLE_T


class gceOOP:

    class temp_block(ThirdBlock):

        def __init__(self, instance: INPUT_COMPATIBLE_T):
            self.instance = instance

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::temp block with (INSTANCE) end",
                inputs={
                    "INSTANCE": ThirdInputValue.as_input(
                        self.instance, p.SRBlockOnlyInputValue
                    )
                },
                dropdowns={},
            )

    class temp_block2(ThirdBlock):

        def __init__(self, a: INPUT_COMPATIBLE_T, b: INPUT_COMPATIBLE_T):
            self.a = a
            self.b = b

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::temp command with (A) and (B)",
                inputs={
                    "A": ThirdInputValue.as_input(self.a, p.SRBlockOnlyInputValue),
                    "B": ThirdInputValue.as_input(self.b, p.SRBlockOnlyInputValue),
                },
                dropdowns={},
            )

    class create_class_at(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::create class at var (NAME) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.current_class()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class create_subclass_at(ThirdBlock):

        def __init__(
            self,
            name: INPUT_COMPATIBLE_T,
            superclass: INPUT_COMPATIBLE_T,
            substack: INPUT_COMPATIBLE_T,
        ):
            self.name = name
            self.superclass = superclass
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::create subclass at var (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SUPERCLASS": ThirdInputValue.as_input(
                        self.superclass, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.current_class()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class create_class_named(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::create class named (NAME) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.current_class()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class create_subclass_named(ThirdBlock):

        def __init__(
            self,
            name: INPUT_COMPATIBLE_T,
            superclass: INPUT_COMPATIBLE_T,
            substack: INPUT_COMPATIBLE_T,
        ):
            self.name = name
            self.superclass = superclass
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::create subclass named (NAME) with superclass (SUPERCLASS) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SUPERCLASS": ThirdInputValue.as_input(
                        self.superclass, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.current_class()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class on_class(ThirdBlock):

        def __init__(self, class_: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.class_ = class_
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on class (CLASS) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.current_class()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class current_class(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&gceOOP::current class", inputs={}, dropdowns={})

    class is_subclass(ThirdBlock):

        def __init__(
            self, subclass: INPUT_COMPATIBLE_T, superclass: INPUT_COMPATIBLE_T
        ):
            self.subclass = subclass
            self.superclass = superclass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::is (SUBCLASS) a subclass of (SUPERCLASS) ?",
                inputs={
                    "SUBCLASS": ThirdInputValue.as_input(
                        self.subclass, p.SRBlockAndTextInputValue
                    ),
                    "SUPERCLASS": ThirdInputValue.as_input(
                        self.superclass, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_superclass(ThirdBlock):

        def __init__(self, class_: INPUT_COMPATIBLE_T):
            self.class_ = class_

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::get superclass of (CLASS)",
                inputs={
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class define_instance_method(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::define instance method (NAME) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.self_value()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class define_special_method(ThirdBlock):

        def __init__(
            self, special_method: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
        ):
            self.special_method = special_method
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::define ([SPECIAL_METHOD]) instance method {:SHADOW:} {SUBSTACK}",
                inputs={
                    "SPECIAL_METHOD": ThirdInputValue.as_input(
                        self.special_method, p.SRBlockAndDropdownInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.self_value()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class self_value(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(opcode="&gceOOP::self", inputs={}, dropdowns={})

    class call_super_method(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T):
            self.name = name
            self.posargs = posargs

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::call super method (NAME) with positional args (POSARGS)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "POSARGS": ThirdInputValue.as_input(
                        self.posargs, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class call_super_init_method(ThirdBlock):

        def __init__(self, posargs: INPUT_COMPATIBLE_T):
            self.posargs = posargs

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::call super init method with positional args (POSARGS)",
                inputs={
                    "POSARGS": ThirdInputValue.as_input(
                        self.posargs, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class define_getter(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::define getter for (NAME) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.self_value()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class define_setter(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::define setter for (NAME) {:SHADOW1:} {:SHADOW2:} {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SHADOW1": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.self_value()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SHADOW2": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.define_setter_value()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class define_operator_method(ThirdBlock):

        def __init__(
            self, operator_kind: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T
        ):
            self.operator_kind = operator_kind
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::define operator method ([OPERATOR_KIND]) {:SHADOW:} {SUBSTACK}",
                inputs={
                    "OPERATOR_KIND": ThirdInputValue.as_input(
                        self.operator_kind, p.SRBlockAndDropdownInputValue
                    ),
                    "SHADOW": ThirdInputValue.as_input(
                        ThirdInputValue(gceOOP.operator_operator_value()),
                        p.SREmbeddedBlockInputValue,
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class operator_operator_value(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::operator value {{id=gceOOP_operatorOperatorValue}}",
                inputs={},
                dropdowns={},
            )

    class set_class_variable(ThirdBlock):

        def __init__(
            self,
            class_: INPUT_COMPATIBLE_T,
            name: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.class_ = class_
            self.name = name
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on (CLASS) set class var (NAME) to (VALUE)",
                inputs={
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_class_variable(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T):
            self.name = name
            self.class_ = class_

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on (CLASS) get class var (NAME)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class delete_class_variable(ThirdBlock):

        def __init__(self, class_: INPUT_COMPATIBLE_T, name: INPUT_COMPATIBLE_T):
            self.class_ = class_
            self.name = name

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on (CLASS) delete class var (NAME)",
                inputs={
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class define_static_method(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, substack: INPUT_COMPATIBLE_T):
            self.name = name
            self.substack = substack

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::define static method (NAME) {SUBSTACK}",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "SUBSTACK": ThirdInputValue.as_input(
                        self.substack, p.SRScriptInputValue
                    ),
                },
                dropdowns={},
            )

    class property_names_of_class(ThirdBlock):

        def __init__(self, property: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T):
            self.property = property
            self.class_ = class_

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::([PROPERTY]) names of class (CLASS)",
                inputs={
                    "PROPERTY": ThirdInputValue.as_input(
                        self.property, p.SRBlockAndDropdownInputValue
                    ),
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class create_instance(ThirdBlock):

        def __init__(self, class_: INPUT_COMPATIBLE_T, posargs: INPUT_COMPATIBLE_T):
            self.class_ = class_
            self.posargs = posargs

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::create instance of class (CLASS) with positional args (POSARGS)",
                inputs={
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                    "POSARGS": ThirdInputValue.as_input(
                        self.posargs, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class is_instance(ThirdBlock):

        def __init__(
            self, potential_instance: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T
        ):
            self.potential_instance = potential_instance
            self.class_ = class_

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::is (POTENTIAL_INSTANCE) an instance of (CLASS) ?",
                inputs={
                    "POTENTIAL_INSTANCE": ThirdInputValue.as_input(
                        self.potential_instance, p.SRBlockAndTextInputValue
                    ),
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_class_of_instance(ThirdBlock):

        def __init__(self, instance: INPUT_COMPATIBLE_T):
            self.instance = instance

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::get class of (INSTANCE)",
                inputs={
                    "INSTANCE": ThirdInputValue.as_input(
                        self.instance, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class set_attribute(ThirdBlock):

        def __init__(
            self,
            instance: INPUT_COMPATIBLE_T,
            name: INPUT_COMPATIBLE_T,
            value: INPUT_COMPATIBLE_T,
        ):
            self.instance = instance
            self.name = name
            self.value = value

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on (INSTANCE) set attribute (NAME) to (VALUE)",
                inputs={
                    "INSTANCE": ThirdInputValue.as_input(
                        self.instance, p.SRBlockAndTextInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "VALUE": ThirdInputValue.as_input(
                        self.value, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_attribute(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, instance: INPUT_COMPATIBLE_T):
            self.name = name
            self.instance = instance

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on (INSTANCE) get attribute (NAME)",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "INSTANCE": ThirdInputValue.as_input(
                        self.instance, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_all_attributes(ThirdBlock):

        def __init__(self, instance: INPUT_COMPATIBLE_T):
            self.instance = instance

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::all attributes of (INSTANCE)",
                inputs={
                    "INSTANCE": ThirdInputValue.as_input(
                        self.instance, p.SRBlockAndTextInputValue
                    )
                },
                dropdowns={},
            )

    class call_method(ThirdBlock):

        def __init__(
            self,
            instance: INPUT_COMPATIBLE_T,
            name: INPUT_COMPATIBLE_T,
            posargs: INPUT_COMPATIBLE_T,
        ):
            self.instance = instance
            self.name = name
            self.posargs = posargs

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on (INSTANCE) call method (NAME) with positional args (POSARGS)",
                inputs={
                    "INSTANCE": ThirdInputValue.as_input(
                        self.instance, p.SRBlockAndTextInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "POSARGS": ThirdInputValue.as_input(
                        self.posargs, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class call_static_method(ThirdBlock):

        def __init__(
            self,
            class_: INPUT_COMPATIBLE_T,
            name: INPUT_COMPATIBLE_T,
            posargs: INPUT_COMPATIBLE_T,
        ):
            self.class_ = class_
            self.name = name
            self.posargs = posargs

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::on (CLASS) call static method (NAME) with positional args (POSARGS)",
                inputs={
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "POSARGS": ThirdInputValue.as_input(
                        self.posargs, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class get_static_method_func(ThirdBlock):

        def __init__(self, name: INPUT_COMPATIBLE_T, class_: INPUT_COMPATIBLE_T):
            self.name = name
            self.class_ = class_

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::get static method (NAME) of (CLASS) as function",
                inputs={
                    "NAME": ThirdInputValue.as_input(
                        self.name, p.SRBlockAndTextInputValue
                    ),
                    "CLASS": ThirdInputValue.as_input(
                        self.class_, p.SRBlockAndTextInputValue
                    ),
                },
                dropdowns={},
            )

    class define_setter_value(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::operator value {{id=gceOOP_defineSetterValue}}",
                inputs={},
                dropdowns={},
            )

    class menu_class_property(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::#menu:classProperty", inputs={}, dropdowns={}
            )

    class menu_operator_method(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::#menu:operatorMethod", inputs={}, dropdowns={}
            )

    class menu_special_method(ThirdBlock):

        def __init__(self):
            pass

        def to_second(self) -> p.SRBlock:
            return p.SRBlock(
                opcode="&gceOOP::#menu:specialMethod", inputs={}, dropdowns={}
            )
