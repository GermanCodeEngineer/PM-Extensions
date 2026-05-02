from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import copy
from gceutils import AbstractTreePath, grepr_dataclass
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



@grepr_dataclass()
class TestProject:
    blocks: list[p.SRBlock]
    extension_ids: list[str]

    @staticmethod
    def join_projects(projects: list[TestProject]) -> TestProject:
        all_blocks = []
        all_extension_ids = set()
        for project in projects:
            assert len(project.blocks) == 1, "Expected one top level test_scope block"
            assert project.blocks[0].opcode == "&gceTestRunner::test scope named (NAME) {SUBSTACK}", "Expected top level block to be a test_scope"
            all_blocks.extend(project.blocks)
            all_extension_ids.update(project.extension_ids)
        return TestProject(blocks=all_blocks, extension_ids=list(all_extension_ids))
    
def convert_project(test_project: TestProject) -> p.FRProject:
    srproject = p.SRProject.create_empty()
    srsprite = p.SRSprite.create_empty("Test")
    srproject.sprites.append(srsprite)
    srproject.sprite_layer_stack.append(srsprite.uuid)

    blocks = copy.copy(test_project.blocks)
    blocks.insert(0, h.event.whenflagclicked())
    srsprite.scripts = [p.SRScript(position=(0, 0), blocks=blocks)]

    srproject.extensions = []
    for id in test_project.extension_ids:
        url = EXTENSION_SOURCES[id]
        srproject.extensions.append(
            p.SRCustomExtension(id, url) if url is not None else p.SRBuiltinExtension(id=id)
        )
    

    opcode_info_copy = p.info_api.opcode_info.copy()
    info_api_copy = OpcodeInfoAPI(opcode_info_copy)
    srproject.add_all_extensions_to_info_api(info_api_copy)

    # Tricks to avoid errors for invalid extension URLs (currently too strict)
    extensions_before = copy.deepcopy(srproject.extensions)
    for extension in srproject.extensions:
        extension.url = "https://example.com/"

    srproject.validate(AbstractTreePath(), info_api_copy)
    srproject.extensions = extensions_before

    frproject = srproject.to_first(info_api_copy)
    return frproject

def write_project_to_file(project: TestProject, output_file: Path) -> None:
    frproject = convert_project(project)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    frproject.to_file(str(output_file))

def test_TypeChecker() -> TestProject:
    blocks = [
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
    ]
    
    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto", "SPjavascriptV2", "agBuffer", "ddeDateFormat", 
        "ddeDateFormatV2", "divAlgEffects", "divIterator", "dogeiscutObject", "dogeiscutRegularExpressions", 
        "dogeiscutSet", "fruitsPaintUtils", "jwArray", "jwColor", "jwDate", "jwLambda", "jwNum", "jwTargets", 
        "jwVector", "jwXML", "newCanvas", "steve0greatnesstimers"
    ])

def test_Cast() -> TestProject:
    blocks = [
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
    ]
    
    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto", "SPjavascriptV2",
    ])

def test_scoped_variables_blocks() -> TestProject:
    kind_all = "all scopes"
    kind_local = "local scope"
    kind_global = "global scope"
    bind_global = "global"

    blocks = [
        t.test_scope("Scoped Variables Blocks", [
            t.test_scope("set/get/exists", [
                t.test_scope("Set and read a local variable", [
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
            ]),

            t.test_scope("delete var", [
                t.test_scope("Delete removes the variable from the current scope", [
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
            ]),

            t.test_scope("all variables + local scope", [
                t.test_scope("List variables by kind and verify nested local scope behavior", [
                    o.create_var_scope([
                        o.set_scope_var("a", "1"),
                        o.set_scope_var("b", "2"),
                        t.assert_unstrict_equal(o.all_variables(kind_all), '["a","b"]'),
                        t.assert_unstrict_equal(o.all_variables(kind_local), '["a","b"]'),
                        t.assert_unstrict_equal(o.all_variables(kind_global), '[]'),

                        o.create_var_scope([
                            t.test_scope("In a fresh local scope, inherited names are visible in all scopes", [
                                t.assert_unstrict_equal(o.all_variables(kind_all), '["a","b"]'),
                                t.assert_unstrict_equal(o.all_variables(kind_local), '[]'),
                                t.assert_unstrict_equal(o.all_variables(kind_global), '[]'),
                                o.set_scope_var("c", "3"),
                                t.assert_unstrict_equal(o.all_variables(kind_all), '["a","b","c"]'),
                                t.assert_unstrict_equal(o.all_variables(kind_local), '["c"]'),
                                t.assert_unstrict_equal(o.all_variables(kind_global), '[]'),
                            ]),
                        ]),

                        t.assert_not(o.scope_var_exists("c", kind_local)),
                        t.assert_not(o.scope_var_exists("c", kind_all)),
                    ]),
                ]),
            ]),

            t.test_scope("bind global + non-local", [
                t.test_scope("Bind global in an inner scope and mutate it", [
                    o.run_with_separate_globals([
                        o.set_scope_var("globalCounter", "0"),
                        o.create_var_scope([
                            o.bind_var_to_scope(bind_global, "globalCounter"),
                            o.set_scope_var("globalCounter", "1"),
                        ]),
                        t.assert_strict_equal(o.get_scope_var("globalCounter"), "1"),
                    ]),
                ]),
                t.test_scope("Bind non-local variable in nested local scopes and mutate it", [
                    o.create_var_scope([
                        o.set_scope_var("outerLocal", "A"),
                        o.create_var_scope([
                            o.bind_var_to_scope("non-local", "outerLocal"),
                            o.set_scope_var("outerLocal", "B"),
                        ]),
                        t.assert_strict_equal(o.get_scope_var("outerLocal"), "B"),
                    ]),
                ]),
            ]),

            t.test_scope("bind error paths", [
                t.test_scope("Binding a missing global/non-local variable should throw", [
                    t.assert_throws([
                        o.bind_var_to_scope(bind_global, "missingGlobal"),
                    ]),
                    o.create_var_scope([
                        t.assert_throws([
                            o.bind_var_to_scope("non-local", "missingNonLocal"),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("createVarScope cleanup on error", [
                t.test_scope("exitUserScope must run even if an error is thrown inside the scope", [
                    o.create_var_scope([
                        o.set_scope_var("outerVar", "present"),
                        o.create_var_scope([
                            o.set_scope_var("innerVar", "value"),
                            t.assert_throws([
                                o.execute_expression(o.get_scope_var("__missing_var__")),
                            ]),
                        ]),
                        t.test_scope("Inner variable should be gone after error", [
                            t.assert_not(o.scope_var_exists("innerVar", kind_all)),
                        ]),
                        t.test_scope("Outer variable should still exist", [
                            t.assert_(o.scope_var_exists("outerVar", kind_all)),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("scopeVarExists with 3-level nesting", [
                t.test_scope("Verify kindLocal, kindAll, kindGlobal across 3 scopes", [
                    o.run_with_separate_globals([
                        o.set_scope_var("globalVar", "g"),
                        o.create_var_scope([
                            o.set_scope_var("level1", "L1"),
                            o.create_var_scope([
                                o.set_scope_var("level2", "L2"),
                                o.create_var_scope([
                                    o.set_scope_var("level3", "L3"),
                                    t.test_scope("Innermost: level3 is local, others are not", [
                                        t.assert_(o.scope_var_exists("level3", kind_local)),
                                        t.assert_not(o.scope_var_exists("level1", kind_local)),
                                        t.assert_not(o.scope_var_exists("level2", kind_local)),
                                    ]),
                                    t.test_scope("All three are visible via kindAll", [
                                        t.assert_(o.scope_var_exists("level1", kind_all)),
                                        t.assert_(o.scope_var_exists("level2", kind_all)),
                                        t.assert_(o.scope_var_exists("level3", kind_all)),
                                    ]),
                                    t.test_scope("Global is visible via kindGlobal and kindAll", [
                                        t.assert_(o.scope_var_exists("globalVar", kind_global)),
                                        t.assert_(o.scope_var_exists("globalVar", kind_all)),
                                    ]),
                                    t.test_scope("Local vars are NOT global", [
                                        t.assert_not(o.scope_var_exists("level3", kind_global)),
                                        t.assert_not(o.scope_var_exists("level2", kind_global)),
                                    ]),
                                ]),
                            ]),
                            t.test_scope("level2 and level3 gone after exiting their scopes", [
                                t.assert_not(o.scope_var_exists("level2", kind_all)),
                                t.assert_not(o.scope_var_exists("level3", kind_all)),
                                t.assert_(o.scope_var_exists("level1", kind_local)),
                            ]),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("runWithSeparateGlobals", [
                t.test_scope("Outer locals are not visible inside", [
                    o.create_var_scope([
                        o.set_scope_var("outerLocal", "outer"),
                        o.run_with_separate_globals([
                            t.assert_not(o.scope_var_exists("outerLocal", kind_all)),
                            t.assert_not(o.scope_var_exists("outerLocal", kind_local)),
                            t.assert_not(o.scope_var_exists("outerLocal", kind_global)),
                            t.assert_throws([
                                o.execute_expression(o.get_scope_var("outerLocal")),
                            ]),
                        ]),
                    ]),
                ]),
                t.test_scope("Outer globals are not visible inside", [
                    o.set_scope_var("outerGlobal", "outerGlobalValue"),
                    o.run_with_separate_globals([
                        t.assert_not(o.scope_var_exists("outerGlobal", kind_all)),
                        t.assert_not(o.scope_var_exists("outerGlobal", kind_global)),
                        t.assert_throws([
                            o.execute_expression(o.get_scope_var("outerGlobal")),
                        ]),
                    ]),
                    o.delete_scope_var("outerGlobal"),
                ]),
                t.test_scope("Writes inside do not affect outer locals", [
                    o.create_var_scope([
                        o.set_scope_var("sharedName", "before"),
                        o.run_with_separate_globals([
                            o.set_scope_var("sharedName", "inside"),
                            t.assert_strict_equal(o.get_scope_var("sharedName"), "inside"),
                        ]),
                        t.assert_strict_equal(o.get_scope_var("sharedName"), "before"),
                    ]),
                ]),
                t.test_scope("Writes inside do not affect outer globals", [
                    o.set_scope_var("sharedGlobal", "globalBefore"),
                    o.run_with_separate_globals([
                        o.set_scope_var("sharedGlobal", "globalInside"),
                        t.assert_strict_equal(o.get_scope_var("sharedGlobal"), "globalInside"),
                    ]),
                    t.assert_strict_equal(o.get_scope_var("sharedGlobal"), "globalBefore"),
                    o.delete_scope_var("sharedGlobal"),
                ]),
                t.test_scope("Inner globals and locals start empty", [
                    o.run_with_separate_globals([
                        t.assert_unstrict_equal(o.all_variables(kind_all), "[]"),
                        t.assert_unstrict_equal(o.all_variables(kind_global), "[]"),
                        t.assert_unstrict_equal(o.all_variables(kind_local), "[]"),
                    ]),
                ]),
                t.test_scope("Variables created inside are gone after block exits", [
                    o.run_with_separate_globals([
                        o.set_scope_var("innerOnly", "value"),
                    ]),
                    t.assert_not(o.scope_var_exists("innerOnly", kind_all)),
                ]),
                t.test_scope("Cleanup happens even if an error is thrown inside", [
                    t.assert_throws([
                        o.run_with_separate_globals([
                            o.set_scope_var("innerError", "value"),
                            o.execute_expression(o.get_scope_var("__missing__")),
                        ]),
                    ]),
                    t.assert_not(o.scope_var_exists("innerError", kind_all)),
                ]),
                t.test_scope("Nested runWithSeparateGlobals are fully independent", [
                    o.set_scope_var("outerG", "OG"),
                    o.run_with_separate_globals([
                        o.set_scope_var("middleG", "MG"),
                        o.run_with_separate_globals([
                            t.assert_not(o.scope_var_exists("outerG", kind_all)),
                            t.assert_not(o.scope_var_exists("middleG", kind_all)),
                        ]),
                        t.assert_(o.scope_var_exists("middleG", kind_global)),
                        t.assert_not(o.scope_var_exists("outerG", kind_all)),
                    ]),
                    t.assert_(o.scope_var_exists("outerG", kind_global)),
                    t.assert_not(o.scope_var_exists("middleG", kind_all)),
                    o.delete_scope_var("outerG")
                ]),
            ]),
        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_function_blocks() -> TestProject:
    blocks = [
        t.test_scope("Function Blocks", [
            t.test_scope("basic function", [
                t.test_scope("Define a simple function that returns a constant", [
                    o.create_function_at("myFunc", [
                        o.return_value("hello"),
                    ]),
                ]),
                t.test_scope("Call the function with no arguments", [
                    t.assert_strict_equal(
                        o.call_function("myFunc", "[]"),
                        "hello"
                    ),
                ]),
            ]),

            t.test_scope("function with args", [
                t.test_scope("Configure and define function with two arguments", [
                    o.configure_next_function_args('["greeting", "name"]', '[]'),
                    o.create_function_at("greet", [
                        o.return_value(h.operator.join3(o.get_scope_var("greeting"), " ", o.get_scope_var("name"))),
                    ]),
                ]),
                t.test_scope("Call with two arguments passed as array", [
                    t.assert_strict_equal(
                        o.call_function("greet", '["Hello", "Ada"]'),
                        "Hello Ada"
                    ),
                ]),
            ]),

            t.test_scope("default arguments", [
                t.test_scope("Configure function with required arg and default trailing arg", [
                    o.configure_next_function_args('["person", "greeting"]', '["Hi"]'),
                    o.create_function_at("sayHi", [
                        o.return_value(h.operator.join3(o.get_scope_var("greeting"), " ", o.get_scope_var("person"))),
                    ]),
                ]),
                t.test_scope("Call with only first arg (second uses default Hi)", [
                    t.assert_strict_equal(
                        o.call_function("sayHi", '["Bob"]'),
                        "Hi Bob"
                    ),
                ]),
                t.test_scope("Call with both args (overrides default)", [
                    t.assert_strict_equal(
                        o.call_function("sayHi", '["Bob", "Hey"]'),
                        "Hey Bob"
                    ),
                ]),
            ]),

            t.test_scope("return behavior", [
                t.test_scope("Function returns early inside an if-block; later return must not run", [
                    o.configure_next_function_args('["flag"]', '[]'),
                    o.create_function_at("conditional", [
                        h.control.if_(
                            h.operator.equals(o.get_scope_var("flag"), "yes"),
                            [o.return_value("early")],
                        ),
                        o.return_value("late"),
                    ]),
                ]),
                t.test_scope("When condition is true, early return fires", [
                    t.assert_strict_equal(
                        o.call_function("conditional", '["yes"]'),
                        "early"
                    ),
                ]),
                t.test_scope("When condition is false, falls through to second return", [
                    t.assert_strict_equal(
                        o.call_function("conditional", '["no"]'),
                        "late"
                    ),
                ]),
            ]),

            t.test_scope("closures", [o.run_with_separate_globals([
                t.test_scope("Outer function accepts prefix, returns inner function that closes over it", [
                    o.configure_next_function_args('["prefix"]', '[]'),
                    o.create_function_at("makeGreeter", [
                        t.test_scope("Configure inner function arg before defining it", [
                            o.configure_next_function_args('["name"]', '[]'),
                            o.return_value(o.create_function_named("greeter", [
                                o.return_value(h.operator.join3(o.get_scope_var("prefix"), ", ", o.get_scope_var("name"))),
                            ])),
                        ]),
                    ]),
                ]),
                t.test_scope("Each call to makeGreeter produces an independent greeter", [
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
                ]),
                t.test_scope("Captured prefix is independent per closure instance", [
                    t.assert_strict_equal(
                        o.call_function("hiGreeter", '["Bob"]'),
                        "Hi, Bob"
                    ),
                ]),
            ])]),

            t.test_scope("create function named", [o.run_with_separate_globals([
                t.test_scope("Create a function as a reporter block (returns the function)", [
                    o.set_scope_var("myFunc", o.create_function_named("anonFunc", [
                        o.return_value("from-anon"),
                    ])),
                ]),
                t.test_scope("Call the stored function", [
                    t.assert_strict_equal(
                        o.call_function("myFunc", "[]"),
                        "from-anon"
                    ),
                ]),
            ])]),

            t.test_scope("error: wrong arg count", [
                t.test_scope("Function that accepts no arguments", [
                    o.create_function_at("noArgs", [
                        o.return_value("done"),
                    ]),
                ]),
                t.test_scope("Calling with extra arguments should throw", [
                    t.assert_throws([
                        o.execute_expression(o.call_function("noArgs", '["extra"]')),
                    ]),
                ]),
                t.test_scope("Function that requires one argument", [
                    o.configure_next_function_args('["required"]', '[]'),
                    o.create_function_at("oneArg", [
                        o.return_value(o.get_scope_var("required")),
                    ]),
                ]),
                t.test_scope("Calling with no arguments should throw", [
                    t.assert_throws([
                        o.execute_expression(o.call_function("oneArg", "[]")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("var scope inside function body", [
                t.test_scope("createVarScope inside a function is isolated per call", [
                    o.configure_next_function_args('["val"]', '[]'),
                    o.create_function_at("withScope", [
                        o.create_var_scope([
                            o.set_scope_var("inner", o.get_scope_var("val")),
                            o.return_value(o.get_scope_var("inner")),
                        ]),
                    ]),
                ]),
                t.test_scope("First call", [
                    t.assert_strict_equal(o.call_function("withScope", '["first"]'), "first"),
                ]),
                t.test_scope("Second call — inner var is fresh each call", [
                    t.assert_strict_equal(o.call_function("withScope", '["second"]'), "second"),
                ]),
                t.test_scope("Inner scope var is not visible outside the function", [
                    t.assert_not(o.scope_var_exists("inner", "all scopes")),
                ]),
            ]),
        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_utilities_blocks() -> TestProject:
    blocks = [
        t.test_scope("Utilities Blocks", [

            # ------------------------------------------------------------------ #
            t.test_scope("nothing", [
                t.test_scope("Nothing is its own type", [
                    t.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
                ]),
                t.test_scope("Nothing equals itself via string comparison", [
                    t.assert_unstrict_equal(o.nothing(), o.nothing()),
                ]),
                t.test_scope("Nothing is identical to itself (same singleton)", [
                    t.assert_(o.check_identity(o.nothing(), o.nothing())),
                ]),
                t.test_scope("Nothing is not identical to any other value", [
                    t.assert_not(o.check_identity(o.nothing(), "0")),
                    t.assert_not(o.check_identity(o.nothing(), "")),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("typeofValue", [
                t.test_scope("Primitive types", [
                    t.assert_unstrict_equal(o.typeof_value("hello"), o.typeof_value_selection("String")),
                    t.assert_unstrict_equal(o.typeof_value("42"), o.typeof_value_selection("Number")),
                    t.assert_unstrict_equal(o.typeof_value(h.operator.true_boolean()), o.typeof_value_selection("Boolean")),
                ]),
                t.test_scope("GCE types", [
                    t.assert_unstrict_equal(o.typeof_value(o.nothing()), o.typeof_value_selection("Nothing (GCE)")),
                    t.assert_unstrict_equal(
                        o.typeof_value(o.create_function_named("f", [o.return_value("x")])),
                        o.typeof_value_selection("Function (GCE)")
                    ),
                    t.assert_unstrict_equal(
                        o.typeof_value(o.create_class_named("MyClass", [])),
                        o.typeof_value_selection("Class (GCE)")
                    ),
                    t.assert_unstrict_equal(
                        o.typeof_value(o.create_instance(o.create_class_named("MyClass", []), '[]')),
                        o.typeof_value_selection("Class Instance (GCE)")
                    ),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("typeofValueIsMenu", [
                t.test_scope("Correct type returns true", [
                    t.assert_(o.typeof_value_is_menu("hello", "String")),
                    t.assert_(o.typeof_value_is_menu("42", "Number")),
                    t.assert_(o.typeof_value_is_menu(h.operator.true_boolean(), "Boolean")),
                    t.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
                ]),
                t.test_scope("Wrong type returns false", [
                    t.assert_not(o.typeof_value_is_menu("hello", "Number")),
                    t.assert_not(o.typeof_value_is_menu("42", "String")),
                    t.assert_not(o.typeof_value_is_menu(o.nothing(), "String")),
                ]),
                t.test_scope("typeofValueIsMenu is consistent with typeofValue", [
                    o.create_var_scope([
                        o.set_scope_var("fn", o.create_function_named("g", [o.return_value("y")])),
                        t.assert_(o.typeof_value_is_menu(o.get_scope_var("fn"), "Function (GCE)")),
                        t.assert_not(o.typeof_value_is_menu(o.get_scope_var("fn"), "Class (GCE)")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("typeofValueSelection", [
                t.test_scope("The reporter returns the menu value as a string", [
                    t.assert_unstrict_equal(o.typeof_value_selection("String"), "String"),
                    t.assert_unstrict_equal(o.typeof_value_selection("Nothing (GCE)"), "Nothing (GCE)"),
                    t.assert_unstrict_equal(o.typeof_value_selection("Function (GCE)"), "Function (GCE)"),
                ]),
                t.test_scope("Result matches typeofValue output", [
                    t.assert_(h.operator.equals(o.typeof_value(o.nothing()), o.typeof_value_selection("Nothing (GCE)"))),
                    t.assert_(h.operator.equals(o.typeof_value("test"), o.typeof_value_selection("String"))),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("objectAsString", [
                t.test_scope("Primitive values stringify as-is", [
                    t.assert_unstrict_equal(o.object_as_string("hello"), "hello"),
                    t.assert_unstrict_equal(o.object_as_string("42"), "42"),
                ]),
                t.test_scope("Nothing stringifies to its representation", [
                    t.assert_does_not_throw([
                        o.execute_expression(o.object_as_string(o.nothing())),
                    ]),
                ]),
                t.test_scope("Instance without as-string method: no error, returns some string", [
                    o.create_var_scope([
                        o.create_class_at("Plain", []),
                        o.set_scope_var("inst", o.create_instance("Plain", '[]')),
                        t.assert_does_not_throw([
                            o.execute_expression(o.object_as_string(o.get_scope_var("inst"))),
                        ]),
                        t.assert_(o.typeof_value_is_menu(o.object_as_string(o.get_scope_var("inst")), "String")),
                    ]),
                ]),
                t.test_scope("Instance WITH as-string method: calls the method", [
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
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("checkIdentity", [
                t.test_scope("Two separate instances of the same class are NOT identical", [
                    o.create_var_scope([
                        o.create_class_at("MyClass", []),
                        o.set_scope_var("a", o.create_instance("MyClass", '[]')),
                        o.set_scope_var("b", o.create_instance("MyClass", '[]')),
                        t.assert_not(o.check_identity(o.get_scope_var("a"), o.get_scope_var("b"))),
                    ]),
                ]),
                t.test_scope("The same instance stored in two variables IS identical", [
                    o.create_var_scope([
                        o.create_class_at("MyClass", []),
                        o.set_scope_var("a", o.create_instance("MyClass", '[]')),
                        o.set_scope_var("b", o.get_scope_var("a")),
                        t.assert_(o.check_identity(o.get_scope_var("a"), o.get_scope_var("b"))),
                    ]),
                ]),
                t.test_scope("Nothing is identical to itself", [
                    t.assert_(o.check_identity(o.nothing(), o.nothing())),
                ]),
                t.test_scope("Nothing is not identical to a function", [
                    t.assert_not(o.check_identity(
                        o.nothing(),
                        o.create_function_named("h", [o.return_value("z")]),
                    )),
                ]),
                t.test_scope("Two separately created functions are NOT identical", [
                    o.create_var_scope([
                        o.set_scope_var("f1", o.create_function_named("fn1", [o.return_value("r")])),
                        o.set_scope_var("f2", o.create_function_named("fn2", [o.return_value("r")])),
                        t.assert_not(o.check_identity(o.get_scope_var("f1"), o.get_scope_var("f2"))),
                    ]),
                ]),
                t.test_scope("Primitive strings identical", [
                    t.assert_(o.check_identity("hello", "hello")),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("executeExpression", [
                t.test_scope("Evaluate a reporter block as a command (no error)", [
                    t.assert_does_not_throw([
                        o.execute_expression(o.nothing()),
                    ]),
                ]),
                t.test_scope("executeExpression propagates errors from its subexpression", [
                    t.assert_throws([
                        o.execute_expression(o.get_scope_var("__missing__")),
                    ]),
                ]),
                t.test_scope("executeExpression can evaluate any reporter", [
                    t.assert_does_not_throw([
                        o.execute_expression(o.typeof_value("test")),
                    ]),
                    t.assert_does_not_throw([
                        o.execute_expression(o.object_as_string("hello")),
                    ]),
                ]),
                t.test_scope("executeExpression can call a function and discard the return value", [
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

        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_instance_methods() -> TestProject:
    blocks = [
        t.test_scope("Instance Methods", [

            t.test_scope("basic method call", [
                t.test_scope("Define class with methods, call them on an instance", [
                    o.create_var_scope([
                        o.create_class_at("Greeter", [
                            o.configure_next_function_args('["name"]', '[]'),
                            o.define_instance_method("greet", [
                                o.return_value(h.operator.join3("Hello, ", o.get_scope_var("name"), "!")),
                            ]),
                            o.define_instance_method("getType", [
                                o.return_value(o.typeof_value(o.self())),
                            ]),
                            o.define_instance_method("getAttr", [
                                o.return_value(o.get_attribute("label", o.self())),
                            ]),
                        ]),
                        o.set_scope_var("g", o.create_instance("Greeter", '[]')),
                        o.set_attribute(o.get_scope_var("g"), "label", "test-label"),

                        t.test_scope("Method with arg", [
                            t.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "greet", '["World"]'),
                                "Hello, World!",
                            ),
                        ]),
                        t.test_scope("Same method with different arg", [
                            t.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "greet", '["Alice"]'),
                                "Hello, Alice!",
                            ),
                        ]),
                        t.test_scope("No-arg method returns correct type string", [
                            t.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "getType", '[]'),
                                o.typeof_value_selection("Class Instance (GCE)"),
                            ),
                        ]),
                        t.test_scope("Method reads self attribute", [
                            t.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "getAttr", '[]'),
                                "test-label",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("self is the correct instance", [
                t.test_scope("Two instances with different attribute values", [
                    o.create_var_scope([
                        o.create_class_at("Box", [
                            o.define_instance_method("describe", [
                                o.return_value(h.operator.join("Box-", o.get_attribute("id", o.self()))),
                            ]),
                        ]),
                        o.set_scope_var("b1", o.create_instance("Box", '[]')),
                        o.set_scope_var("b2", o.create_instance("Box", '[]')),
                        o.set_attribute(o.get_scope_var("b1"), "id", "AAA"),
                        o.set_attribute(o.get_scope_var("b2"), "id", "BBB"),
                        t.assert_unstrict_equal(o.call_method(o.get_scope_var("b1"), "describe", '[]'), "Box-AAA"),
                        t.assert_unstrict_equal(o.call_method(o.get_scope_var("b2"), "describe", '[]'), "Box-BBB"),
                        t.test_scope("self is distinct for each instance", [
                            t.assert_not(o.check_identity(o.get_scope_var("b1"), o.get_scope_var("b2"))),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("error cases", [
                t.test_scope("Calling an undefined method throws", [
                    o.create_var_scope([
                        o.create_class_at("Empty", []),
                        o.set_scope_var("e", o.create_instance("Empty", '[]')),
                        t.assert_throws([
                            o.execute_expression(o.call_method(o.get_scope_var("e"), "nonExistent", '[]')),
                        ]),
                    ]),
                ]),
                t.test_scope("Calling a method on a non-instance throws", [
                    t.assert_throws([
                        o.execute_expression(o.call_method("not-an-instance", "anyMethod", '[]')),
                    ]),
                ]),
            ]),

        ]),
    ]
    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_special_method_init() -> TestProject:
    blocks = [
        t.test_scope("Special Method: init", [

            t.test_scope("init sets attributes from args", [
                t.test_scope("Define class whose init sets x and y from positional args", [
                    o.create_var_scope([
                        o.create_class_at("Point", [
                            o.configure_next_function_args('["x","y"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self(), "x", o.get_scope_var("x")),
                                o.set_attribute(o.self(), "y", o.get_scope_var("y")),
                            ]),
                        ]),
                        o.set_scope_var("p", o.create_instance("Point", '["3","4"]')),
                        t.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("p")), "3"),
                        t.assert_unstrict_equal(o.get_attribute("y", o.get_scope_var("p")), "4"),
                        t.test_scope("Second instance has independent values", [
                            o.set_scope_var("q", o.create_instance("Point", '["10","20"]')),
                            t.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("q")), "10"),
                            t.assert_unstrict_equal(o.get_attribute("y", o.get_scope_var("q")), "20"),
                        ]),
                        t.test_scope("First instance unchanged after second is created", [
                            t.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("p")), "3"),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("init with default args", [
                t.test_scope("Defaults fill in when args omitted", [
                    o.create_var_scope([
                        o.create_class_at("Color", [
                            o.configure_next_function_args('["r","g","b"]', '["0","0","0"]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self(), "r", o.get_scope_var("r")),
                                o.set_attribute(o.self(), "g", o.get_scope_var("g")),
                                o.set_attribute(o.self(), "b", o.get_scope_var("b")),
                            ]),
                        ]),
                        t.test_scope("All defaults: r=0, g=0, b=0", [
                            o.set_scope_var("black", o.create_instance("Color", '[]')),
                            t.assert_unstrict_equal(o.get_attribute("r", o.get_scope_var("black")), "0"),
                            t.assert_unstrict_equal(o.get_attribute("g", o.get_scope_var("black")), "0"),
                            t.assert_unstrict_equal(o.get_attribute("b", o.get_scope_var("black")), "0"),
                        ]),
                        t.test_scope("Partial override: r=255", [
                            o.set_scope_var("red", o.create_instance("Color", '["255"]')),
                            t.assert_unstrict_equal(o.get_attribute("r", o.get_scope_var("red")), "255"),
                            t.assert_unstrict_equal(o.get_attribute("g", o.get_scope_var("red")), "0"),
                        ]),
                        t.test_scope("Full args", [
                            o.set_scope_var("custom", o.create_instance("Color", '["10","20","30"]')),
                            t.assert_unstrict_equal(o.get_attribute("b", o.get_scope_var("custom")), "30"),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("subclass init calls super init", [
                t.test_scope("Subclass init calls callSuperInitMethod", [
                    o.create_var_scope([
                        o.create_class_at("Shape", [
                            o.configure_next_function_args('["color"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self(), "color", o.get_scope_var("color")),
                            ]),
                        ]),
                        o.create_subclass_at("Circle", "Shape", [
                            o.configure_next_function_args('["radius","color"]', '[]'),
                            o.define_special_method("init", [
                                o.execute_expression(o.call_super_init_method('["blue"]')),
                                o.set_attribute(o.self(), "radius", o.get_scope_var("radius")),
                            ]),
                        ]),
                        o.set_scope_var("c", o.create_instance("Circle", '["5","ignored"]')),
                        t.test_scope("radius set by Circle init", [
                            t.assert_unstrict_equal(o.get_attribute("radius", o.get_scope_var("c")), "5"),
                        ]),
                        t.test_scope("color set by super (Shape) init with hardcoded value", [
                            t.assert_unstrict_equal(o.get_attribute("color", o.get_scope_var("c")), "blue"),
                        ]),
                    ]),
                ]),
            ]),

        ]),
    ]
    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_inheritance_and_super() -> TestProject:
    blocks = [
        t.test_scope("Inheritance and Super", [

            t.test_scope("isSubclass", [
                o.create_var_scope([
                    o.create_class_at("A", []),
                    o.create_subclass_at("B", "A", []),
                    o.create_subclass_at("C", "B", []),
                    t.test_scope("Direct subclass", [
                        t.assert_(o.is_subclass("B", "A")),
                    ]),
                    t.test_scope("Transitive subclass", [
                        t.assert_(o.is_subclass("C", "A")),
                        t.assert_(o.is_subclass("C", "B")),
                    ]),
                    t.test_scope("Reverse is false", [
                        t.assert_not(o.is_subclass("A", "B")),
                        t.assert_not(o.is_subclass("A", "C")),
                    ]),
                    t.test_scope("A class is not a subclass of itself", [
                        t.assert_not(o.is_subclass("A", "A")),
                    ]),
                ]),
            ]),

            t.test_scope("isInstance with inheritance", [
                o.create_var_scope([
                    o.create_class_at("Vehicle", []),
                    o.create_subclass_at("Car", "Vehicle", []),
                    o.set_scope_var("v", o.create_instance("Vehicle", '[]')),
                    o.set_scope_var("c", o.create_instance("Car", '[]')),
                    t.test_scope("Instance is instance of own class", [
                        t.assert_(o.is_instance(o.get_scope_var("v"), "Vehicle")),
                        t.assert_(o.is_instance(o.get_scope_var("c"), "Car")),
                    ]),
                    t.test_scope("Subclass instance is instance of superclass", [
                        t.assert_(o.is_instance(o.get_scope_var("c"), "Vehicle")),
                    ]),
                    t.test_scope("Superclass instance is NOT instance of subclass", [
                        t.assert_not(o.is_instance(o.get_scope_var("v"), "Car")),
                    ]),
                ]),
            ]),

            t.test_scope("method override and super", [
                o.create_var_scope([
                    o.create_class_at("Animal", [
                        o.define_instance_method("speak", [
                            o.return_value("generic sound"),
                        ]),
                        o.define_instance_method("breathe", [
                            o.return_value("breathing"),
                        ]),
                    ]),
                    o.create_subclass_at("Dog", "Animal", [
                        o.define_instance_method("speak", [
                            o.return_value(h.operator.join(
                                o.call_super_method("speak", '[]'),
                                " (but louder)",
                            )),
                        ]),
                    ]),
                    o.set_scope_var("a", o.create_instance("Animal", '[]')),
                    o.set_scope_var("d", o.create_instance("Dog", '[]')),
                    t.test_scope("Overridden method returns augmented result", [
                        t.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("d"), "speak", '[]'),
                            "generic sound (but louder)",
                        ),
                    ]),
                    t.test_scope("Parent method still returns original", [
                        t.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("a"), "speak", '[]'),
                            "generic sound",
                        ),
                    ]),
                    t.test_scope("Inherited (non-overridden) method works on subclass", [
                        t.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("d"), "breathe", '[]'),
                            "breathing",
                        ),
                    ]),
                ]),
            ]),

            t.test_scope("getSuperclass", [
                o.create_var_scope([
                    o.create_class_at("Base", []),
                    o.create_subclass_at("Child", "Base", []),
                    t.test_scope("Superclass of Child is Base", [
                        t.assert_text_in_value("Base", o.get_superclass("Child")),
                    ]),
                    t.test_scope("Superclass of Base is built-in Superclass", [
                        t.assert_text_in_value("Superclass", o.get_superclass("Base")),
                    ]),
                    t.test_scope("getSuperclass on a missing class name throws", [
                        t.assert_throws([
                            o.execute_expression(o.get_superclass("__no_such_class__")),
                        ]),
                    ]),
                ]),
            ]),

        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_getters_and_setters() -> TestProject:
    blocks = [
        t.test_scope("Getters and Setters", [

            t.test_scope("setter transforms and stores, getter retrieves", [
                t.test_scope("Setter prepends 'set:'; getter appends ':get'", [
                    o.create_var_scope([
                        o.create_class_at("Box", [
                            o.define_setter("size", [
                                o.set_attribute(
                                    o.self(), "_size",
                                    h.operator.join("set:", o.define_setter_value()),
                                ),
                            ]),
                            o.define_getter("size", [
                                o.return_value(
                                    h.operator.join(o.get_attribute("_size", o.self()), ":get"),
                                ),
                            ]),
                        ]),
                        o.set_scope_var("b", o.create_instance("Box", '[]')),
                        t.test_scope("setAttribute goes through setter", [
                            o.set_attribute(o.get_scope_var("b"), "size", "42"),
                        ]),
                        t.test_scope("Raw _size attribute reflects setter transformation", [
                            t.assert_unstrict_equal(o.get_attribute("_size", o.get_scope_var("b")), "set:42"),
                        ]),
                        t.test_scope("getAttribute goes through getter", [
                            t.assert_unstrict_equal(o.get_attribute("size", o.get_scope_var("b")), "set:42:get"),
                        ]),
                        t.test_scope("Update via setter replaces stored value", [
                            o.set_attribute(o.get_scope_var("b"), "size", "hello"),
                            t.assert_unstrict_equal(o.get_attribute("_size", o.get_scope_var("b")), "set:hello"),
                            t.assert_unstrict_equal(o.get_attribute("size", o.get_scope_var("b")), "set:hello:get"),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("getter-only attribute", [
                t.test_scope("Getter for computed read-only value", [
                    o.create_var_scope([
                        o.create_class_at("Circle", [
                            o.define_getter("doubled", [
                                o.return_value(h.operator.multiply(
                                    o.get_attribute("_val", o.self()), "2",
                                )),
                            ]),
                        ]),
                        o.set_scope_var("c", o.create_instance("Circle", '[]')),
                        o.set_attribute(o.get_scope_var("c"), "_val", "7"),
                        t.test_scope("getter doubles _val", [
                            t.assert_strict_equal(o.get_attribute("doubled", o.get_scope_var("c")), "14"),
                        ]),
                        t.test_scope("Raw _val unaffected", [
                            t.assert_strict_equal(o.get_attribute("_val", o.get_scope_var("c")), "7"),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("attributes without getter/setter bypass directly", [
                t.test_scope("setAttribute and getAttribute on plain attributes", [
                    o.create_var_scope([
                        o.create_class_at("Plain", []),
                        o.set_scope_var("p", o.create_instance("Plain", '[]')),
                        o.set_attribute(o.get_scope_var("p"), "x", "99"),
                        t.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("p")), "99"),
                    ]),
                ]),
            ]),

        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_operator_methods() -> TestProject:
    blocks = [
        t.test_scope("Operator Methods", [

            t.test_scope("left add operator", [
                t.test_scope("Custom class with left add: returns val + operand", [
                    o.create_var_scope([
                        o.create_class_at("MyNum", [
                            o.configure_next_function_args('["val"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self(), "val", o.get_scope_var("val")),
                            ]),
                            o.define_operator_method("left add", [
                                o.return_value(h.operator.add(
                                    o.get_attribute("val", o.self()),
                                    o.operator_operator_value(),
                                )),
                            ]),
                            o.define_operator_method("left subtract", [
                                o.return_value(h.operator.subtract(
                                    o.get_attribute("val", o.self()),
                                    o.operator_operator_value(),
                                )),
                            ]),
                        ]),
                        o.set_scope_var("n", o.create_instance("MyNum", '["10"]')),
                        t.test_scope("left add: 10 + 5 = 15", [
                            t.assert_strict_equal(h.operator.add(o.get_scope_var("n"), "5"), "15"),
                        ]),
                        t.test_scope("left add: 10 + 0 = 10", [
                            t.assert_strict_equal(h.operator.add(o.get_scope_var("n"), "0"), "10"),
                        ]),
                        t.test_scope("left subtract: 10 - 3 = 7", [
                            t.assert_strict_equal(h.operator.subtract(o.get_scope_var("n"), "3"), "7"),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("equals operator", [
                t.test_scope("Custom equals: compares val attribute", [
                    o.create_var_scope([
                        o.create_class_at("Token", [
                            o.configure_next_function_args('["id"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self(), "id", o.get_scope_var("id")),
                            ]),
                            o.define_operator_method("equals", [
                                o.return_value(h.operator.equals(
                                    o.get_attribute("id", o.self()),
                                    o.operator_operator_value(),
                                )),
                            ]),
                        ]),
                        o.set_scope_var("tok", o.create_instance("Token", '["abc"]')),
                        t.test_scope("Equals the stored id", [
                            t.assert_(h.operator.equals(o.get_scope_var("tok"), "abc")),
                        ]),
                        t.test_scope("Does not equal a different value", [
                            t.assert_not(h.operator.equals(o.get_scope_var("tok"), "xyz")),
                            t.assert_not(h.operator.equals(o.get_scope_var("tok"), "")),
                        ]),
                    ]),
                ]),
            ]),

        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_static_methods() -> TestProject:
    blocks = [
        t.test_scope("Static Methods", [

            t.test_scope("define and call a static method", [
                o.create_var_scope([
                    o.create_class_at("MathUtils", [
                        o.configure_next_function_args('["x"]', '[]'),
                        o.define_static_method("square", [
                            o.return_value(h.operator.multiply(
                                o.get_scope_var("x"), o.get_scope_var("x"),
                            )),
                        ]),
                        o.configure_next_function_args('["a","b"]', '[]'),
                        o.define_static_method("add", [
                            o.return_value(h.operator.add(
                                o.get_scope_var("a"), o.get_scope_var("b"),
                            )),
                        ]),
                    ]),
                    t.test_scope("callStaticMethod: square(4) = 16", [
                        t.assert_strict_equal(
                            o.call_static_method("MathUtils", "square", '["4"]'),
                            "16",
                        ),
                    ]),
                    t.test_scope("callStaticMethod: square(0) = 0", [
                        t.assert_strict_equal(
                            o.call_static_method("MathUtils", "square", '["0"]'),
                            "0",
                        ),
                    ]),
                    t.test_scope("callStaticMethod: add(3, 7) = 10", [
                        t.assert_strict_equal(
                            o.call_static_method("MathUtils", "add", '["3","7"]'),
                            "10",
                        ),
                    ]),
                ]),
            ]),

            t.test_scope("getStaticMethodFunc + callFunction", [
                o.create_var_scope([
                    o.create_class_at("Fmt", [
                        o.configure_next_function_args('["val"]', '[]'),
                        o.define_static_method("wrap", [
                            o.return_value(h.operator.join3(
                                "[", o.get_scope_var("val"), "]",
                            )),
                        ]),
                    ]),
                    t.test_scope("getStaticMethodFunc returns a callable function", [
                        o.set_scope_var("wrapFn", o.get_static_method_func("wrap", "Fmt")),
                        t.assert_unstrict_equal(o.typeof_value(o.get_scope_var("wrapFn")), o.typeof_value_selection("Function (GCE)")),
                    ]),
                    t.test_scope("callFunction on retrieved static method", [
                        t.assert_unstrict_equal(
                            o.call_function("wrapFn", '["hello"]'),
                            "[hello]",
                        ),
                    ]),
                    t.test_scope("Both callStaticMethod and callFunction give same result", [
                        t.assert_unstrict_equal(
                            o.call_static_method("Fmt", "wrap", '["world"]'),
                            o.call_function("wrapFn", '["world"]'),
                        ),
                    ]),
                ]),
            ]),

            t.test_scope("error cases", [
                o.create_var_scope([
                    o.create_class_at("Solo", []),
                    t.test_scope("Calling a non-existent static method throws", [
                        t.assert_throws([
                            o.execute_expression(o.call_static_method("Solo", "missing", '[]')),
                        ]),
                    ]),
                ]),
            ]),

        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_class_variables() -> TestProject:
    blocks = [
        t.test_scope("Class Variables", [

            t.test_scope("set and get class variable", [
                o.create_var_scope([
                    o.create_class_at("Counter", []),
                    t.test_scope("Set and read a class variable", [
                        o.set_class_variable("Counter", "count", "0"),
                        t.assert_unstrict_equal(o.get_class_variable("count", "Counter"), "0"),
                    ]),
                    t.test_scope("Update the class variable", [
                        o.set_class_variable("Counter", "count", "42"),
                        t.assert_unstrict_equal(o.get_class_variable("count", "Counter"), "42"),
                    ]),
                    t.test_scope("Multiple class variables coexist", [
                        o.set_class_variable("Counter", "name", "MyCounter"),
                        t.assert_unstrict_equal(o.get_class_variable("name", "Counter"), "MyCounter"),
                    ]),
                    t.test_scope("Reading first variable unchanged", [
                        t.assert_unstrict_equal(o.get_class_variable("count", "Counter"), "42"),
                    ]),
                ]),
            ]),

            t.test_scope("propertyNamesOfClass reflects class variables", [
                o.create_var_scope([
                    o.create_class_at("Config", [
                        o.define_instance_method("doWork", [
                            o.return_value("done"),
                        ]),
                    ]),
                    o.set_class_variable("Config", "version", "1"),
                    o.set_class_variable("Config", "author", "test"),
                    t.test_scope("Class variable names listed", [
                        t.assert_text_in_value("version", o.property_names_of_class("class variable", "Config")),
                        t.assert_text_in_value("author", o.property_names_of_class("class variable", "Config")),
                    ]),
                    t.test_scope("Method names NOT in class variable list", [
                        t.assert_text_not_in_value("doWork", o.property_names_of_class("class variable", "Config")),
                    ]),
                    t.test_scope("Instance method names listed correctly", [
                        t.assert_text_in_value("doWork", o.property_names_of_class("instance method", "Config")),
                    ]),
                    t.test_scope("Class variable names NOT in instance method list", [
                        t.assert_text_not_in_value("version", o.property_names_of_class("instance method", "Config")),
                    ]),
                ]),
            ]),

            t.test_scope("delete class variable", [
                o.create_var_scope([
                    o.create_class_at("Bag", []),
                    o.set_class_variable("Bag", "keep", "yes"),
                    o.set_class_variable("Bag", "remove", "no"),
                    t.test_scope("Both exist before delete", [
                        t.assert_text_in_value("keep", o.property_names_of_class("class variable", "Bag")),
                        t.assert_text_in_value("remove", o.property_names_of_class("class variable", "Bag")),
                    ]),
                    t.test_scope("Delete one", [
                        o.delete_class_variable("Bag", "remove"),
                    ]),
                    t.test_scope("Deleted variable throws on get", [
                        t.assert_throws([
                            o.execute_expression(o.get_class_variable("remove", "Bag")),
                        ]),
                    ]),
                    t.test_scope("Deleted variable absent from property names", [
                        t.assert_text_not_in_value("remove", o.property_names_of_class("class variable", "Bag")),
                    ]),
                    t.test_scope("Other variable unaffected", [
                        t.assert_text_in_value("keep", o.property_names_of_class("class variable", "Bag")),
                        t.assert_unstrict_equal(o.get_class_variable("keep", "Bag"), "yes"),
                    ]),
                ]),
            ]),

            t.test_scope("class variables are shared across instances", [
                o.create_var_scope([
                    o.create_class_at("Shared", [
                        o.define_instance_method("getVar", [
                            o.return_value(o.get_class_variable("shared", "Shared")),
                        ]),
                    ]),
                    o.set_class_variable("Shared", "shared", "initial"),
                    o.set_scope_var("i1", o.create_instance("Shared", '[]')),
                    o.set_scope_var("i2", o.create_instance("Shared", '[]')),
                    t.test_scope("Both instances see the same class variable", [
                        t.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("i1"), "getVar", '[]'),
                            "initial",
                        ),
                        t.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("i2"), "getVar", '[]'),
                            "initial",
                        ),
                    ]),
                    t.test_scope("Update class variable - both instances see new value", [
                        o.set_class_variable("Shared", "shared", "updated"),
                        t.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("i1"), "getVar", '[]'),
                            "updated",
                        ),
                        t.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("i2"), "getVar", '[]'),
                            "updated",
                        ),
                    ]),
                ]),
            ]),

        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_class_definition_blocks() -> TestProject:
    blocks = [
        t.test_scope("Class Definition and Inheritance Blocks", [

            # ------------------------------------------------------------------ #
            t.test_scope("createClassAt", [
                t.test_scope("Class is accessible by name and typeof is Class (GCE)", [
                    o.create_var_scope([
                        o.create_class_at("MyClass", []),
                        t.assert_unstrict_equal(o.typeof_value(o.get_scope_var("MyClass")), o.typeof_value_selection("Class (GCE)")),
                        t.test_scope("Can create an instance immediately", [
                            o.set_scope_var("inst", o.create_instance("MyClass", '[]')),
                            t.assert_(o.typeof_value_is_menu(o.get_scope_var("inst"), "Class Instance (GCE)")),
                            t.assert_(o.is_instance(o.get_scope_var("inst"), "MyClass")),
                        ]),
                    ]),
                ]),
                t.test_scope("Class with methods and init defined inline", [
                    o.create_var_scope([
                        o.create_class_at("Counter", [
                            o.configure_next_function_args('["start"]', '["0"]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self(), "count", o.get_scope_var("start")),
                            ]),
                            o.define_instance_method("value", [
                                o.return_value(o.get_attribute("count", o.self())),
                            ]),
                        ]),
                        o.set_scope_var("c", o.create_instance("Counter", '["5"]')),
                        t.assert_unstrict_equal(o.call_method(o.get_scope_var("c"), "value", '[]'), "5"),
                        t.test_scope("Default arg: no args uses default 0", [
                            o.set_scope_var("d", o.create_instance("Counter", '[]')),
                            t.assert_unstrict_equal(o.call_method(o.get_scope_var("d"), "value", '[]'), "0"),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("createClassNamed (reporter)", [
                t.test_scope("Create class inline as a reporter value, store and use it", [
                    o.create_var_scope([
                        o.set_scope_var("Dyn", o.create_class_named("DynClass", [
                            o.define_instance_method("ping", [
                                o.return_value("pong"),
                            ]),
                        ])),
                        t.test_scope("Stored value is a Class (GCE)", [
                            t.assert_unstrict_equal(o.typeof_value(o.get_scope_var("Dyn")), o.typeof_value_selection("Class (GCE)")),
                        ]),
                        t.test_scope("Class can be instantiated", [
                            o.set_scope_var("inst", o.create_instance(o.get_scope_var("Dyn"), '[]')),
                            t.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("inst"), "ping", '[]'),
                                "pong",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("currentClass", [
                t.test_scope("currentClass inside createClassAt returns the class being defined", [
                    o.create_var_scope([
                        o.create_class_at("Stamped", [
                            o.set_class_variable(o.current_class(), "tag", "stamped-value"),
                        ]),
                        t.test_scope("Class variable set via currentClass is accessible by name", [
                            t.assert_unstrict_equal(o.get_class_variable("tag", "Stamped"), "stamped-value"),
                        ]),
                    ]),
                ]),
                t.test_scope("currentClass inside createClassNamed also works", [
                    o.create_var_scope([
                        o.set_scope_var("NC", o.create_class_named("NamedCls", [
                            o.set_class_variable(o.current_class(), "info", "from-named"),
                        ])),
                        t.assert_unstrict_equal(o.get_class_variable("info", o.get_scope_var("NC")), "from-named"),
                    ]),
                ]),
                t.test_scope("currentClass inside onClass returns the correct class", [
                    o.create_var_scope([
                        o.create_class_at("Extendable", []),
                        o.on_class("Extendable", [
                            o.set_class_variable(o.current_class(), "addedTag", "via-on-class"),
                        ]),
                        t.assert_unstrict_equal(o.get_class_variable("addedTag", "Extendable"), "via-on-class"),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("createSubclassAt", [
                o.create_var_scope([
                    o.create_class_at("Animal", [
                        o.define_instance_method("breathe", [
                            o.return_value("breathing"),
                        ]),
                    ]),
                    o.create_subclass_at("Dog", "Animal", [
                        o.define_instance_method("bark", [
                            o.return_value("woof"),
                        ]),
                    ]),
                    t.test_scope("isSubclass reflects the relationship", [
                        t.assert_(o.is_subclass("Dog", "Animal")),
                        t.assert_not(o.is_subclass("Animal", "Dog")),
                    ]),
                    t.test_scope("getSuperclass of Dog is Animal", [
                        t.assert_text_in_value("Animal", o.get_superclass("Dog")),
                    ]),
                    t.test_scope("Dog instance can call both inherited and own methods", [
                        o.set_scope_var("d", o.create_instance("Dog", '[]')),
                        t.assert_unstrict_equal(o.call_method(o.get_scope_var("d"), "breathe", '[]'), "breathing"),
                        t.assert_unstrict_equal(o.call_method(o.get_scope_var("d"), "bark", '[]'), "woof"),
                    ]),
                    t.test_scope("currentClass inside subclass body returns the subclass", [
                        o.create_subclass_at("Puppy", "Dog", [
                            o.set_class_variable(o.current_class(), "size", "small"),
                        ]),
                        t.assert_unstrict_equal(o.get_class_variable("size", "Puppy"), "small"),
                    ]),
                    t.test_scope("isSubclass is transitive", [
                        t.assert_(o.is_subclass("Puppy", "Animal")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("createSubclassNamed (reporter)", [
                o.create_var_scope([
                    o.create_class_at("BaseR", [
                        o.define_instance_method("base", [
                            o.return_value("from-base"),
                        ]),
                    ]),
                    o.set_scope_var("Sub", o.create_subclass_named("SubNamed", "BaseR", [
                        o.define_instance_method("child", [
                            o.return_value("from-child"),
                        ]),
                    ])),
                    t.test_scope("Stored value is a Class (GCE)", [
                        t.assert_unstrict_equal(o.typeof_value(o.get_scope_var("Sub")), o.typeof_value_selection("Class (GCE)")),
                    ]),
                    t.test_scope("isSubclass works for reporter-created subclass", [
                        t.assert_(o.is_subclass(o.get_scope_var("Sub"), "BaseR")),
                    ]),
                    t.test_scope("Instance inherits from base and has own method", [
                        o.set_scope_var("inst", o.create_instance(o.get_scope_var("Sub"), '[]')),
                        t.assert_unstrict_equal(o.call_method(o.get_scope_var("inst"), "base", '[]'), "from-base"),
                        t.assert_unstrict_equal(o.call_method(o.get_scope_var("inst"), "child", '[]'), "from-child"),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("isSubclass", [
                o.create_var_scope([
                    o.create_class_at("A", []),
                    o.create_subclass_at("B", "A", []),
                    o.create_subclass_at("C", "B", []),
                    t.test_scope("Direct and transitive subclass", [
                        t.assert_(o.is_subclass("B", "A")),
                        t.assert_(o.is_subclass("C", "A")),
                        t.assert_(o.is_subclass("C", "B")),
                    ]),
                    t.test_scope("Reverse is false", [
                        t.assert_not(o.is_subclass("A", "B")),
                        t.assert_not(o.is_subclass("A", "C")),
                    ]),
                    t.test_scope("A class is kinda a subclass of itself", [
                        t.assert_(o.is_subclass("A", "A")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("getSuperclass", [
                o.create_var_scope([
                    o.create_class_at("Root", []),
                    o.create_subclass_at("Branch", "Root", []),
                    t.test_scope("Superclass of Branch is Root", [
                        t.assert_text_in_value("Root", o.get_superclass("Branch")),
                    ]),
                    t.test_scope("Root's superclass is the built-in Superclass", [
                        t.assert_text_in_value("Superclass", o.get_superclass("Root")),
                    ]),
                    t.test_scope("Missing class throws", [
                        t.assert_throws([
                            o.execute_expression(o.get_superclass("__no_such_class__")),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("onClass: add instance method", [
                t.test_scope("Define class with no methods, then add one via onClass", [
                    o.create_var_scope([
                        o.create_class_at("Greeter", []),
                        o.on_class("Greeter", [
                            o.configure_next_function_args('["name"]', '[]'),
                            o.define_instance_method("hello", [
                                o.return_value(h.operator.join("Hello, ", o.get_scope_var("name"))),
                            ]),
                        ]),
                        o.set_scope_var("g", o.create_instance("Greeter", '[]')),
                        t.test_scope("Method added via onClass is callable", [
                            t.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "hello", '["World"]'),
                                "Hello, World",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("onClass: add static method", [
                o.create_var_scope([
                    o.create_class_at("Util", []),
                    o.on_class("Util", [
                        o.configure_next_function_args('["x"]', '[]'),
                        o.define_static_method("double", [
                            o.return_value(h.operator.multiply(o.get_scope_var("x"), "2")),
                        ]),
                    ]),
                    t.test_scope("Static method added via onClass is callable", [
                        t.assert_unstrict_equal(
                            o.call_static_method("Util", "double", '["7"]'),
                            "14",
                        ),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("onClass: currentClass inside body", [
                t.test_scope("currentClass used inside onClass body sets a class variable", [
                    o.create_var_scope([
                        o.create_class_at("Tagged", []),
                        o.on_class("Tagged", [
                            o.set_class_variable(o.current_class(), "source", "on-class"),
                        ]),
                        t.assert_unstrict_equal(o.get_class_variable("source", "Tagged"), "on-class"),
                        t.test_scope("Multiple onClass calls accumulate class variables", [
                            o.on_class("Tagged", [
                                o.set_class_variable(o.current_class(), "extra", "second"),
                            ]),
                            t.assert_unstrict_equal(o.get_class_variable("source", "Tagged"), "on-class"),
                            t.assert_unstrict_equal(o.get_class_variable("extra", "Tagged"), "second"),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("onClass: visible in propertyNamesOfClass", [
                t.test_scope("Method added via onClass appears in property list", [
                    o.create_var_scope([
                        o.create_class_at("Widget", []),
                        t.test_scope("No methods yet", [
                            t.assert_text_not_in_value("render", o.property_names_of_class("instance method", "Widget")),
                            o.on_class("Widget", [
                                o.define_instance_method("render", [
                                    o.return_value("rendered"),
                                ]),
                            ]),
                        ]),
                        t.test_scope("Method now listed after onClass", [
                            t.assert_text_in_value("render", o.property_names_of_class("instance method", "Widget")),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("onClass: cleanup on error", [
                t.test_scope("class def scope cleanup runs even when body throws", [
                    o.create_var_scope([
                        o.create_class_at("Safe", []),
                        t.assert_throws([
                            o.on_class("Safe", [
                                o.execute_expression(o.get_scope_var("__missing__")),
                            ]),
                        ]),
                        t.test_scope("After the error, onClass on same class still works", [
                            t.assert_does_not_throw([
                                o.on_class("Safe", [
                                    o.define_instance_method("ok", [
                                        o.return_value("ok"),
                                    ]),
                                ]),
                            ]),
                            t.assert_unstrict_equal(
                                o.call_method(o.create_instance("Safe", '[]'), "ok", '[]'),
                                "ok",
                            ),
                        ]),
                    ]),
                ]),
            ]),

        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_introspection() -> TestProject:
    blocks = [
        t.test_scope("Introspection", [

            t.test_scope("getAttribute and setAttribute (direct)", [
                o.create_var_scope([
                    o.create_class_at("Person", [
                        o.configure_next_function_args('["name"]', '[]'),
                        o.define_special_method("init", [
                            o.set_attribute(o.self(), "name", o.get_scope_var("name")),
                        ]),
                        o.define_instance_method("greet", [
                            o.return_value(h.operator.join("Hi, ", o.get_attribute("name", o.self()))),
                        ]),
                    ]),
                    o.create_subclass_at("Employee", "Person", []),
                    o.set_scope_var("p", o.create_instance("Person", '["Bob"]')),
                    o.set_attribute(o.get_scope_var("p"), "age", "30"),
                    t.test_scope("Attribute set via init", [
                        t.assert_unstrict_equal(o.get_attribute("name", o.get_scope_var("p")), "Bob"),
                    ]),
                    t.test_scope("Attribute set after creation", [
                        t.assert_unstrict_equal(o.get_attribute("age", o.get_scope_var("p")), "30"),
                    ]),
                    t.test_scope("Overwrite attribute", [
                        o.set_attribute(o.get_scope_var("p"), "name", "Robert"),
                        t.assert_unstrict_equal(o.get_attribute("name", o.get_scope_var("p")), "Robert"),
                    ]),
                    t.test_scope("Missing attribute throws", [
                        t.assert_throws([
                            o.execute_expression(o.get_attribute("missing", o.get_scope_var("p"))),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("getClassOfInstance", [
                o.create_var_scope([
                    o.create_class_at("Cat", []),
                    o.create_subclass_at("Kitten", "Cat", []),
                    o.set_scope_var("c", o.create_instance("Cat", '[]')),
                    o.set_scope_var("k", o.create_instance("Kitten", '[]')),
                    t.test_scope("getClassOfInstance contains the class name", [
                        t.assert_text_in_value("Cat", o.get_class_of_instance(o.get_scope_var("c"))),
                        t.assert_text_in_value("Kitten", o.get_class_of_instance(o.get_scope_var("k"))),
                    ]),
                    t.test_scope("Cat instance does NOT report Kitten", [
                        t.assert_text_not_in_value("Kitten", o.get_class_of_instance(o.get_scope_var("c"))),
                    ]),
                ]),
            ]),

            t.test_scope("isInstance", [
                o.create_var_scope([
                    o.create_class_at("Fruit", []),
                    o.create_subclass_at("Apple", "Fruit", []),
                    o.set_scope_var("f", o.create_instance("Fruit", '[]')),
                    o.set_scope_var("a", o.create_instance("Apple", '[]')),
                    t.test_scope("Instance of own class", [
                        t.assert_(o.is_instance(o.get_scope_var("f"), "Fruit")),
                        t.assert_(o.is_instance(o.get_scope_var("a"), "Apple")),
                    ]),
                    t.test_scope("Subclass instance is instance of superclass", [
                        t.assert_(o.is_instance(o.get_scope_var("a"), "Fruit")),
                    ]),
                    t.test_scope("Superclass instance is NOT instance of subclass", [
                        t.assert_not(o.is_instance(o.get_scope_var("f"), "Apple")),
                    ]),
                    t.test_scope("Non-instance values return false", [
                        t.assert_not(o.is_instance("hello", "Fruit")),
                        t.assert_not(o.is_instance(o.nothing(), "Fruit")),
                    ]),
                ]),
            ]),

            t.test_scope("propertyNamesOfClass", [
                o.create_var_scope([
                    o.create_class_at("Widget", [
                        o.define_instance_method("render", [
                            o.return_value("rendered"),
                        ]),
                        o.define_static_method("create", [
                            o.return_value("widget"),
                        ]),
                        o.define_getter("width", [
                            o.return_value(o.get_attribute("_w", o.self())),
                        ]),
                        o.define_setter("height", [
                            o.set_attribute(o.self(), "_h", o.define_setter_value()),
                        ]),
                    ]),
                    o.set_class_variable("Widget", "version", "2"),
                    t.test_scope("Instance methods", [
                        t.assert_text_in_value("render", o.property_names_of_class("instance method", "Widget")),
                        t.assert_text_not_in_value("create", o.property_names_of_class("instance method", "Widget")),
                    ]),
                    t.test_scope("Static methods", [
                        t.assert_text_in_value("create", o.property_names_of_class("static method", "Widget")),
                        t.assert_text_not_in_value("render", o.property_names_of_class("static method", "Widget")),
                    ]),
                    t.test_scope("Getter methods", [
                        t.assert_text_in_value("width", o.property_names_of_class("getter method", "Widget")),
                        t.assert_text_not_in_value("height", o.property_names_of_class("getter method", "Widget")),
                    ]),
                    t.test_scope("Setter methods", [
                        t.assert_text_in_value("height", o.property_names_of_class("setter method", "Widget")),
                        t.assert_text_not_in_value("width", o.property_names_of_class("setter method", "Widget")),
                    ]),
                    t.test_scope("Class variables", [
                        t.assert_text_in_value("version", o.property_names_of_class("class variable", "Widget")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            t.test_scope("propertyNamesOfClass edge cases", [
                t.test_scope("Empty class has no own instance methods (beyond built-in)", [
                    o.create_var_scope([
                        o.create_class_at("Empty", []),
                        t.assert_text_not_in_value("render", o.property_names_of_class("instance method", "Empty")),
                        t.assert_text_not_in_value("create", o.property_names_of_class("static method", "Empty")),
                        t.assert_text_not_in_value("version", o.property_names_of_class("class variable", "Empty")),
                    ]),
                ]),
                t.test_scope("Subclass without own methods still sees inherited methods", [
                    o.create_var_scope([
                        o.create_class_at("Parent", [
                            o.define_instance_method("inherited", [
                                o.return_value("from-parent"),
                            ]),
                            o.define_static_method("parentStatic", [
                                o.return_value("static-from-parent"),
                            ]),
                        ]),
                        o.create_subclass_at("ChildNoMethods", "Parent", []),
                        t.test_scope("Inherited instance method visible on child", [
                            t.assert_text_in_value("inherited", o.property_names_of_class("instance method", "ChildNoMethods")),
                        ]),
                        t.test_scope("Inherited static method visible on child", [
                            t.assert_text_in_value("parentStatic", o.property_names_of_class("static method", "ChildNoMethods")),
                        ]),
                        t.test_scope("Parent's own methods also still visible on parent", [
                            t.assert_text_in_value("inherited", o.property_names_of_class("instance method", "Parent")),
                        ]),
                    ]),
                ]),
                t.test_scope("Overriding a method replaces it, not duplicates it", [
                    o.create_var_scope([
                        o.create_class_at("Base2", [
                            o.define_instance_method("greet", [
                                o.return_value("base-greet"),
                            ]),
                        ]),
                        o.create_subclass_at("Child2", "Base2", [
                            o.define_instance_method("greet", [
                                o.return_value("child-greet"),
                            ]),
                        ]),
                        t.test_scope("greet appears in child's instance methods", [
                            t.assert_text_in_value("greet", o.property_names_of_class("instance method", "Child2")),
                        ]),
                        t.test_scope("Override is active — child instance calls child version", [
                            o.set_scope_var("c", o.create_instance("Child2", '[]')),
                            t.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("c"), "greet", '[]'),
                                "child-greet",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            t.test_scope("getAllAttributes", [
                o.create_var_scope([
                    o.create_class_at("Data", []),
                    o.set_scope_var("d", o.create_instance("Data", '[]')),
                    o.set_attribute(o.get_scope_var("d"), "x", "1"),
                    o.set_attribute(o.get_scope_var("d"), "y", "2"),
                    t.test_scope("getAllAttributes includes all set attributes", [
                        t.assert_text_in_value("x", o.get_all_attributes(o.get_scope_var("d"))),
                        t.assert_text_in_value("y", o.get_all_attributes(o.get_scope_var("d"))),
                        t.assert_text_in_value("1", o.get_all_attributes(o.get_scope_var("d"))),
                        t.assert_text_in_value("2", o.get_all_attributes(o.get_scope_var("d"))),
                    ]),
                ]),
            ]),

        ]),
    ]
    
    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def main() -> None:
    configure()
    test_projects_dir = Path("test_projects")

    projects: list[tuple[TestProject, Path]] = []
    
    #projects.append((test_TypeChecker(), test_projects_dir / "test_TypeChecker.pmp"))
    #projects.append((test_Cast(), test_projects_dir / "test_Cast.pmp"))
    #projects.append((test_scoped_variables_blocks(), test_projects_dir / "test_scoped_variables.pmp"))
    #projects.append((test_function_blocks(), test_projects_dir / "test_function.pmp"))
    #projects.append((test_utilities_blocks(), test_projects_dir / "test_utilities.pmp"))
    projects.append((test_class_definition_blocks(), test_projects_dir / "test_class_definition.pmp"))
    #projects.append((test_instance_methods(), test_projects_dir / "test_instance_methods.pmp"))
    #projects.append((test_special_method_init(), test_projects_dir / "test_special_method_init.pmp"))
    #projects.append((test_inheritance_and_super(), test_projects_dir / "test_inheritance_and_super.pmp"))
    #projects.append((test_getters_and_setters(), test_projects_dir / "test_getters_and_setters.pmp"))
    #projects.append((test_operator_methods(), test_projects_dir / "test_operator_methods.pmp"))
    #projects.append((test_static_methods(), test_projects_dir / "test_static_methods.pmp"))
    #projects.append((test_class_variables(), test_projects_dir / "test_class_variables.pmp"))
    #projects.append((test_introspection(), test_projects_dir / "test_introspection.pmp"))

    for project, path in projects:
        write_project_to_file(project, path)
    
    united_project = TestProject.join_projects([p for p, _ in projects])
    write_project_to_file(united_project, test_projects_dir / "test_united.pmp")

if __name__ == "__main__":
    main()
