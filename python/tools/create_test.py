from __future__ import annotations
import sys; from pathlib import Path
sys.path.append(
    str(Path(__file__).parent.parent)
)

from helpers.gceClassesOOP import gceClassesOOP as c

from gceutils import AbstractTreePath, grepr_dataclass
import pmp_manip as p
from typing import Callable


@grepr_dataclass(frozen=True)
class ExampleCase:
    key: str
    title: str
    description: str
    build_script: Callable[[], p.SRScript]


def create_class_test():
    return p.SRScript(
        position=(0, 0),
        blocks=[
            c.createClassAt(
                name="Greeter",
                substack=[
                    c.defineSpecialMethod(
                        [
                            c.setAttribute(c.self(), "prefix", "Hello"),
                            c.return_(c.nothing()),
                        ],
                        "init",
                    ),
                    c.defineInstanceMethod(
                        name="greet",
                        substack=[
                            c.return_(c.getAttribute("name", c.self()))
                        ],
                    ),
                    c.defineStaticMethod(
                        name="fromName",
                        substack=[
                            c.setScopeVar("obj", c.createInstance("Greeter", "[]")),
                            c.setAttribute(c.getScopeVar("obj"), "name", "World"),
                            c.return_(c.getScopeVar("obj")),
                        ]
                    ),
                ],
            ),
            c.setScopeVar("greeter", c.callStaticMethod("Greeter", "fromName", "[]")),
            c.setScopeVar("message", c.callMethod("greeter", "greet", "[]")),
            c.executeExpression(c.getScopeVar("message")),
        ]
    )


def create_scopes_and_functions_edge_test() -> p.SRScript:
    return p.SRScript(
        position=(0, 180),
        blocks=[
            c.logStacks(),
            c.setScopeVar("outer", "global-value"),
            c.executeExpression(c.scopeVarExists("outer", "all scopes")),
            c.executeExpression(c.allVariables("global scope")),
            c.createVarScope(
                [
                    c.bindVarToScope("outer", "global"),
                    c.setScopeVar("shadow", "local-value"),
                    c.executeExpression(c.getScopeVar("outer")),
                    c.executeExpression(c.scopeVarExists("shadow", "local scope")),
                    c.executeExpression(c.allVariables("all scopes")),
                    c.configureNextFunctionArgs('["a", "b"]', '["B-default"]'),
                    c.createFunctionAt(
                        "combine",
                        [
                            c.return_("combine-result")
                        ],
                    ),
                    c.setScopeVar(
                        "echo",
                        c.createFunctionNamed(
                            "echo",
                            [
                                c.return_(c.nothing()),
                            ],
                        ),
                    ),
                    c.executeExpression(c.callFunction("combine", '["A-only"]')),
                    c.executeExpression(c.callFunction("echo", "[]")),
                    c.deleteScopeVar("shadow"),
                    c.executeExpression(c.scopeVarExists("shadow", "all scopes")),
                ]
            ),
            c.executeExpression(c.getScopeVar("outer")),
        ],
    )


def create_inheritance_and_super_test() -> p.SRScript:
    return p.SRScript(
        position=(520, 0),
        blocks=[
            c.createClassAt(
                "BaseGreeter",
                [
                    c.defineSpecialMethod(
                        [
                            c.setAttribute(c.self(), "name", "Base"),
                            c.return_(c.nothing()),
                        ],
                        "init",
                    ),
                    c.defineInstanceMethod(
                        "greet",
                        [
                            c.return_("Hello from Base"),
                        ],
                    ),
                    c.defineSpecialMethod(
                        [
                            c.return_("BaseGreeter(self)"),
                        ],
                        "as string",
                    ),
                ],
            ),
            c.createSubclassAt(
                "FriendlyGreeter",
                "BaseGreeter",
                [
                    c.defineSpecialMethod(
                        [
                            c.executeExpression(c.callSuperInitMethod("[]")),
                            c.setAttribute(c.self(), "name", "Friendly"),
                            c.return_(c.nothing()),
                        ],
                        "init",
                    ),
                    c.defineInstanceMethod(
                        "greet",
                        [
                            c.return_(c.callSuperMethod("greet", "[]")),
                        ],
                    ),
                ],
            ),
            c.setScopeVar("isSub", c.isSubclass("FriendlyGreeter", "BaseGreeter")),
            c.setScopeVar("superOfFriendly", c.getSuperclass("FriendlyGreeter")),
            c.setScopeVar("greeter", c.createInstance("FriendlyGreeter", "[]")),
            c.setScopeVar("result", c.callMethod("greeter", "greet", "[]")),
            c.executeExpression(c.objectAsString(c.getScopeVar("greeter"))),
            c.executeExpression(c.typeof(c.getScopeVar("greeter"))),
        ],
    )


def create_class_meta_and_members_test() -> p.SRScript:
    return p.SRScript(
        position=(520, 260),
        blocks=[
            c.setScopeVar(
                "Point",
                c.createClassNamed(
                    "Point",
                    [
                        c.executeExpression(c.classBeingCreated()),
                        c.defineGetter(
                            "x",
                            [
                                c.return_(c.getAttribute("_x", c.self())),
                            ],
                        ),
                        c.defineSetter(
                            "x",
                            [
                                c.setAttribute(c.self(), "_x", c.defineSetterValue()),
                                c.return_(c.nothing()),
                            ],
                        ),
                        c.defineOperatorMethod(
                            [
                                c.return_(c.operatorOtherValue()),
                            ],
                            "left add",
                        ),
                        c.defineStaticMethod(
                            "origin",
                            [
                                c.return_(c.createInstance("Point", "[0]")),
                            ],
                        ),
                        c.setClassVariable(c.classBeingCreated(), "kind", "point"),
                    ],
                ),
            ),
            c.setScopeVar(
                "Point3D",
                c.createSubclassNamed(
                    "Point3D",
                    c.getScopeVar("Point"),
                    [
                        c.defineInstanceMethod(
                            "dim",
                            [
                                c.return_("3"),
                            ],
                        ),
                    ],
                ),
            ),
            c.onClass(
                c.getScopeVar("Point3D"),
                [
                    c.defineInstanceMethod(
                        "dimensionLabel",
                        [
                            c.return_("three-dimensional"),
                        ],
                    ),
                ],
            ),
            c.setScopeVar("origin", c.callStaticMethod("Point", "origin", "[]")),
            c.setAttribute(c.getScopeVar("origin"), "x", "9"),
            c.executeExpression(c.getAttribute("x", c.getScopeVar("origin"))),
            c.executeExpression(c.getAllAttributes(c.getScopeVar("origin"))),
            c.executeExpression(c.getClassOfInstance(c.getScopeVar("origin"))),
            c.executeExpression(c.isInstance(c.getScopeVar("origin"), "Point")),
            c.executeExpression(c.checkIdentity(c.getScopeVar("origin"), c.getScopeVar("origin"))),
            c.executeExpression(c.callMethod(c.getScopeVar("origin"), "dimensionLabel", "[]")),
            c.executeExpression(c.getClassVariable("kind", "Point")),
            c.deleteClassVariable("Point", "kind"),
            c.executeExpression(c.propertyNamesOfClass("Point", "instance method")),
            c.executeExpression(c.propertyNamesOfClass("Point", "static method")),
            c.executeExpression(c.propertyNamesOfClass("Point", "getter method")),
            c.executeExpression(c.propertyNamesOfClass("Point", "setter method")),
            c.executeExpression(c.propertyNamesOfClass("Point", "operator method")),
            c.executeExpression(c.propertyNamesOfClass("Point", "class variable")),
            c.setScopeVar("originFactory", c.getStaticMethodFunc("origin", "Point")),
            c.executeExpression(c.callFunction(c.getScopeVar("originFactory"), "[]")),
        ],
    )


EXAMPLE_CASES: list[ExampleCase] = [
    ExampleCase(
        key="create_class_test",
        title="Basic Class With Instance Method",
        description=(
            "Minimal class definition showing create class + instance method + return. "
            "Good first example for users new to the extension."
        ),
        build_script=create_class_test,
    ),
    ExampleCase(
        key="create_scopes_and_functions_edge_test",
        title="Scopes, Binding, and Function Defaults",
        description=(
            "Connected variable-scope workflow with local scopes, global binding, existence checks, "
            "deletion, and function argument defaults. Includes edge behavior like optional arguments "
            "and returning Nothing."
        ),
        build_script=create_scopes_and_functions_edge_test,
    ),
    ExampleCase(
        key="create_inheritance_and_super_test",
        title="Inheritance, Super Calls, and Special Methods",
        description=(
            "Uses superclass/subclass checks, init + as-string special methods, and super calls. "
            "Demonstrates object creation and method dispatch across inheritance boundaries."
        ),
        build_script=create_inheritance_and_super_test,
    ),
    ExampleCase(
        key="create_class_meta_and_members_test",
        title="Class Metadata, Getters/Setters, Operators, and Static APIs",
        description=(
            "Complex class model using named class builders, class reopening, getters/setters, "
            "operator methods, class variables, static methods as first-class functions, and instance "
            "introspection blocks."
        ),
        build_script=create_class_meta_and_members_test,
    ),
]


def print_example_descriptions() -> None:
    print("\n" + 50 * "=" + " Classes Example Catalog " + 50 * "=")
    for idx, case in enumerate(EXAMPLE_CASES, start=1):
        print(f"\n{idx}. {case.key} - {case.title}")
        print(f"   {case.description}")

def create_test() -> None:
    cfg = p.get_default_config()
    handler = lambda url: url.startswith("https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/")
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    p.init_config(cfg)

    project = p.SRProject.create_empty()
    project.stage.scripts = [case.build_script() for case in EXAMPLE_CASES]
    project.extensions = [p.SRCustomExtension(
        id="gceClassesOOP",
        url=("https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/"+
        "refs/heads/main/extensions/classes.js"),
    )]

    print(50*"=", "Created Project", 50*"=")
    print(project)
    project.add_all_extensions_to_info_api(p.info_api)
    project.validate(AbstractTreePath(), p.info_api)
    frproject = project.to_first(p.info_api)
    frproject.to_file("project_tests.pmp")
    print_example_descriptions()


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    create_test()

if __name__ == "__main__":
    main()
