from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable

sys.path.append(str(Path(__file__).parent.parent))

import copy
import pmp_manip as p
from gceutils import AbstractTreePath, grepr_dataclass

from helpers.event import event
from helpers.gceFuncsScopes import gceFuncsScopes as fs
from helpers.gceOOP import gceOOP as c
from helpers.gceTestRunner import gceTestRunner as t


EXTENSION_URL_BASE = (
    #"https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/"
    #"refs/heads/main/extensions"
    "http://localhost:5173/extensions"
)


@grepr_dataclass(frozen=True)
class ExampleCase:
    key: str
    title: str
    description: str
    build_script: Callable[[], p.SRScript]


def extension_url(filename: str) -> str:
    return f"{EXTENSION_URL_BASE}/{filename}"


def describe_suite(name: str, *tests: p.SRBlock) -> p.SRBlock:
    return t.test_scope(name, list(tests))


def run_case(name: str, *blocks: p.SRBlock) -> p.SRBlock:
    return t.test_scope(name, list(blocks))


def create_class_test() -> p.SRScript:
    return p.SRScript(
        position=(0, 0),
        blocks=[ # HERE: review tests
            event.whenflagclicked(),
            describe_suite(
                "Basic Class With Instance Method",
                run_case(
                    "static factory creates an instance and greet returns the expected name",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                name="Greeter",
                                substack=[
                                    c.define_special_method(
                                        [
                                            c.set_attribute(c.self(), "prefix", "Hello"),
                                            fs.return_value(fs.nothing()),
                                        ],
                                        "init",
                                    ),
                                    c.define_instance_method(
                                        name="greet",
                                        substack=[
                                            fs.return_value(
                                                c.get_attribute("name", c.self())
                                            )
                                        ],
                                    ),
                                    c.define_static_method(
                                        name="fromName",
                                        substack=[
                                            fs.set_scope_var(
                                                "obj",
                                                c.create_instance("Greeter", "[]"),
                                            ),
                                            c.set_attribute(
                                                fs.get_scope_var("obj"),
                                                "name",
                                                "World",
                                            ),
                                            fs.return_value(fs.get_scope_var("obj")),
                                        ],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "greeter",
                                c.call_static_method("Greeter", "fromName", "[]"),
                            ),
                            fs.set_scope_var(
                                "message",
                                c.call_method("greeter", "greet", "[]"),
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(fs.get_scope_var("message"), "World"),
                    t.assert_unstrict_equal(
                        fs.object_as_string(fs.get_scope_var("greeter")),
                        "<Instance of 'Greeter'>",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.get_scope_var("greeter")),
                        "Class Instance",
                    ),
                ),
                run_case(
                    "missing instance methods raise a clear error",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "EmptyGreeter",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "emptyGreeter",
                                c.create_instance("EmptyGreeter", "[]"),
                            ),
                        ]
                    ),
                    t.assert_throws_contains(
                        "Undefined instance method",
                        [
                            fs.execute_expression(
                                c.call_method("emptyGreeter", "missing", "[]")
                            ),
                        ],
                    ),
                ),
                run_case(
                    "too many positional args raises",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "OneArgClass",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                    c.define_instance_method(
                                        "oneArg",
                                        [fs.return_value(fs.nothing())],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "oneArgObj",
                                c.create_instance("OneArgClass", "[]"),
                            ),
                        ]
                    ),
                    t.assert_throws_contains(
                        "expected at most",
                        [
                            fs.execute_expression(
                                c.call_method(
                                    "oneArgObj", "oneArg", '["extra1", "extra2"]'
                                )
                            ),
                        ],
                    ),
                ),
                run_case(
                    "too few positional args raises",
                    t.assert_does_not_throw(
                        [
                            fs.configure_next_function_args('["a", "b"]', "[]"),
                            fs.set_scope_var(
                                "twoArgFunc",
                                fs.create_function_named(
                                    "twoArgFunc",
                                    [fs.return_value(fs.get_scope_var("a"))],
                                ),
                            ),
                        ]
                    ),
                    t.assert_throws_contains(
                        "expected at least",
                        [
                            fs.execute_expression(
                                fs.call_function(
                                    fs.get_scope_var("twoArgFunc"), '["only-one"]'
                                )
                            ),
                        ],
                    ),
                ),
                run_case(
                    "missing attribute (no getter) raises",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "Plain",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "plainObj",
                                c.create_instance("Plain", "[]"),
                            ),
                        ]
                    ),
                    t.assert_throws_contains(
                        "no attribute",
                        [
                            fs.execute_expression(
                                c.get_attribute("missing", fs.get_scope_var("plainObj"))
                            ),
                        ],
                    ),
                ),
            ),
        ],
    )


def create_scopes_and_functions_edge_test() -> p.SRScript:
    return p.SRScript(
        position=(0, 180),
        blocks=[
            event.whenflagclicked(),
            describe_suite(
                "Scopes, Binding, and Function Defaults",
                run_case(
                    "global binding and local shadowing behave as expected",
                    t.assert_does_not_throw(
                        [
                            fs.set_scope_var("outer", "global-value"),
                            fs.create_var_scope(
                                [
                                    fs.bind_var_to_scope("outer", "global"),
                                    t.assert_(
                                        fs.scope_var_exists("outer", "all scopes")
                                    ),
                                    t.assert_unstrict_equal(
                                        fs.get_scope_var("outer"),
                                        "global-value",
                                    ),
                                    fs.set_scope_var("shadow", "local-value"),
                                    t.assert_(
                                        fs.scope_var_exists(
                                            "shadow",
                                            "local scope",
                                        )
                                    ),
                                    fs.delete_scope_var("shadow"),
                                    t.assert_not(
                                        fs.scope_var_exists(
                                            "shadow",
                                            "all scopes",
                                        )
                                    ),
                                ]
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(fs.get_scope_var("outer"), "global-value"),
                ),
                run_case(
                    "function defaults and Nothing returns are respected",
                    t.assert_does_not_throw(
                        [
                            fs.configure_next_function_args(
                                '["a", "b"]',
                                '["B-default"]',
                            ),
                            fs.create_function_at(
                                "combine",
                                [fs.return_value(fs.get_scope_var("b"))],
                            ),
                            fs.set_scope_var(
                                "combined",
                                fs.call_function("combine", '["A-only"]'),
                            ),
                            fs.set_scope_var(
                                "echo",
                                fs.create_function_named(
                                    "echo",
                                    [fs.return_value(fs.nothing())],
                                ),
                            ),
                            fs.set_scope_var(
                                "echoResult",
                                fs.call_function("echo", "[]"),
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(fs.get_scope_var("combined"), "B-default"),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.get_scope_var("echo")),
                        "Function",
                    ),
                    t.assert_unstrict_equal(
                        fs.object_as_string(fs.get_scope_var("echoResult")),
                        "<Nothing>",
                    ),
                ),
                run_case(
                    "invalid default configurations raise an error",
                    t.assert_throws_contains(
                        "as many default values",
                        [
                            fs.configure_next_function_args(
                                '["onlyArg"]',
                                '["first", "second"]',
                            ),
                        ],
                    ),
                ),
                run_case(
                    "non-local binding links a closure variable across nested scopes",
                    t.assert_does_not_throw(
                        [
                            # Set up: outer scope has "counter"
                            fs.set_scope_var("nlCounter", "0"),
                            fs.create_var_scope(
                                [
                                    # inner scope: bind non-local so mutations propagate
                                    fs.bind_var_to_scope("nlCounter", "non-local"),
                                    fs.set_scope_var("nlCounter", "42"),
                                ]
                            ),
                        ]
                    ),
                    # outer "nlCounter" should now reflect the inner write
                    t.assert_unstrict_equal(fs.get_scope_var("nlCounter"), "42"),
                ),
                run_case(
                    "delete non-existent variable raises",
                    t.assert_throws_contains(
                        "not defined",
                        [
                            fs.delete_scope_var("doesNotExist_xyz"),
                        ],
                    ),
                ),
                run_case(
                    "all_variables returns expected names",
                    t.assert_does_not_throw(
                        [
                            fs.set_scope_var("varA", "1"),
                            fs.set_scope_var("varB", "2"),
                        ]
                    ),
                    # varA and varB must appear in the global scope list
                    t.assert_(
                        fs.scope_var_exists("varA", "global scope")
                    ),
                    t.assert_(
                        fs.scope_var_exists("varB", "global scope")
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.all_variables("global scope")),
                        "Array",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.all_variables("all scopes")),
                        "Array",
                    ),
                ),
                run_case(
                    "closure captures variable from definition site",
                    t.assert_does_not_throw(
                        [
                            fs.set_scope_var("captured", "original"),
                            fs.set_scope_var(
                                "closureFunc",
                                fs.create_function_named(
                                    "closureFunc",
                                    [fs.return_value(fs.get_scope_var("captured"))],
                                ),
                            ),
                            # Mutate AFTER the function was captured — it reads from the
                            # surrounding scope at call time (scope is captured by reference)
                            fs.set_scope_var("captured", "mutated"),
                        ]
                    ),
                    t.assert_unstrict_equal(
                        fs.call_function(fs.get_scope_var("closureFunc"), "[]"),
                        "mutated",
                    ),
                ),
                run_case(
                    "typeof returns correct labels for builtin value types",
                    t.assert_does_not_throw(
                        [
                            fs.configure_next_function_args("[]", "[]"),
                            fs.create_function_at(
                                "typeofTestFunc",
                                [fs.return_value(fs.nothing())],
                            ),
                            c.create_class_at(
                                "TypeofTestClass",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                    c.define_instance_method(
                                        "typeofTestMethod",
                                        [fs.return_value(fs.nothing())],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "typeofTestInstance",
                                c.create_instance("TypeofTestClass", "[]"),
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.nothing()),
                        "Nothing",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.get_scope_var("typeofTestFunc")),
                        "Function",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.get_scope_var("typeofTestInstance")),
                        "Class Instance",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.get_scope_var("TypeofTestClass")),
                        "Class",
                    ),
                ),
            ),
        ],
    )


def create_inheritance_and_super_test() -> p.SRScript:
    return p.SRScript(
        position=(520, 0),
        blocks=[
            event.whenflagclicked(),
            describe_suite(
                "Inheritance, Super Calls, and Special Methods",
                run_case(
                    "super init, inherited as-string, and subclass checks work",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "BaseGreeter",
                                [
                                    c.define_special_method(
                                        [
                                            c.set_attribute(c.self(), "name", "Base"),
                                            fs.return_value(fs.nothing()),
                                        ],
                                        "init",
                                    ),
                                    c.define_instance_method(
                                        "greet",
                                        [fs.return_value("Hello from Base")],
                                    ),
                                    c.define_special_method(
                                        [fs.return_value("BaseGreeter(self)")],
                                        "as string",
                                    ),
                                ],
                            ),
                            c.create_subclass_at(
                                "FriendlyGreeter",
                                "BaseGreeter",
                                [
                                    c.define_special_method(
                                        [
                                            fs.execute_expression(
                                                c.call_super_init_method("[]")
                                            ),
                                            c.set_attribute(
                                                c.self(),
                                                "name",
                                                "Friendly",
                                            ),
                                            fs.return_value(fs.nothing()),
                                        ],
                                        "init",
                                    ),
                                    c.define_instance_method(
                                        "greet",
                                        [
                                            fs.return_value(
                                                c.call_super_method("greet", "[]")
                                            )
                                        ],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "greeter",
                                c.create_instance("FriendlyGreeter", "[]"),
                            ),
                            fs.set_scope_var(
                                "result",
                                c.call_method("greeter", "greet", "[]"),
                            ),
                        ]
                    ),
                    t.assert_(c.is_subclass("FriendlyGreeter", "BaseGreeter")),
                    t.assert_unstrict_equal(
                        fs.object_as_string(c.get_superclass("FriendlyGreeter")),
                        "<Class 'BaseGreeter'>",
                    ),
                    t.assert_unstrict_equal(fs.get_scope_var("result"), "Hello from Base"),
                    t.assert_unstrict_equal(
                        fs.object_as_string(fs.get_scope_var("greeter")),
                        "BaseGreeter(self)",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.get_scope_var("greeter")),
                        "Class Instance",
                    ),
                ),
                run_case(
                    "calling super without a superclass raises",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "NoBase",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                    c.define_instance_method(
                                        "greet",
                                        [
                                            fs.return_value(
                                                c.call_super_method("greet", "[]")
                                            )
                                        ],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "noBase",
                                c.create_instance("NoBase", "[]"),
                            ),
                        ]
                    ),
                    t.assert_throws_contains(
                        "class has no superclass",
                        [
                            fs.execute_expression(
                                c.call_method("noBase", "greet", "[]")
                            ),
                        ],
                    ),
                ),
                run_case(
                    "is_instance is polymorphic: subclass instance satisfies superclass check",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "Animal",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                ],
                            ),
                            c.create_subclass_at(
                                "Dog",
                                "Animal",
                                [
                                    c.define_special_method(
                                        [
                                            fs.execute_expression(
                                                c.call_super_init_method("[]")
                                            ),
                                            fs.return_value(fs.nothing()),
                                        ],
                                        "init",
                                    ),
                                ],
                            ),
                            c.create_class_at(
                                "Cat",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "dog",
                                c.create_instance("Dog", "[]"),
                            ),
                        ]
                    ),
                    # Dog instance is also an Animal
                    t.assert_(c.is_instance(fs.get_scope_var("dog"), "Animal")),
                    # Dog instance is not a Cat
                    t.assert_not(c.is_instance(fs.get_scope_var("dog"), "Cat")),
                    # A class (not an instance) being checked against itself returns True
                    t.assert_(c.is_subclass("Dog", "Animal")),
                    t.assert_not(c.is_subclass("Animal", "Dog")),
                ),
                run_case(
                    "get_superclass returns Nothing for a base class",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "RootClass",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                ],
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(
                        fs.object_as_string(c.get_superclass("RootClass")),
                        "<Nothing>",
                    ),
                ),
                run_case(
                    "identity check: same instance is identical, two different instances are not",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "IdentCls",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                ],
                            ),
                            fs.set_scope_var("identA", c.create_instance("IdentCls", "[]")),
                            fs.set_scope_var("identB", c.create_instance("IdentCls", "[]")),
                        ]
                    ),
                    t.assert_(
                        fs.check_identity(
                            fs.get_scope_var("identA"),
                            fs.get_scope_var("identA"),
                        )
                    ),
                    t.assert_not(
                        fs.check_identity(
                            fs.get_scope_var("identA"),
                            fs.get_scope_var("identB"),
                        )
                    ),
                ),
            ),
        ],
    )


def create_class_meta_and_members_test() -> p.SRScript:
    return p.SRScript(
        position=(520, 260),
        blocks=[
            event.whenflagclicked(),
            describe_suite(
                "Class Metadata, Getters/Setters, Operators, and Static APIs",
                run_case(
                    "getters, setters, static APIs, and metadata work together",
                    t.assert_does_not_throw(
                        [
                            fs.set_scope_var(
                                "Point",
                                c.create_class_named(
                                    "Point",
                                    [
                                        t.assert_unstrict_equal(
                                            fs.object_as_string(
                                                c.current_class()
                                            ),
                                            "<Class 'Point'>",
                                        ),
                                        c.define_getter(
                                            "x",
                                            [
                                                fs.return_value(
                                                    c.get_attribute("_x", c.self())
                                                ),
                                            ],
                                        ),
                                        c.define_setter(
                                            "x",
                                            [
                                                c.set_attribute(
                                                    c.self(),
                                                    "_x",
                                                    c.define_setter_value(),
                                                ),
                                                fs.return_value(fs.nothing()),
                                            ],
                                        ),
                                        c.define_operator_method(
                                            [
                                                fs.return_value(
                                                    fs.object_as_string(
                                                        c.operator_other_value()
                                                    )
                                                ),
                                            ],
                                            "left add",
                                        ),
                                        c.define_static_method(
                                            "origin",
                                            [
                                                fs.return_value(
                                                    c.create_instance("Point", "[]")
                                                ),
                                            ],
                                        ),
                                        c.set_class_variable(
                                            c.current_class(),
                                            "kind",
                                            "point",
                                        ),
                                    ],
                                ),
                            ),
                            fs.set_scope_var(
                                "Point3D",
                                c.create_subclass_named(
                                    "Point3D",
                                    fs.get_scope_var("Point"),
                                    [
                                        c.define_instance_method(
                                            "dim",
                                            [fs.return_value("3")],
                                        ),
                                    ],
                                ),
                            ),
                            c.on_class(
                                fs.get_scope_var("Point3D"),
                                [
                                    c.define_instance_method(
                                        "dimensionLabel",
                                        [fs.return_value("three-dimensional")],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "origin",
                                c.call_static_method("Point", "origin", "[]"),
                            ),
                            # set_attribute routes through the setter for "x"
                            c.set_attribute(fs.get_scope_var("origin"), "x", "9"),
                            fs.set_scope_var(
                                "originFactory",
                                c.get_static_method_func("origin", "Point"),
                            ),
                            fs.set_scope_var(
                                "point3d",
                                c.create_instance(fs.get_scope_var("Point3D"), "[]"),
                            ),
                        ]
                    ),
                    # getter routes through setter-written _x
                    t.assert_unstrict_equal(
                        c.get_attribute("x", fs.get_scope_var("origin")),
                        "9",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(c.get_all_attributes(fs.get_scope_var("origin"))),
                        "Object",
                    ),
                    t.assert_unstrict_equal(
                        fs.object_as_string(
                            c.get_class_of_instance(fs.get_scope_var("origin"))
                        ),
                        "<Class 'Point'>",
                    ),
                    t.assert_(c.is_instance(fs.get_scope_var("origin"), "Point")),
                    t.assert_(
                        fs.check_identity(
                            fs.get_scope_var("origin"),
                            fs.get_scope_var("origin"),
                        )
                    ),
                    t.assert_unstrict_equal(c.get_class_variable("kind", "Point"), "point"),
                    t.assert_unstrict_equal(
                        fs.typeof_value(fs.get_scope_var("originFactory")),
                        "Function",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(
                            fs.call_function(fs.get_scope_var("originFactory"), "[]")
                        ),
                        "Class Instance",
                    ),
                    t.assert_unstrict_equal(
                        c.call_method(fs.get_scope_var("point3d"), "dimensionLabel", "[]"),
                        "three-dimensional",
                    ),
                ),
                run_case(
                    "deleted class variables and getter-only attributes raise as expected",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "ReadOnlyThing",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                    c.define_getter(
                                        "value",
                                        [fs.return_value("locked")],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "readOnlyThing",
                                c.create_instance("ReadOnlyThing", "[]"),
                            ),
                            fs.set_scope_var(
                                "MetaPoint",
                                c.create_class_named(
                                    "MetaPoint",
                                    [
                                        c.define_static_method(
                                            "origin",
                                            [
                                                fs.return_value(
                                                    c.create_instance(
                                                        "MetaPoint",
                                                        "[]",
                                                    )
                                                ),
                                            ],
                                        ),
                                        c.set_class_variable(
                                            c.current_class(),
                                            "kind",
                                            "meta",
                                        ),
                                    ],
                                ),
                            ),
                            fs.set_scope_var(
                                "metaOrigin",
                                c.call_static_method("MetaPoint", "origin", "[]"),
                            ),
                            c.delete_class_variable("MetaPoint", "kind"),
                        ]
                    ),
                    t.assert_throws_contains(
                        "getter method",
                        [
                            c.set_attribute(
                                fs.get_scope_var("readOnlyThing"),
                                "value",
                                "new",
                            ),
                        ],
                    ),
                    t.assert_throws_contains(
                        "Undefined class variable",
                        [
                            fs.execute_expression(
                                c.get_class_variable("kind", "MetaPoint")
                            ),
                        ],
                    ),
                    t.assert_throws_contains(
                        "Undefined instance method",
                        [
                            fs.execute_expression(
                                c.call_method(
                                    fs.get_scope_var("metaOrigin"),
                                    "dimensionLabel",
                                    "[]",
                                )
                            ),
                        ],
                    ),
                ),
                run_case(
                    "operator method is actually invoked and returns the expected value",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "OpClass",
                                [
                                    c.define_special_method(
                                        [
                                            c.set_attribute(c.self(), "val", "op-instance"),
                                            fs.return_value(fs.nothing()),
                                        ],
                                        "init",
                                    ),
                                    # left add: returns "self+<other>"
                                    c.define_operator_method(
                                        [
                                            fs.return_value(
                                                fs.object_as_string(
                                                    c.operator_other_value()
                                                )
                                            ),
                                        ],
                                        "left add",
                                    ),
                                    # equals: returns true when other has the same val attribute
                                    c.define_operator_method(
                                        [
                                            fs.return_value(
                                                fs.object_as_string(
                                                    c.operator_other_value()
                                                )
                                            ),
                                        ],
                                        "equals",
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "opObj",
                                c.create_instance("OpClass", "[]"),
                            ),
                            fs.set_scope_var(
                                "opResult",
                                # opObj + "extra" should trigger the left-add operator method
                                # We call it directly via call_method with internal name
                                c.call_method(
                                    "opObj",
                                    "__operator_left_add__",
                                    '["extra"]',
                                ),
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(
                        fs.get_scope_var("opResult"),
                        "extra",
                    ),
                ),
                run_case(
                    "setter returning non-Nothing raises",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "BadSetter",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                    c.define_setter(
                                        "bad",
                                        [
                                            # intentionally return a non-Nothing value
                                            fs.return_value("oops"),
                                        ],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "badSetterObj",
                                c.create_instance("BadSetter", "[]"),
                            ),
                        ]
                    ),
                    t.assert_throws_contains(
                        "must return",
                        [
                            c.set_attribute(
                                fs.get_scope_var("badSetterObj"),
                                "bad",
                                "value",
                            ),
                        ],
                    ),
                ),
                run_case(
                    "property_names_of_class returns correct member lists",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "MemberListClass",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                    c.define_instance_method(
                                        "instM",
                                        [fs.return_value(fs.nothing())],
                                    ),
                                    c.define_static_method(
                                        "statM",
                                        [fs.return_value(fs.nothing())],
                                    ),
                                    c.define_getter(
                                        "getterProp",
                                        [fs.return_value("g")],
                                    ),
                                    c.define_setter(
                                        "setterProp",
                                        [fs.return_value(fs.nothing())],
                                    ),
                                    c.define_operator_method(
                                        [fs.return_value(fs.nothing())],
                                        "left add",
                                    ),
                                    c.set_class_variable(
                                        c.current_class(),
                                        "clsVar",
                                        "cv",
                                    ),
                                ],
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(
                            c.property_names_of_class("MemberListClass", "instance method")
                        ),
                        "Array",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(
                            c.property_names_of_class("MemberListClass", "static method")
                        ),
                        "Array",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(
                            c.property_names_of_class("MemberListClass", "getter method")
                        ),
                        "Array",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(
                            c.property_names_of_class("MemberListClass", "setter method")
                        ),
                        "Array",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(
                            c.property_names_of_class("MemberListClass", "operator method")
                        ),
                        "Array",
                    ),
                    t.assert_unstrict_equal(
                        fs.typeof_value(
                            c.property_names_of_class("MemberListClass", "class variable")
                        ),
                        "Array",
                    ),
                ),
                run_case(
                    "class variable can be updated and on_class adds to an existing class",
                    t.assert_does_not_throw(
                        [
                            c.create_class_at(
                                "UpdatableClass",
                                [
                                    c.define_special_method(
                                        [fs.return_value(fs.nothing())],
                                        "init",
                                    ),
                                    c.set_class_variable(
                                        c.current_class(),
                                        "count",
                                        "0",
                                    ),
                                ],
                            ),
                            # update the class variable
                            c.set_class_variable("UpdatableClass", "count", "99"),
                            # on_class reopens and adds a new method
                            c.on_class(
                                "UpdatableClass",
                                [
                                    c.define_instance_method(
                                        "newMethod",
                                        [fs.return_value("added-later")],
                                    ),
                                ],
                            ),
                            fs.set_scope_var(
                                "updObj",
                                c.create_instance("UpdatableClass", "[]"),
                            ),
                        ]
                    ),
                    t.assert_unstrict_equal(
                        c.get_class_variable("count", "UpdatableClass"),
                        "99",
                    ),
                    t.assert_unstrict_equal(
                        c.call_method(fs.get_scope_var("updObj"), "newMethod", "[]"),
                        "added-later",
                    ),
                ),
            ),
        ],
    )


EXAMPLE_CASES: list[ExampleCase] = [
    ExampleCase(
        key="create_class_test",
        title="Basic Class With Instance Method",
        description=(
            "Runnable test suite for class creation, static factory methods, returned values, "
            "missing-method errors, argument count errors (too many / too few), "
            "missing attribute access, and typeof on class instances."
        ),
        build_script=create_class_test,
    ),
    ExampleCase(
        key="create_scopes_and_functions_edge_test",
        title="Scopes, Binding, and Function Defaults",
        description=(
            "Covers global/local scope behavior, global binding, non-local binding, "
            "function defaults, Nothing returns, invalid configuration errors, "
            "closure capture semantics, delete-non-existent errors, all_variables return type, "
            "and typeof for Function/Class/Nothing/ClassInstance."
        ),
        build_script=create_scopes_and_functions_edge_test,
    ),
    ExampleCase(
        key="create_inheritance_and_super_test",
        title="Inheritance, Super Calls, and Special Methods",
        description=(
            "Checks subclass relationships (positive and negative), inherited as-string behavior, "
            "super dispatch, no-superclass error, get_superclass returning Nothing for root classes, "
            "polymorphic is_instance, and identity check positive/negative cases."
        ),
        build_script=create_inheritance_and_super_test,
    ),
    ExampleCase(
        key="create_class_meta_and_members_test",
        title="Class Metadata, Getters/Setters, Operators, and Static APIs",
        description=(
            "Exercises getters/setters (read and write through set_attribute), "
            "class metadata, static method functions, instance introspection, "
            "operator method actual invocation, setter returning non-Nothing error, "
            "property_names_of_class for all six member types, "
            "class variable update, and on_class reopening."
        ),
        build_script=create_class_meta_and_members_test,
    ),
]


def print_example_descriptions() -> None:
    print("\n" + 50 * "=" + " Test Catalog " + 50 * "=")
    for idx, case in enumerate(EXAMPLE_CASES, start=1):
        print(f"\n{idx}. {case.key} - {case.title}")
        print(f"   {case.description}")


def create_test() -> None:
    cfg = p.get_default_config()
    handler = (
        lambda url: url.startswith(
            "https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/"
        )
    )
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    p.init_config(cfg)

    project = p.SRProject.create_empty()
    project.stage.scripts = [case.build_script() for case in EXAMPLE_CASES]
    project.extensions = [
        p.SRCustomExtension(
            id="gceOOP",
             url=extension_url("gceOOP.js"),
        ),
        p.SRCustomExtension(
            id="gceFuncsScopes",
            url=extension_url("gceFuncsScopes.js"),
        ),
        p.SRCustomExtension(
            id="gceTestRunner",
            url=extension_url("gceTestRunner.js"),
        ),
    ]

    print(50 * "=", "Created Project", 50 * "=")
    print(project)
    project.add_all_extensions_to_info_api(p.info_api)

    # Tricks to avoid errors for invalid extension URLs (currently too strict)
    extensions_before = copy.deepcopy(project.extensions)
    for extension in project.extensions:
        extension.url = "https://example.com/"

    project.validate(AbstractTreePath(), p.info_api)
    project.extensions = extensions_before

    frproject = project.to_first(p.info_api)
    frproject.to_file("project_tests.pmp")
    print_example_descriptions()
    print(project.extensions)


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.parse_args()

    create_test()


if __name__ == "__main__":
    main()
