from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import copy
from gceutils import AbstractTreePath
import pmp_manip as p
from pmp_manip.opcode_info.api import OpcodeInfoAPI

from helpers.gceFuncsScopes import gceFuncsScopes
from helpers.gceOOP import gceOOP
from helpers.gceTestRunner import gceTestRunner as t
from helpers.jwProto import jwProto as labels
import helpers as h


class o(gceOOP, gceFuncsScopes): # Combine both OOP extensions
    pass

EXTENSION_URL_BASE = (
    #"https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/"
    #"refs/heads/main/extensions"
    "http://localhost:5173/extensions"
)

def own_extension_url(filename: str) -> str:
    return f"{EXTENSION_URL_BASE}/{filename}"

EXTENSION_SOURCES = {
    # My Extensions
    "gceOOP": own_extension_url("gceOOP.js"),
    "gceFuncsScopes": own_extension_url("gceFuncsScopes.js"),
    "gceTestRunner": own_extension_url("gceTestRunner.js"),

    # Useful Extensions
    "jwProto": None,
    "SPjavascriptV2": None,

    # All Custom Type Extensions
    "agBuffer": "https://extensions.penguinmod.com/extensions/AndrewGaming587/agBuffer.js",
    # agBuffer: vm.agBuffer.Type
    # agBufferPointer: vm.agBuffer.PointerType
    "ddeDateFormat": "https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormat.js",
    "ddeDateFormatV2": "https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormatV2.js",
    "divAlgEffects": "https://extensions.penguinmod.com/extensions/Div/divAlgEffects.js",
    # divEffect: vm.divAlgEffects.Effect
    "divIterator": "https://extensions.penguinmod.com/extensions/Div/divIterators.js",
    # divIterator: vm.divIterator.Type
    "dogeiscutObject": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js",
    "dogeiscutRegularExpressions": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutRegularExpressions.js",
    # dogeiscutRegularExpression: vm.dogeiscutRegularExpression.Type
    "dogeiscutSet": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutSet.js",
    "fruitsPaintUtils": "https://extensions.penguinmod.com/extensions/Fruits555000/PaintUtils.js",
    # paintUtilsColour: Object.getPrototypeOf(vm.runtime.ext_fruitsPaintUtils.getColour({COLOUR_NAME: "orange"}))
    "jwArray": None,
    "jwColor": None,
    "jwDate": None,
    "jwLambda": None,
    "jwNum": None,
    "jwTargets": None,
    "jwVector": None,
    "jwXML": None,
    "newCanvas": None,
    # canvasData: runtime._extensionVariables.canvas
    "steve0greatnesstimers": "https://extensions.penguinmod.com/extensions/steve0greatness/timers.js",
    # externaltimer: runtime._extensionVariables.externaltimer
}

def configure() -> None:
    cfg = p.get_default_config()
    handler = (
        lambda url: url.startswith(EXTENSION_URL_BASE)
    )
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    p.init_config(cfg)



_SCRIPT_IDX = 0
def create_script(*blocks: tuple[p.SRBlock, ...]) -> p.SRScript:
    global _SCRIPT_IDX
    script = p.SRScript(
        position=(200 * _SCRIPT_IDX, 0),
        blocks=[
            *blocks,
        ],
    )
    _SCRIPT_IDX += 1
    return script

def create_test_project(extension_ids: list[str], scripts: list[p.SRScript]) -> p.FRProject:
    project = p.SRProject.create_empty()
    project.stage.scripts = scripts
    project.extensions = []
    for id in extension_ids:
        url = EXTENSION_SOURCES[id]
        project.extensions.append(
            p.SRCustomExtension(id, url) if url is not None else p.SRBuiltinExtension(id=id)
        )
    

    opcode_info_copy = p.info_api.opcode_info.copy()
    info_api_copy = OpcodeInfoAPI(opcode_info_copy)
    project.add_all_extensions_to_info_api(info_api_copy)

    # Tricks to avoid errors for invalid extension URLs (currently too strict)
    extensions_before = copy.deepcopy(project.extensions)
    for extension in project.extensions:
        extension.url = "https://example.com/"

    project.validate(AbstractTreePath(), info_api_copy)
    project.extensions = extensions_before

    frproject = project.to_first(info_api_copy)
    return frproject

def write_project_to_file(project: p.FRProject, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)
    project.to_file(str(output_file))

def test_TypeChecker() -> p.FRProject:
    script = create_script(
        h.event.whenflagclicked(),
        t.test_scope("TypeChecker", [
            t.test_scope("My Types", [
                t.assert_(o.typeof_value_is_menu(o.create_function_named("myFn", []), "Function (GCE)")),
                labels.label_command("Methods can not be accessed from a reporter"),
                t.assert_(o.typeof_value_is_menu(o.create_class_named("MyClass", []), "Class (GCE)")),
                t.assert_(o.typeof_value_is_menu(o.create_instance(o.create_class_named("MyClass", []), "[]"), "Class Instance (GCE)")),
                t.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
            ]),
            t.test_scope("Common/Safe JS data types", [
                t.assert_(o.typeof_value_is_menu(h.SPjavascriptV2.js_reporter("return undefined"), "JavaScript Undefined")),
                t.assert_(o.typeof_value_is_menu(h.SPjavascriptV2.js_reporter("return null"), "JavaScript Null")),
                t.assert_(o.typeof_value_is_menu(h.operator.true_boolean(), "Boolean")),
                t.assert_(o.typeof_value_is_menu("777", "Number")),
                t.assert_(o.typeof_value_is_menu("hello", "String")),
            ]),
            t.test_scope("Custom Extension Types", [
                t.assert_(o.typeof_value_is_menu(h.agBuffer.new_buffer("1"), "Buffer (AndrewGaming587)")),
                t.assert_(o.typeof_value_is_menu(h.agBuffer.create_pointer(
                    "0", False, h.agBuffer.new_buffer("1"), "Uint8",
                ), "Buffer Pointer (AndrewGaming587)")),
                t.assert_(o.typeof_value_is_menu(h.ddeDateFormat.current_date(), "Date (Old Version) (ddededodediamante)")),
                t.assert_(o.typeof_value_is_menu(h.ddeDateFormatV2.current_date(), "Date (ddededodediamante)")),
                labels.label_command("You can't access a div effect type from any reporter"),            
                t.assert_(o.typeof_value_is_menu(h.divIterator.iter_builder("", []), "Iterator (Div)")),
                t.assert_(o.typeof_value_is_menu(h.dogeiscutObject.blank(), "Object (DogeisCut)")),
                t.assert_(o.typeof_value_is_menu(h.dogeiscutRegularExpressions.regex("(.*)", "gm"), "Regular Expression (DogeisCut)")),
                t.assert_(o.typeof_value_is_menu(h.dogeiscutSet.blank(), "Set (DogeisCut)")),
                labels.label_command("You can't access a timer type from any reporter"),
                t.assert_(o.typeof_value_is_menu(h.jwArray.blank(), "Array (jwklong)")),
                t.assert_(o.typeof_value_is_menu(h.jwColor.new_color("#ff0000"), "Color (jwklong)")),
                t.assert_(o.typeof_value_is_menu(h.jwDate.now(), "Date (jwklong)")),
                t.assert_(o.typeof_value_is_menu(h.jwLambda.new_lambda([]), "Lambda (jwklong)")),
                t.assert_(o.typeof_value_is_menu(h.jwNum.add("1", "2"), "Number (jwklong)")),
                t.assert_(o.typeof_value_is_menu(h.jwTargets.this(), "Target (jwklong)")),
                t.assert_(o.typeof_value_is_menu(h.jwVector.new_vector("1", "2"), "Vector (jwklong)")),
                t.assert_(o.typeof_value_is_menu(h.jwXML.new_node("test"), "XML (jwklong)")),
                labels.label_function("For this to work please create a canvas variable e.g. 'myCanvasVar', then enable the condition", [
                    h.control.if_(False, [
                        t.assert_(o.typeof_value_is_menu("<put the canvas variable block here>", "Canvas (RedMan13)")),
                    ]),
                ]),
                t.assert_(o.typeof_value_is_menu(h.fruitsPaintUtils.get_colour("orange"), "Paint Utils Colour (Fruits555000)")),
            ]),
        ])
    )
    
    return create_test_project(scripts=[script], extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto", "SPjavascriptV2", "agBuffer", "ddeDateFormat", 
        "ddeDateFormatV2", "divAlgEffects", "divIterator", "dogeiscutObject", "dogeiscutRegularExpressions", 
        "dogeiscutSet", "fruitsPaintUtils", "jwArray", "jwColor", "jwDate", "jwLambda", "jwNum", "jwTargets", 
        "jwVector", "jwXML", "newCanvas", "steve0greatnesstimers"
    ])

def test_Cast() -> p.FRProject:
    script = create_script(
        h.event.whenflagclicked(),
        t.test_scope("Cast", [
            t.test_scope("toArray", [o.create_var_scope([
                o.set_scope_var("my var", "hello"),
                o.set_scope_var("var list", o.all_variables("all scopes")),
                t.assert_type(o.get_scope_var("var list"), "Array (jwklong)"),
                t.assert_unstrict_equal(o.get_scope_var("var list"), '["my var"]')
            ])]),
            t.test_scope("toObject", [o.create_var_scope([
                o.create_class_at("MyClass", []),
                o.set_scope_var("instance var", o.create_instance(o.create_class_named("MyClass", []), "[]")),
                o.set_attribute(o.get_scope_var("instance var"), "my attribute", "hello"),
                o.set_scope_var("attributes", o.get_all_attributes(o.get_scope_var("instance var"))),
                t.assert_type(o.get_scope_var("attributes"), "Object (DogeisCut)"),
                t.assert_unstrict_equal(o.get_scope_var("attributes"), '{"my attribute":"hello"}'),
            ])]),
            t.test_scope("toClass && toClassInstance && toFunction", [o.create_var_scope([
                o.create_class_at("MyClass", []),
                t.assert_unstrict_equal(o.get_superclass(o.create_subclass_named("Sub", "MyClass", [])), "<Class 'MyClass'>"),
                t.assert_throws_contains("but got no input value", [
                    o.execute_expression(o.get_superclass(h.SPjavascriptV2.js_reporter("return undefined"))),
                ]),
                t.assert_throws_contains("but got no input value", [
                    o.execute_expression(o.get_superclass(h.SPjavascriptV2.js_reporter("return null"))),
                ]),
                t.assert_unstrict_equal(o.get_superclass("MyClass"), "<Class 'Superclass'>"),
                o.create_class_at("513", []),
                t.assert_unstrict_equal(o.get_superclass("513"), "<Class 'Superclass'>"),
                t.assert_throws_contains("but got no input value", [
                    o.execute_expression(o.get_superclass(h.SPjavascriptV2.js_reporter("return null"))),
                ]),
                t.assert_throws([
                    o.create_subclass_at("Sub2", o.create_function_named("myFunction", []), []),
                ]),
            ])]),
        ]),
    )
    
    return create_test_project(scripts=[script], extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto", "SPjavascriptV2",
    ])

def test_scoped_variables_blocks() -> p.FRProject:
    kind_all = "all scopes"
    kind_local = "local scope"
    kind_global = "global scope"
    bind_global = "global"

    script = create_script(
        h.event.whenflagclicked(),
        t.test_scope("Scoped Variables Blocks", [
            t.test_scope("set/get/exists", [
                labels.label_command("Set and read a local variable"),
                o.create_var_scope([
                    t.assert_not(o.scope_var_exists("myVar", kind_all)),
                    t.assert_not(o.scope_var_exists("myVar", kind_local)),
                    t.assert_not(o.scope_var_exists("myVar", kind_global)),
                    o.set_scope_var("myVar", "hello"),
                    t.assert_strict_equal(o.get_scope_var("myVar"), "hello"),
                    t.assert_(o.scope_var_exists("myVar", kind_all)),
                    t.assert_(o.scope_var_exists("myVar", kind_local)),
                    t.assert_not(o.scope_var_exists("myVar", kind_global)),
                ]),
            ]),

            t.test_scope("delete var", [
                labels.label_command("Delete removes the variable from the current scope"),
                o.create_var_scope([
                    o.set_scope_var("tmp", "to-delete"),
                    t.assert_(o.scope_var_exists("tmp", kind_all)),
                    o.delete_scope_var("tmp"),
                    t.assert_not(o.scope_var_exists("tmp", kind_all)),
                    t.assert_not(o.scope_var_exists("tmp", kind_local)),
                    t.assert_not(o.scope_var_exists("tmp", kind_global)),
                    t.assert_throws([
                        o.execute_expression(o.get_scope_var("tmp")),
                    ]),
                ]),
            ]),

            t.test_scope("all variables + local scope", [
                labels.label_command("List variables by kind and verify nested local scope behavior"),
                o.create_var_scope([
                    o.set_scope_var("a", "1"),
                    o.set_scope_var("b", "2"),
                    t.assert_unstrict_equal(o.all_variables(kind_all), '["a","b"]'),
                    t.assert_unstrict_equal(o.all_variables(kind_local), '["a","b"]'),
                    t.assert_unstrict_equal(o.all_variables(kind_global), '[]'),

                    o.create_var_scope([
                        labels.label_command("In a fresh local scope, inherited names are visible in all scopes"),
                        t.assert_unstrict_equal(o.all_variables(kind_all), '["a","b"]'),
                        t.assert_unstrict_equal(o.all_variables(kind_local), '[]'),
                        t.assert_unstrict_equal(o.all_variables(kind_global), '[]'),

                        o.set_scope_var("c", "3"),
                        t.assert_unstrict_equal(o.all_variables(kind_all), '["a","b","c"]'),
                        t.assert_unstrict_equal(o.all_variables(kind_local), '["c"]'),
                        t.assert_unstrict_equal(o.all_variables(kind_global), '[]'),
                    ]),

                    t.assert_not(o.scope_var_exists("c", kind_local)),
                    t.assert_not(o.scope_var_exists("c", kind_all)),
                ]),
            ]),

            t.test_scope("bind global + non-local", [
                labels.label_command("Bind global in an inner scope and mutate it"),
                o.set_scope_var("globalCounter", "0"),
                o.create_var_scope([
                    o.bind_var_to_scope(bind_global, "globalCounter"),
                    o.set_scope_var("globalCounter", "1"),
                ]),
                t.assert_strict_equal(o.get_scope_var("globalCounter"), "1"),

                labels.label_command("Bind non-local variable in nested local scopes and mutate it"),
                o.create_var_scope([
                    o.set_scope_var("outerLocal", "A"),
                    o.create_var_scope([
                        o.bind_var_to_scope("non-local", "outerLocal"),
                        o.set_scope_var("outerLocal", "B"),
                    ]),
                    t.assert_strict_equal(o.get_scope_var("outerLocal"), "B"),
                ]),
            ]),

            t.test_scope("bind error paths", [
                labels.label_command("Binding a missing global/non-local variable should throw"),
                t.assert_throws([
                    o.bind_var_to_scope(bind_global, "missingGlobal"),
                ]),
                o.create_var_scope([
                    t.assert_throws([
                        o.bind_var_to_scope("non-local", "missingNonLocal"),
                    ]),
                ]),
            ]),

            t.test_scope("createVarScope cleanup on error", [
                labels.label_command("exitUserScope must run even if an error is thrown inside the scope"),
                o.create_var_scope([
                    o.set_scope_var("outerVar", "present"),
                    t.assert_throws([
                        o.create_var_scope([
                            o.set_scope_var("innerVar", "value"),
                            o.execute_expression(o.get_scope_var("__missing_var__")),
                        ]),
                    ]),
                    labels.label_command("Inner variable should be gone after error"),
                    t.assert_not(o.scope_var_exists("innerVar", kind_all)),
                    labels.label_command("Outer variable should still exist"),
                    t.assert_(o.scope_var_exists("outerVar", kind_all)),
                ]),
            ]),
        ]),
    )

    return create_test_project(scripts=[script], extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_function_blocks() -> p.FRProject:
    script = create_script(
        h.event.whenflagclicked(),
        t.test_scope("Function Blocks", [
            t.test_scope("basic function", [
                labels.label_command("Define a simple function that returns a constant"),
                o.create_function_at("myFunc", [
                    o.return_value("hello"),
                ]),
                labels.label_command("Call the function with no arguments"),
                t.assert_strict_equal(
                    o.call_function("myFunc", "[]"),
                    "hello"
                ),
            ]),

            t.test_scope("function with args", [
                labels.label_command("Configure and define function with two arguments"),
                o.configure_next_function_args('["greeting", "name"]', '[]'),
                o.create_function_at("greet", [
                    o.return_value(h.operator.join3(o.get_scope_var("greeting"), " ", o.get_scope_var("name"))),
                ]),
                labels.label_command("Call with two arguments passed as array"),
                t.assert_strict_equal(
                    o.call_function("greet", '["Hello", "Ada"]'),
                    "Hello Ada"
                ),
            ]),

            t.test_scope("default arguments", [
                labels.label_command("Configure function with required arg and default trailing arg"),
                o.configure_next_function_args('["person", "greeting"]', '["Hi"]'),
                o.create_function_at("sayHi", [
                    o.return_value(h.operator.join3(o.get_scope_var("greeting"), " ", o.get_scope_var("person"))),
                ]),
                labels.label_command("Call with only first arg (second uses default Hi)"),
                t.assert_strict_equal(
                    o.call_function("sayHi", '["Bob"]'),
                    "Hi Bob"
                ),
                labels.label_command("Call with both args (overrides default)"),
                t.assert_strict_equal(
                    o.call_function("sayHi", '["Bob", "Hey"]'),
                    "Hey Bob"
                ),
            ]),

            t.test_scope("return behavior", [
                labels.label_command("Function returns early inside an if-block; later return must not run"),
                o.configure_next_function_args('["flag"]', '[]'),
                o.create_function_at("conditional", [
                    h.control.if_(
                        h.operator.equals(o.get_scope_var("flag"), "yes"),
                        [o.return_value("early")],
                    ),
                    o.return_value("late"),
                ]),
                labels.label_command("When condition is true, early return fires"),
                t.assert_strict_equal(
                    o.call_function("conditional", '["yes"]'),
                    "early"
                ),
                labels.label_command("When condition is false, falls through to second return"),
                t.assert_strict_equal(
                    o.call_function("conditional", '["no"]'),
                    "late"
                ),
            ]),

            t.test_scope("closures", [
                labels.label_command("Outer function accepts prefix, returns inner function that closes over it"),
                o.configure_next_function_args('["prefix"]', '[]'),
                o.create_function_at("makeGreeter", [
                    labels.label_command("Configure inner function arg before defining it"),
                    o.configure_next_function_args('["name"]', '[]'),
                    o.return_value(o.create_function_named("greeter", [
                        o.return_value(h.operator.join3(o.get_scope_var("prefix"), ", ", o.get_scope_var("name"))),
                    ])),
                ]),
                labels.label_command("Each call to makeGreeter produces an independent greeter"),
                o.set_scope_var("hiGreeter", o.call_function("makeGreeter", '["Hi"]')),
                o.set_scope_var("heyGreeter", o.call_function("makeGreeter", '["Hey"]')),
                t.assert_strict_equal(
                    o.call_function("hiGreeter", '["Ada"]'),
                    "Hi, Ada"
                ),
                t.assert_strict_equal(
                    o.call_function("heyGreeter", '["Ada"]'),
                    "Hey, Ada"
                ),
                labels.label_command("Captured prefix is independent per closure instance"),
                t.assert_strict_equal(
                    o.call_function("hiGreeter", '["Bob"]'),
                    "Hi, Bob"
                ),
            ]),

            t.test_scope("create function named", [
                labels.label_command("Create a function as a reporter block (returns the function)"),
                o.set_scope_var("myFunc", o.create_function_named("anonFunc", [
                    o.return_value("from-anon"),
                ])),
                labels.label_command("Call the stored function"),
                t.assert_strict_equal(
                    o.call_function("myFunc", "[]"),
                    "from-anon"
                ),
            ]),

            t.test_scope("error: wrong arg count", [
                labels.label_command("Function that accepts no arguments"),
                o.create_function_at("noArgs", [
                    o.return_value("done"),
                ]),
                labels.label_command("Calling with extra arguments should throw"),
                t.assert_throws([
                    o.execute_expression(o.call_function("noArgs", '["extra"]')),
                ]),
                labels.label_command("Function that requires one argument"),
                o.configure_next_function_args('["required"]', '[]'),
                o.create_function_at("oneArg", [
                    o.return_value(o.get_scope_var("required")),
                ]),
                labels.label_command("Calling with no arguments should throw"),
                t.assert_throws([
                    o.execute_expression(o.call_function("oneArg", "[]")),
                ]),
            ]),
        ]),
    )

    return create_test_project(scripts=[script], extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_utilities_blocks() -> p.FRProject:
    script = create_script(
        h.event.whenflagclicked(),
        t.test_scope("Utilities Blocks", [

            # ------------------------------------------------------------------ #
            t.test_scope("nothing", [
                labels.label_command("Nothing is its own type"),
                t.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
                labels.label_command("Nothing equals itself via string comparison"),
                t.assert_unstrict_equal(o.nothing(), o.nothing()),
                labels.label_command("Nothing is identical to itself (same singleton)"),
                t.assert_(o.check_identity(o.nothing(), o.nothing())),
                labels.label_command("Nothing is not identical to any other value"),
                t.assert_not(o.check_identity(o.nothing(), "0")),
                t.assert_not(o.check_identity(o.nothing(), "")),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("typeof_value", [
                labels.label_command("Primitive types"),
                t.assert_unstrict_equal(o.typeof_value("hello"), "String"),
                t.assert_unstrict_equal(o.typeof_value("42"), "Number"),
                t.assert_unstrict_equal(o.typeof_value(h.operator.true_boolean()), "Boolean"),
                labels.label_command("GCE types"),
                t.assert_unstrict_equal(o.typeof_value(o.nothing()), "Nothing (GCE)"),
                t.assert_unstrict_equal(
                    o.typeof_value(o.create_function_named("f", [o.return_value("x")])),
                    "Function (GCE)"
                ),
                t.assert_unstrict_equal(
                    o.typeof_value(o.create_class_named("MyClass", [])),
                    "Class (GCE)"
                ),
                t.assert_unstrict_equal(
                    o.typeof_value(o.create_instance(o.create_class_named("MyClass", []), '[]')),
                    "Class Instance (GCE)"
                ),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("typeof_value_is_menu", [
                labels.label_command("Correct type returns true"),
                t.assert_(o.typeof_value_is_menu("hello", "String")),
                t.assert_(o.typeof_value_is_menu("42", "Number")),
                t.assert_(o.typeof_value_is_menu(h.operator.true_boolean(), "Boolean")),
                t.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
                labels.label_command("Wrong type returns false"),
                t.assert_not(o.typeof_value_is_menu("hello", "Number")),
                t.assert_not(o.typeof_value_is_menu("42", "String")),
                t.assert_not(o.typeof_value_is_menu(o.nothing(), "String")),
                labels.label_command("typeof_value_is_menu is consistent with typeof_value"),
                o.create_var_scope([
                    o.set_scope_var("fn", o.create_function_named("g", [o.return_value("y")])),
                    t.assert_(o.typeof_value_is_menu(o.get_scope_var("fn"), "Function (GCE)")),
                    t.assert_not(o.typeof_value_is_menu(o.get_scope_var("fn"), "Class (GCE)")),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("typeof_value_selection", [
                labels.label_command("The reporter returns the menu value as a string"),
                t.assert_unstrict_equal(o.typeof_value_selection("String"), "String"),
                t.assert_unstrict_equal(o.typeof_value_selection("Nothing (GCE)"), "Nothing (GCE)"),
                t.assert_unstrict_equal(o.typeof_value_selection("Function (GCE)"), "Function (GCE)"),
                labels.label_command("Result matches typeof_value output"),
                t.assert_(h.operator.equals(o.typeof_value(o.nothing()), o.typeof_value_selection("Nothing (GCE)"))),
                t.assert_(h.operator.equals(o.typeof_value("test"), o.typeof_value_selection("String"))),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("object_as_string", [
                labels.label_command("Primitive values stringify as-is"),
                t.assert_unstrict_equal(o.object_as_string("hello"), "hello"),
                t.assert_unstrict_equal(o.object_as_string("42"), "42"),
                labels.label_command("Nothing stringifies to its representation"),
                t.assert_does_not_throw([
                    o.execute_expression(o.object_as_string(o.nothing())),
                ]),
                labels.label_command("Instance without as-string method: no error, returns some string"),
                o.create_var_scope([
                    o.create_class_at("Plain", []),
                    o.set_scope_var("inst", o.create_instance("Plain", '[]')),
                    t.assert_does_not_throw([
                        o.execute_expression(o.object_as_string(o.get_scope_var("inst"))),
                    ]),
                    t.assert_(o.typeof_value_is_menu(o.object_as_string(o.get_scope_var("inst")), "String")),
                ]),
                labels.label_command("Instance WITH as-string method: calls the method"),
                o.create_var_scope([
                    o.create_class_at("Stringable", [
                        o.define_special_method("as string", [
                            o.return_value("custom-string"),
                        ]),
                    ]),
                    o.set_scope_var("inst", o.create_instance("Stringable", '[]')),
                    t.assert_unstrict_equal(o.object_as_string(o.get_scope_var("inst")), "custom-string"),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("check_identity", [
                labels.label_command("Two separate instances of the same class are NOT identical"),
                o.create_var_scope([
                    o.create_class_at("MyClass", []),
                    o.set_scope_var("a", o.create_instance("MyClass", '[]')),
                    o.set_scope_var("b", o.create_instance("MyClass", '[]')),
                    t.assert_not(o.check_identity(o.get_scope_var("a"), o.get_scope_var("b"))),
                ]),
                labels.label_command("The same instance stored in two variables IS identical"),
                o.create_var_scope([
                    o.create_class_at("MyClass", []),
                    o.set_scope_var("a", o.create_instance("MyClass", '[]')),
                    o.set_scope_var("b", o.get_scope_var("a")),
                    t.assert_(o.check_identity(o.get_scope_var("a"), o.get_scope_var("b"))),
                ]),
                labels.label_command("Nothing is identical to itself"),
                t.assert_(o.check_identity(o.nothing(), o.nothing())),
                labels.label_command("Nothing is not identical to a function"),
                t.assert_not(o.check_identity(
                    o.nothing(),
                    o.create_function_named("h", [o.return_value("z")]),
                )),
                labels.label_command("Two separately created functions are NOT identical"),
                o.create_var_scope([
                    o.set_scope_var("f1", o.create_function_named("fn1", [o.return_value("r")])),
                    o.set_scope_var("f2", o.create_function_named("fn2", [o.return_value("r")])),
                    t.assert_not(o.check_identity(o.get_scope_var("f1"), o.get_scope_var("f2"))),
                ]),
                labels.label_command("Primitive strings identical"),
                t.assert_(o.check_identity("hello", "hello")),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("execute_expression", [
                labels.label_command("Evaluate a reporter block as a command (no error)"),
                t.assert_does_not_throw([
                    o.execute_expression(o.nothing()),
                ]),
                labels.label_command("execute_expression propagates errors from its subexpression"),
                t.assert_throws([
                    o.execute_expression(o.get_scope_var("__missing__")),
                ]),
                labels.label_command("execute_expression can evaluate any reporter"),
                t.assert_does_not_throw([
                    o.execute_expression(o.typeof_value("test")),
                ]),
                t.assert_does_not_throw([
                    o.execute_expression(o.object_as_string("hello")),
                ]),
                labels.label_command("execute_expression can call a function and discard the return value"),
                o.create_var_scope([
                    o.create_function_at("noopFn", [
                        o.return_value("done"),
                    ]),
                    t.assert_does_not_throw([
                        o.execute_expression(o.call_function("noopFn", '[]')),
                    ]),
                ]),
            ]),

        ]),
    )

    return create_test_project(scripts=[script], extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def main() -> None:
    configure()
    test_projects_dir = Path("test_projects")
    #write_project_to_file(test_TypeChecker(), test_projects_dir / "test_TypeChecker.pmp")
    #write_project_to_file(test_Cast(), test_projects_dir / "test_Cast.pmp")
    write_project_to_file(test_scoped_variables_blocks(), test_projects_dir / "test_scoped_variables_blocks.pmp")
    write_project_to_file(test_function_blocks(), test_projects_dir / "test_function_blocks.pmp")
    write_project_to_file(test_utilities_blocks(), test_projects_dir / "test_utilities_blocks.pmp")

if __name__ == "__main__":
    main()
