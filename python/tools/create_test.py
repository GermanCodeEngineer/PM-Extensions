from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable

sys.path.append(str(Path(__file__).parent.parent))

import copy
import pmp_manip as p
from gceutils import AbstractTreePath, grepr_dataclass

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
    return t.describe(name, list(tests))


def run_case(name: str, *blocks: p.SRBlock) -> p.SRBlock:
    return t.run_test(name, list(blocks))


def create_class_test() -> p.SRScript:
    return p.SRScript(
        position=(0, 0),
        blocks=[ # HERE: review tests
            t.reset_results(),
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
                    t.assert_equal(fs.get_scope_var("message"), "World"),
                    t.assert_equal(
                        fs.object_as_string(fs.get_scope_var("greeter")),
                        "<Instance of 'Greeter'>",
                    ),
                    t.assert_equal(
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
                    t.assert_throws(
                        "Undefined instance method",
                        [
                            fs.execute_expression(
                                c.call_method("emptyGreeter", "missing", "[]")
                            ),
                        ],
                    ),
                ),
            ),
            t.report_results(),
        ],
    )


def create_scopes_and_functions_edge_test() -> p.SRScript:
    return p.SRScript(
        position=(0, 180),
        blocks=[
            t.reset_results(),
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
                                    t.assert_equal(
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
                    t.assert_equal(fs.get_scope_var("outer"), "global-value"),
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
                    t.assert_equal(fs.get_scope_var("combined"), "B-default"),
                    t.assert_equal(
                        fs.typeof_value(fs.get_scope_var("echo")),
                        "Function",
                    ),
                    t.assert_equal(
                        fs.object_as_string(fs.get_scope_var("echoResult")),
                        "<Nothing>",
                    ),
                ),
                run_case(
                    "invalid default configurations raise an error",
                    t.assert_throws(
                        "as many default values",
                        [
                            fs.configure_next_function_args(
                                '["onlyArg"]',
                                '["first", "second"]',
                            ),
                        ],
                    ),
                ),
            ),
            t.report_results(),
        ],
    )


def create_inheritance_and_super_test() -> p.SRScript:
    return p.SRScript(
        position=(520, 0),
        blocks=[
            t.reset_results(),
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
                    t.assert_equal(
                        fs.object_as_string(c.get_superclass("FriendlyGreeter")),
                        "<Class 'BaseGreeter'>",
                    ),
                    t.assert_equal(fs.get_scope_var("result"), "Hello from Base"),
                    t.assert_equal(
                        fs.object_as_string(fs.get_scope_var("greeter")),
                        "BaseGreeter(self)",
                    ),
                    t.assert_equal(
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
                    t.assert_throws(
                        "class has no superclass",
                        [
                            fs.execute_expression(
                                c.call_method("noBase", "greet", "[]")
                            ),
                        ],
                    ),
                ),
            ),
            t.report_results(),
        ],
    )


def create_class_meta_and_members_test() -> p.SRScript:
    return p.SRScript(
        position=(520, 260),
        blocks=[
            t.reset_results(),
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
                                        t.assert_equal(
                                            fs.object_as_string(
                                                c.class_being_created()
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
                                            c.class_being_created(),
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
                    t.assert_equal(
                        c.get_attribute("x", fs.get_scope_var("origin")),
                        "9",
                    ),
                    t.assert_equal(
                        fs.typeof_value(c.get_all_attributes(fs.get_scope_var("origin"))),
                        "Object",
                    ),
                    t.assert_equal(
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
                    t.assert_equal(c.get_class_variable("kind", "Point"), "point"),
                    t.assert_equal(
                        fs.typeof_value(fs.get_scope_var("originFactory")),
                        "Function",
                    ),
                    t.assert_equal(
                        fs.typeof_value(
                            fs.call_function(fs.get_scope_var("originFactory"), "[]")
                        ),
                        "Class Instance",
                    ),
                    t.assert_equal(
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
                                            c.class_being_created(),
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
                    t.assert_throws(
                        "getter method",
                        [
                            c.set_attribute(
                                fs.get_scope_var("readOnlyThing"),
                                "value",
                                "new",
                            ),
                        ],
                    ),
                    t.assert_throws(
                        "Undefined class variable",
                        [
                            fs.execute_expression(
                                c.get_class_variable("kind", "MetaPoint")
                            ),
                        ],
                    ),
                    t.assert_throws(
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
            ),
            t.report_results(),
        ],
    )


EXAMPLE_CASES: list[ExampleCase] = [
    ExampleCase(
        key="create_class_test",
        title="Basic Class With Instance Method",
        description=(
            "Runnable test suite for class creation, static factory methods, returned values, "
            "and missing-method error handling."
        ),
        build_script=create_class_test,
    ),
    ExampleCase(
        key="create_scopes_and_functions_edge_test",
        title="Scopes, Binding, and Function Defaults",
        description=(
            "Covers global/local scope behavior, binding, function defaults, Nothing returns, "
            "and invalid configuration errors."
        ),
        build_script=create_scopes_and_functions_edge_test,
    ),
    ExampleCase(
        key="create_inheritance_and_super_test",
        title="Inheritance, Super Calls, and Special Methods",
        description=(
            "Checks subclass relationships, inherited as-string behavior, super dispatch, "
            "and the no-superclass error path."
        ),
        build_script=create_inheritance_and_super_test,
    ),
    ExampleCase(
        key="create_class_meta_and_members_test",
        title="Class Metadata, Getters/Setters, Operators, and Static APIs",
        description=(
            "Exercises getters/setters, class metadata, static method functions, instance "
            "introspection, and expected member-access failures."
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
