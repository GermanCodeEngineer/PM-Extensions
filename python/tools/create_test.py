from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import copy
from gceutils import AbstractTreePath, grepr_dataclass
import pmp_manip as p
from pmp_manip.opcode_info.api import OpcodeInfoAPI
import third

from helpers.gceFuncsScopes import gceFuncsScopes
from helpers.gceOOP import gceOOP
from helpers.gceTestRunner import gceTestRunner as tr
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
    blocks: list[third.ThirdBlock]
    extension_ids: list[str]

    @staticmethod
    def join_projects(projects: list[TestProject]) -> TestProject:
        all_blocks = []
        all_extension_ids = set()
        for project in projects:
            assert len(project.blocks) == 1, "Expected one top level test_scope block"
            assert isinstance(project.blocks[0], tr.test_scope),  "Expected top level block to be a test_scope"
            all_blocks.extend(project.blocks)
            all_extension_ids.update(project.extension_ids)
        return TestProject(blocks=all_blocks, extension_ids=list(all_extension_ids))
    
def convert_project(test_project: TestProject) -> p.FRProject:
    trproject = third.ThirdProject.create_empty()
    trsprite = third.ThirdSprite.create_empty("Test")
    trproject.sprites.append(trsprite)
    trproject.sprite_layer_stack.append(trsprite.uuid)

    blocks = copy.copy(test_project.blocks)
    blocks.insert(0, h.event.whenflagclicked())
    trsprite.scripts = [third.ThirdScript(blocks, row=0, col=0)]

    trproject.extensions = []
    for id in test_project.extension_ids:
        url = EXTENSION_SOURCES[id]
        trproject.extensions.append(
            p.SRCustomExtension(id, url) if url is not None else p.SRBuiltinExtension(id=id)
        )
    
    # Convert from TR to SR
    srproject = trproject.to_second()
    opcode_info_copy = p.info_api.opcode_info.copy()
    info_api_copy = OpcodeInfoAPI(opcode_info_copy)
    srproject.add_all_extensions_to_info_api(info_api_copy)

    # Validate SR
    # Tricks to avoid errors for invalid extension URLs (currently too strict)
    extensions_before = copy.deepcopy(srproject.extensions)
    for extension in srproject.extensions:
        extension.url = "https://example.com/"

    srproject.validate(AbstractTreePath(), info_api_copy)
    srproject.extensions = extensions_before

    # Convert from SR to FR
    frproject = srproject.to_first(info_api_copy)
    return frproject

def write_project_to_file(project: TestProject, output_file: Path) -> None:
    frproject = convert_project(project)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    frproject.to_file(str(output_file))

def test_TypeChecker() -> TestProject:
    blocks = [
        tr.test_scope("TypeChecker", [
            tr.test_scope("My Types", [
                tr.assert_(o.typeof_value_is_menu(o.create_function_named("myFn", []), "Function (GCE)")),
                labels.label_command("Methods can not be accessed from a reporter"),
                tr.assert_(o.typeof_value_is_menu(o.create_class_named("MyClass", []), "Class (GCE)")),
                tr.assert_(o.typeof_value_is_menu(o.create_instance(o.create_class_named("MyClass", []), "[]"), "Class Instance (GCE)")),
                tr.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
            ]),
            tr.test_scope("Common/Safe JS data types", [
                tr.assert_(o.typeof_value_is_menu(h.SPjavascriptV2.js_reporter("return undefined"), "JavaScript Undefined")),
                tr.assert_(o.typeof_value_is_menu(h.SPjavascriptV2.js_reporter("return null"), "JavaScript Null")),
                tr.assert_(o.typeof_value_is_menu(h.operator.true_boolean(), "Boolean")),
                tr.assert_(o.typeof_value_is_menu("777", "Number")),
                tr.assert_(o.typeof_value_is_menu("hello", "String")),
            ]),
            tr.test_scope("Custom Extension Types", [
                tr.assert_(o.typeof_value_is_menu(h.agBuffer.new_buffer("1"), "Buffer (AndrewGaming587)")),
                tr.assert_(o.typeof_value_is_menu(h.agBuffer.create_pointer(
                    "0", False, h.agBuffer.new_buffer("1"), "Uint8",
                ), "Buffer Pointer (AndrewGaming587)")),
                tr.assert_(o.typeof_value_is_menu(h.ddeDateFormat.current_date(), "Date (Old Version) (ddededodediamante)")),
                tr.assert_(o.typeof_value_is_menu(h.ddeDateFormatV2.current_date(), "Date (ddededodediamante)")),
                labels.label_command("You can't access a div effect type from any reporter"),
                tr.assert_(o.typeof_value_is_menu(h.divIterator.iter_builder("", []), "Iterator (Div)")),
                tr.assert_(o.typeof_value_is_menu(h.dogeiscutObject.blank(), "Object (DogeisCut)")),
                tr.assert_(o.typeof_value_is_menu(h.dogeiscutRegularExpressions.regex("(.*)", "gm"), "Regular Expression (DogeisCut)")),
                tr.assert_(o.typeof_value_is_menu(h.dogeiscutSet.blank(), "Set (DogeisCut)")),
                labels.label_command("You can't access a timer type from any reporter"),
                tr.assert_(o.typeof_value_is_menu(h.jwArray.blank(), "Array (jwklong)")),
                tr.assert_(o.typeof_value_is_menu(h.jwColor.new_color("#ff0000"), "Color (jwklong)")),
                tr.assert_(o.typeof_value_is_menu(h.jwDate.now(), "Date (jwklong)")),
                tr.assert_(o.typeof_value_is_menu(h.jwLambda.new_lambda([]), "Lambda (jwklong)")),
                tr.assert_(o.typeof_value_is_menu(h.jwNum.add("1", "2"), "Number (jwklong)")),
                tr.assert_(o.typeof_value_is_menu(h.jwTargets.this(), "Target (jwklong)")),
                tr.assert_(o.typeof_value_is_menu(h.jwVector.new_vector("1", "2"), "Vector (jwklong)")),
                tr.assert_(o.typeof_value_is_menu(h.jwXML.new_node("test"), "XML (jwklong)")),
                labels.label_function("For this to work please create a canvas variable e.g. 'myCanvasVar', then enable the condition", [
                    h.control.if_(False, [
                        tr.assert_(o.typeof_value_is_menu("<put the canvas variable block here>", "Canvas (RedMan13)")),
                    ]),
                ]),
                tr.assert_(o.typeof_value_is_menu(h.fruitsPaintUtils.get_colour("orange"), "Paint Utils Colour (Fruits555000)")),
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
        tr.test_scope("Cast", [
            tr.test_scope("toArray", [o.create_var_scope([
                o.set_scope_var("my var", "hello"),
                o.set_scope_var("var list", o.all_variables("all scopes")),
                tr.assert_type(o.get_scope_var("var list"), "Array (jwklong)"),
                tr.assert_unstrict_equal(o.get_scope_var("var list"), '["my var"]')
            ])]),
            tr.test_scope("toObject", [o.create_var_scope([
                o.create_class_at("MyClass", []),
                o.set_scope_var("instance var", o.create_instance(o.create_class_named("MyClass", []), "[]")),
                o.set_attribute(o.get_scope_var("instance var"), "my attribute", "hello"),
                o.set_scope_var("attributes", o.get_all_attributes(o.get_scope_var("instance var"))),
                tr.assert_type(o.get_scope_var("attributes"), "Object (DogeisCut)"),
                tr.assert_unstrict_equal(o.get_scope_var("attributes"), '{"my attribute":"hello"}'),
            ])]),
            tr.test_scope("toClass && toClassInstance && toFunction", [o.create_var_scope([
                o.create_class_at("MyClass", []),
                tr.assert_unstrict_equal(o.get_superclass(o.create_subclass_named("Sub", "MyClass", [])), "<Class 'MyClass'>"),
                tr.assert_throws_contains("but got no input value", [
                    o.execute_expression(o.get_superclass(h.SPjavascriptV2.js_reporter("return undefined"))),
                ]),
                tr.assert_throws_contains("but got no input value", [
                    o.execute_expression(o.get_superclass(h.SPjavascriptV2.js_reporter("return null"))),
                ]),
                tr.assert_unstrict_equal(o.get_superclass("MyClass"), "<Class 'Superclass'>"),
                o.create_class_at("513", []),
                tr.assert_unstrict_equal(o.get_superclass("513"), "<Class 'Superclass'>"),
                tr.assert_throws_contains("but got no input value", [
                    o.execute_expression(o.get_superclass(h.SPjavascriptV2.js_reporter("return null"))),
                ]),
                tr.assert_throws([
                    o.create_subclass_at("Sub2", o.create_function_named("myFunction", []), []),
                ]),
            ])]),
        ]),
    ]
    
    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto", "SPjavascriptV2",
    ])

def test_scoped_variables() -> TestProject:
    kind_all = "all scopes"
    kind_local = "local scope"
    kind_global = "global scope"
    bind_global = "global"

    blocks = [
        tr.test_scope("Scoped Variables Blocks", [
            tr.test_scope("set/get/exists", [
                tr.test_scope("Set and read a local variable", [
                    o.create_var_scope([
                        tr.assert_not(o.scope_var_exists("myVar", kind_all)),
                        tr.assert_not(o.scope_var_exists("myVar", kind_local)),
                        tr.assert_not(o.scope_var_exists("myVar", kind_global)),
                        o.set_scope_var("myVar", "hello"),
                        tr.assert_strict_equal(o.get_scope_var("myVar"), "hello"),
                        tr.assert_(o.scope_var_exists("myVar", kind_all)),
                        tr.assert_(o.scope_var_exists("myVar", kind_local)),
                        tr.assert_not(o.scope_var_exists("myVar", kind_global)),
                    ]),
                ]),
            ]),

            tr.test_scope("delete var", [
                tr.test_scope("Delete removes the variable from the current scope", [
                    o.create_var_scope([
                        o.set_scope_var("tmp", "to-delete"),
                        tr.assert_(o.scope_var_exists("tmp", kind_all)),
                        o.delete_scope_var("tmp"),
                        tr.assert_not(o.scope_var_exists("tmp", kind_all)),
                        tr.assert_not(o.scope_var_exists("tmp", kind_local)),
                        tr.assert_not(o.scope_var_exists("tmp", kind_global)),
                        tr.assert_throws([
                            o.execute_expression(o.get_scope_var("tmp")),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("all variables + local scope", [
                tr.test_scope("List variables by kind and verify nested local scope behavior", [
                    o.create_var_scope([
                        o.set_scope_var("a", "1"),
                        o.set_scope_var("b", "2"),
                        tr.assert_unstrict_equal(o.all_variables(kind_all), '["a","b"]'),
                        tr.assert_unstrict_equal(o.all_variables(kind_local), '["a","b"]'),
                        tr.assert_unstrict_equal(o.all_variables(kind_global), '[]'),

                        o.create_var_scope([
                            tr.test_scope("In a fresh local scope, inherited names are visible in all scopes", [
                                tr.assert_unstrict_equal(o.all_variables(kind_all), '["a","b"]'),
                                tr.assert_unstrict_equal(o.all_variables(kind_local), '[]'),
                                tr.assert_unstrict_equal(o.all_variables(kind_global), '[]'),
                                o.set_scope_var("c", "3"),
                                tr.assert_unstrict_equal(o.all_variables(kind_all), '["a","b","c"]'),
                                tr.assert_unstrict_equal(o.all_variables(kind_local), '["c"]'),
                                tr.assert_unstrict_equal(o.all_variables(kind_global), '[]'),
                            ]),
                        ]),

                        tr.assert_not(o.scope_var_exists("c", kind_local)),
                        tr.assert_not(o.scope_var_exists("c", kind_all)),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("allVariables with globals and locals simultaneously", [
                tr.test_scope("kind_global and kind_local see only their own tier; kind_all sees both", [
                    o.run_with_separate_globals([
                        o.set_scope_var("globalX", "gx"),
                        o.set_scope_var("globalY", "gy"),
                        o.create_var_scope([
                            o.set_scope_var("localZ", "lz"),
                            tr.test_scope("kind_global sees globals only", [
                                tr.assert_text_in_value("globalX", o.all_variables(kind_global)),
                                tr.assert_text_in_value("globalY", o.all_variables(kind_global)),
                                tr.assert_text_not_in_value("localZ", o.all_variables(kind_global)),
                            ]),
                            tr.test_scope("kind_local sees locals only", [
                                tr.assert_text_in_value("localZ", o.all_variables(kind_local)),
                                tr.assert_text_not_in_value("globalX", o.all_variables(kind_local)),
                                tr.assert_text_not_in_value("globalY", o.all_variables(kind_local)),
                            ]),
                            tr.test_scope("kind_all sees both globals and locals", [
                                tr.assert_text_in_value("globalX", o.all_variables(kind_all)),
                                tr.assert_text_in_value("globalY", o.all_variables(kind_all)),
                                tr.assert_text_in_value("localZ", o.all_variables(kind_all)),
                            ]),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("bind global + non-local", [
                tr.test_scope("Bind global in an inner scope and mutate it", [
                    o.run_with_separate_globals([
                        o.set_scope_var("globalCounter", "0"),
                        o.create_var_scope([
                            o.bind_var_to_scope(bind_global, "globalCounter"),
                            o.set_scope_var("globalCounter", "1"),
                        ]),
                        tr.assert_strict_equal(o.get_scope_var("globalCounter"), "1"),
                    ]),
                ]),
                tr.test_scope("Bind non-local variable in nested local scopes and mutate it", [
                    o.create_var_scope([
                        o.set_scope_var("outerLocal", "A"),
                        o.create_var_scope([
                            o.bind_var_to_scope("non-local", "outerLocal"),
                            o.set_scope_var("outerLocal", "B"),
                        ]),
                        tr.assert_strict_equal(o.get_scope_var("outerLocal"), "B"),
                    ]),
                ]),
            ]),

            tr.test_scope("shadowing: inner scope shadows outer name", [
                tr.test_scope("get_scope_var resolves to innermost definition", [
                    o.create_var_scope([
                        o.set_scope_var("x", "outer"),
                        o.create_var_scope([
                            o.set_scope_var("x", "inner"),
                            tr.test_scope("Inner scope sees the inner value", [
                                tr.assert_strict_equal(o.get_scope_var("x"), "inner"),
                            ]),
                        ]),
                        tr.test_scope("After inner scope exits, outer value is restored", [
                            tr.assert_strict_equal(o.get_scope_var("x"), "outer"),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("bind then delete", [
                tr.test_scope("Delete a bound global variable from an inner scope", [
                    o.run_with_separate_globals([
                        o.set_scope_var("toDelete", "exists"),
                        o.create_var_scope([
                            o.bind_var_to_scope(bind_global, "toDelete"),
                            o.delete_scope_var("toDelete"),
                        ]),
                        tr.test_scope("Variable is gone from globals after delete", [
                            tr.assert_not(o.scope_var_exists("toDelete", kind_global)),
                            tr.assert_not(o.scope_var_exists("toDelete", kind_all)),
                        ]),
                    ]),
                ]),
                tr.test_scope("Delete a bound non-local variable from an inner scope", [
                    o.create_var_scope([
                        o.set_scope_var("outerVar", "exists"),
                        o.create_var_scope([
                            o.bind_var_to_scope("non-local", "outerVar"),
                            o.delete_scope_var("outerVar"),
                        ]),
                        tr.test_scope("Variable is gone from outer scope after delete", [
                            tr.assert_not(o.scope_var_exists("outerVar", kind_all)),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("bind error paths", [
                tr.test_scope("Binding a missing global/non-local variable should throw", [
                    tr.assert_throws([
                        o.bind_var_to_scope(bind_global, "missingGlobal"),
                    ]),
                    o.create_var_scope([
                        tr.assert_throws([
                            o.bind_var_to_scope("non-local", "missingNonLocal"),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("createVarScope cleanup on error", [
                tr.test_scope("exitUserScope must run even if an error is thrown inside the scope", [
                    o.create_var_scope([
                        o.set_scope_var("outerVar", "present"),
                        o.create_var_scope([
                            o.set_scope_var("innerVar", "value"),
                            tr.assert_throws([
                                o.execute_expression(o.get_scope_var("__missing_var__")),
                            ]),
                        ]),
                        tr.test_scope("Inner variable should be gone after error", [
                            tr.assert_not(o.scope_var_exists("innerVar", kind_all)),
                        ]),
                        tr.test_scope("Outer variable should still exist", [
                            tr.assert_(o.scope_var_exists("outerVar", kind_all)),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("scopeVarExists with 3-level nesting", [
                tr.test_scope("Verify kindLocal, kindAll, kindGlobal across 3 scopes", [
                    o.run_with_separate_globals([
                        o.set_scope_var("globalVar", "g"),
                        o.create_var_scope([
                            o.set_scope_var("level1", "L1"),
                            o.create_var_scope([
                                o.set_scope_var("level2", "L2"),
                                o.create_var_scope([
                                    o.set_scope_var("level3", "L3"),
                                    tr.test_scope("Innermost: level3 is local, others are not", [
                                        tr.assert_(o.scope_var_exists("level3", kind_local)),
                                        tr.assert_not(o.scope_var_exists("level1", kind_local)),
                                        tr.assert_not(o.scope_var_exists("level2", kind_local)),
                                    ]),
                                    tr.test_scope("All three are visible via kindAll", [
                                        tr.assert_(o.scope_var_exists("level1", kind_all)),
                                        tr.assert_(o.scope_var_exists("level2", kind_all)),
                                        tr.assert_(o.scope_var_exists("level3", kind_all)),
                                    ]),
                                    tr.test_scope("Global is visible via kindGlobal and kindAll", [
                                        tr.assert_(o.scope_var_exists("globalVar", kind_global)),
                                        tr.assert_(o.scope_var_exists("globalVar", kind_all)),
                                    ]),
                                    tr.test_scope("Local vars are NOT global", [
                                        tr.assert_not(o.scope_var_exists("level3", kind_global)),
                                        tr.assert_not(o.scope_var_exists("level2", kind_global)),
                                    ]),
                                ]),
                            ]),
                            tr.test_scope("level2 and level3 gone after exiting their scopes", [
                                tr.assert_not(o.scope_var_exists("level2", kind_all)),
                                tr.assert_not(o.scope_var_exists("level3", kind_all)),
                                tr.assert_(o.scope_var_exists("level1", kind_local)),
                            ]),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("runWithSeparateGlobals", [
                tr.test_scope("Outer locals are not visible inside", [
                    o.create_var_scope([
                        o.set_scope_var("outerLocal", "outer"),
                        o.run_with_separate_globals([
                            tr.assert_not(o.scope_var_exists("outerLocal", kind_all)),
                            tr.assert_not(o.scope_var_exists("outerLocal", kind_local)),
                            tr.assert_not(o.scope_var_exists("outerLocal", kind_global)),
                            tr.assert_throws([
                                o.execute_expression(o.get_scope_var("outerLocal")),
                            ]),
                        ]),
                    ]),
                ]),
                tr.test_scope("Outer globals are not visible inside", [
                    o.set_scope_var("outerGlobal", "outerGlobalValue"),
                    o.run_with_separate_globals([
                        tr.assert_not(o.scope_var_exists("outerGlobal", kind_all)),
                        tr.assert_not(o.scope_var_exists("outerGlobal", kind_global)),
                        tr.assert_throws([
                            o.execute_expression(o.get_scope_var("outerGlobal")),
                        ]),
                    ]),
                    o.delete_scope_var("outerGlobal"),
                ]),
                tr.test_scope("Writes inside do not affect outer locals", [
                    o.create_var_scope([
                        o.set_scope_var("sharedName", "before"),
                        o.run_with_separate_globals([
                            o.set_scope_var("sharedName", "inside"),
                            tr.assert_strict_equal(o.get_scope_var("sharedName"), "inside"),
                        ]),
                        tr.assert_strict_equal(o.get_scope_var("sharedName"), "before"),
                    ]),
                ]),
                tr.test_scope("Writes inside do not affect outer globals", [
                    o.set_scope_var("sharedGlobal", "globalBefore"),
                    o.run_with_separate_globals([
                        o.set_scope_var("sharedGlobal", "globalInside"),
                        tr.assert_strict_equal(o.get_scope_var("sharedGlobal"), "globalInside"),
                    ]),
                    tr.assert_strict_equal(o.get_scope_var("sharedGlobal"), "globalBefore"),
                    o.delete_scope_var("sharedGlobal"),
                ]),
                tr.test_scope("Inner globals and locals start empty", [
                    o.run_with_separate_globals([
                        tr.assert_unstrict_equal(o.all_variables(kind_all), "[]"),
                        tr.assert_unstrict_equal(o.all_variables(kind_global), "[]"),
                        tr.assert_unstrict_equal(o.all_variables(kind_local), "[]"),
                    ]),
                ]),
                tr.test_scope("Variables created inside are gone after block exits", [
                    o.run_with_separate_globals([
                        o.set_scope_var("innerOnly", "value"),
                    ]),
                    tr.assert_not(o.scope_var_exists("innerOnly", kind_all)),
                ]),
                tr.test_scope("Cleanup happens even if an error is thrown inside", [
                    tr.assert_throws([
                        o.run_with_separate_globals([
                            o.set_scope_var("innerError", "value"),
                            o.execute_expression(o.get_scope_var("__missing__")),
                        ]),
                    ]),
                    tr.assert_not(o.scope_var_exists("innerError", kind_all)),
                ]),
                tr.test_scope("Nested runWithSeparateGlobals are fully independent", [
                    o.set_scope_var("outerG", "OG"),
                    o.run_with_separate_globals([
                        o.set_scope_var("middleG", "MG"),
                        o.run_with_separate_globals([
                            tr.assert_not(o.scope_var_exists("outerG", kind_all)),
                            tr.assert_not(o.scope_var_exists("middleG", kind_all)),
                        ]),
                        tr.assert_(o.scope_var_exists("middleG", kind_global)),
                        tr.assert_not(o.scope_var_exists("outerG", kind_all)),
                    ]),
                    tr.assert_(o.scope_var_exists("outerG", kind_global)),
                    tr.assert_not(o.scope_var_exists("middleG", kind_all)),
                    o.delete_scope_var("outerG")
                ]),
            ]),
        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_functions() -> TestProject:
    blocks = [
        tr.test_scope("Function Blocks", [
            tr.test_scope("basic function", [
                o.create_var_scope([
                    tr.test_scope("Define a simple function that returns a constant", [
                        o.create_function_at("myFunc", [
                            o.return_value("hello"),
                        ]),
                    ]),
                    tr.test_scope("Call the function with no arguments", [
                        tr.assert_strict_equal(
                            o.call_function("myFunc", "[]"),
                            "hello"
                        ),
                    ]),
                ]),
            ]),

            tr.test_scope("function with args", [
                o.create_var_scope([
                    tr.test_scope("Configure and define function with two arguments", [
                        o.configure_next_function_args('["greeting", "name"]', '[]'),
                        o.create_function_at("greet", [
                            o.return_value(h.operator.join3(o.get_scope_var("greeting"), " ", o.get_scope_var("name"))),
                        ]),
                    ]),
                    tr.test_scope("Call with two arguments passed as array", [
                        tr.assert_strict_equal(
                            o.call_function("greet", '["Hello", "Ada"]'),
                            "Hello Ada"
                        ),
                    ]),
                ]),
            ]),

            tr.test_scope("default arguments", [
                o.create_var_scope([
                    tr.test_scope("Configure function with required arg and default trailing arg", [
                        o.configure_next_function_args('["person", "greeting"]', '["Hi"]'),
                        o.create_function_at("sayHi", [
                            o.return_value(h.operator.join3(o.get_scope_var("greeting"), " ", o.get_scope_var("person"))),
                        ]),
                    ]),
                    tr.test_scope("Call with only first arg (second uses default Hi)", [
                        tr.assert_strict_equal(
                            o.call_function("sayHi", '["Bob"]'),
                            "Hi Bob"
                        ),
                    ]),
                    tr.test_scope("Call with both args (overrides default)", [
                        tr.assert_strict_equal(
                            o.call_function("sayHi", '["Bob", "Hey"]'),
                            "Hey Bob"
                        ),
                    ]),
                ]),
            ]),

            tr.test_scope("return behavior", [
                o.create_var_scope([
                    tr.test_scope("Function returns early inside an if-block; later return must not run", [
                        o.configure_next_function_args('["flag"]', '[]'),
                        o.create_function_at("conditional", [
                            h.control.if_(
                                h.operator.equals(o.get_scope_var("flag"), "yes"),
                                [o.return_value("early")],
                            ),
                            o.return_value("late"),
                        ]),
                    ]),
                    tr.test_scope("When condition is true, early return fires", [
                        tr.assert_strict_equal(
                            o.call_function("conditional", '["yes"]'),
                            "early"
                        ),
                    ]),
                    tr.test_scope("When condition is false, falls through to second return", [
                        tr.assert_strict_equal(
                            o.call_function("conditional", '["no"]'),
                            "late"
                        ),
                    ]),
                ]),
            ]),

            tr.test_scope("closures", [o.run_with_separate_globals([
                tr.test_scope("Outer function accepts prefix, returns inner function that closes over it", [
                    o.configure_next_function_args('["prefix"]', '[]'),
                    o.create_function_at("makeGreeter", [
                        tr.test_scope("Configure inner function arg before defining it", [
                            o.configure_next_function_args('["name"]', '[]'),
                            o.return_value(o.create_function_named("greeter", [
                                o.return_value(h.operator.join3(o.get_scope_var("prefix"), ", ", o.get_scope_var("name"))),
                            ])),
                        ]),
                    ]),
                ]),
                tr.test_scope("Each call to makeGreeter produces an independent greeter", [
                    o.set_scope_var("hiGreeter", o.call_function("makeGreeter", '["Hi"]')),
                    o.set_scope_var("heyGreeter", o.call_function("makeGreeter", '["Hey"]')),
                    tr.assert_strict_equal(
                        o.call_function("hiGreeter", '["Ada"]'),
                        "Hi, Ada"
                    ),
                    tr.assert_strict_equal(
                        o.call_function("heyGreeter", '["Ada"]'),
                        "Hey, Ada"
                    ),
                ]),
                tr.test_scope("Captured prefix is independent per closure instance", [
                    tr.assert_strict_equal(
                        o.call_function("hiGreeter", '["Bob"]'),
                        "Hi, Bob"
                    ),
                ]),
            ])]),

            tr.test_scope("create function named", [o.run_with_separate_globals([
                tr.test_scope("Create a function as a reporter block (returns the function)", [
                    o.set_scope_var("myFunc", o.create_function_named("anonFunc", [
                        o.return_value("from-anon"),
                    ])),
                ]),
                tr.test_scope("Call the stored function", [
                    tr.assert_strict_equal(
                        o.call_function("myFunc", "[]"),
                        "from-anon"
                    ),
                ]),
            ])]),

            tr.test_scope("error: wrong arg count", [o.run_with_separate_globals([
                tr.test_scope("Function that accepts no arguments", [
                    o.create_function_at("noArgs", [
                        o.return_value("done"),
                    ]),
                ]),
                tr.test_scope("Calling with extra arguments should throw", [
                    tr.assert_throws([
                        o.execute_expression(o.call_function("noArgs", '["extra"]')),
                    ]),
                ]),
                tr.test_scope("Function that requires one argument", [
                    o.configure_next_function_args('["required"]', '[]'),
                    o.create_function_at("oneArg", [
                        o.return_value(o.get_scope_var("required")),
                    ]),
                ]),
                tr.test_scope("Calling with no arguments should throw", [
                    tr.assert_throws([
                        o.execute_expression(o.call_function("oneArg", "[]")),
                    ]),
                ]),
            ])]),

            # ------------------------------------------------------------------ #
            tr.test_scope("var scope inside function body", [o.create_var_scope([
                tr.test_scope("createVarScope inside a function is isolated per call", [
                    o.configure_next_function_args('["val"]', '[]'),
                    o.create_function_at("withScope", [
                        o.create_var_scope([
                            o.set_scope_var("inner", o.get_scope_var("val")),
                            o.return_value(o.get_scope_var("inner")),
                        ]),
                    ]),
                ]),
                tr.test_scope("First call", [
                    tr.assert_strict_equal(o.call_function("withScope", '["first"]'), "first"),
                ]),
                tr.test_scope("Second call: inner var is fresh each call", [
                    tr.assert_strict_equal(o.call_function("withScope", '["second"]'), "second"),
                ]),
                tr.test_scope("Inner scope var is not visible outside the function", [
                    tr.assert_not(o.scope_var_exists("inner", "all scopes")),
                ]),
            ])]),
        ]),
    ]

    return TestProject(blocks, extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])


def test_utilities() -> TestProject:
    blocks = [
        tr.test_scope("Utilities Blocks", [

            # ------------------------------------------------------------------ #
            tr.test_scope("nothing", [
                tr.test_scope("Nothing is its own type", [
                    tr.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
                ]),
                tr.test_scope("Nothing equals itself via string comparison", [
                    tr.assert_unstrict_equal(o.nothing(), o.nothing()),
                ]),
                tr.test_scope("Nothing is identical to itself (same singleton)", [
                    tr.assert_(o.check_identity(o.nothing(), o.nothing())),
                ]),
                tr.test_scope("Nothing is not identical to any other value", [
                    tr.assert_not(o.check_identity(o.nothing(), "0")),
                    tr.assert_not(o.check_identity(o.nothing(), "")),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("typeofValue", [
                tr.test_scope("Primitive types", [
                    tr.assert_unstrict_equal(o.typeof_value("hello"), o.typeof_value_selection("String")),
                    tr.assert_unstrict_equal(o.typeof_value("42"), o.typeof_value_selection("Number")),
                    tr.assert_unstrict_equal(o.typeof_value(h.operator.true_boolean()), o.typeof_value_selection("Boolean")),
                ]),
                tr.test_scope("GCE types", [
                    tr.assert_unstrict_equal(o.typeof_value(o.nothing()), o.typeof_value_selection("Nothing (GCE)")),
                    tr.assert_unstrict_equal(
                        o.typeof_value(o.create_function_named("f", [o.return_value("x")])),
                        o.typeof_value_selection("Function (GCE)")
                    ),
                    tr.assert_unstrict_equal(
                        o.typeof_value(o.create_class_named("MyClass", [])),
                        o.typeof_value_selection("Class (GCE)")
                    ),
                    tr.assert_unstrict_equal(
                        o.typeof_value(o.create_instance(o.create_class_named("MyClass", []), '[]')),
                        o.typeof_value_selection("Class Instance (GCE)")
                    ),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("typeofValueIsMenu", [
                tr.test_scope("Correct type returns true", [
                    tr.assert_(o.typeof_value_is_menu("hello", "String")),
                    tr.assert_(o.typeof_value_is_menu("42", "Number")),
                    tr.assert_(o.typeof_value_is_menu(h.operator.true_boolean(), "Boolean")),
                    tr.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
                ]),
                tr.test_scope("Wrong type returns false", [
                    tr.assert_not(o.typeof_value_is_menu("hello", "Number")),
                    tr.assert_not(o.typeof_value_is_menu("42", "String")),
                    tr.assert_not(o.typeof_value_is_menu(o.nothing(), "String")),
                ]),
                tr.test_scope("typeofValueIsMenu is consistent with typeofValue", [
                    o.create_var_scope([
                        o.set_scope_var("fn", o.create_function_named("g", [o.return_value("y")])),
                        tr.assert_(o.typeof_value_is_menu(o.get_scope_var("fn"), "Function (GCE)")),
                        tr.assert_not(o.typeof_value_is_menu(o.get_scope_var("fn"), "Class (GCE)")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("typeofValueSelection", [
                tr.test_scope("The reporter returns the menu value as a string", [
                    tr.assert_unstrict_equal(o.typeof_value_selection("String"), "String"),
                    tr.assert_unstrict_equal(o.typeof_value_selection("Nothing (GCE)"), "Nothing (GCE)"),
                    tr.assert_unstrict_equal(o.typeof_value_selection("Function (GCE)"), "Function (GCE)"),
                ]),
                tr.test_scope("Result matches typeofValue output", [
                    tr.assert_(h.operator.equals(o.typeof_value(o.nothing()), o.typeof_value_selection("Nothing (GCE)"))),
                    tr.assert_(h.operator.equals(o.typeof_value("test"), o.typeof_value_selection("String"))),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("objectAsString", [
                tr.test_scope("Primitive values stringify as-is", [
                    tr.assert_unstrict_equal(o.object_as_string("hello"), "hello"),
                    tr.assert_unstrict_equal(o.object_as_string("42"), "42"),
                ]),
                tr.test_scope("Nothing stringifies to its representation", [
                    tr.assert_does_not_throw([
                        o.execute_expression(o.object_as_string(o.nothing())),
                    ]),
                ]),
                tr.test_scope("Instance without as-string method: no error, returns some string", [
                    o.create_var_scope([
                        o.create_class_at("Plain", []),
                        o.set_scope_var("inst", o.create_instance("Plain", '[]')),
                        tr.assert_does_not_throw([
                            o.execute_expression(o.object_as_string(o.get_scope_var("inst"))),
                        ]),
                        tr.assert_(o.typeof_value_is_menu(o.object_as_string(o.get_scope_var("inst")), "String")),
                    ]),
                ]),
                tr.test_scope("Instance WITH as-string method: calls the method", [
                    o.create_var_scope([
                        o.create_class_at("Stringable", [
                            o.define_special_method("as string", [
                                o.return_value("custom-string"),
                            ]),
                        ]),
                        o.set_scope_var("inst", o.create_instance("Stringable", '[]')),
                        tr.assert_unstrict_equal(o.object_as_string(o.get_scope_var("inst")), "custom-string"),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("checkIdentity", [
                tr.test_scope("Two separate instances of the same class are NOT identical", [
                    o.create_var_scope([
                        o.create_class_at("MyClass", []),
                        o.set_scope_var("a", o.create_instance("MyClass", '[]')),
                        o.set_scope_var("b", o.create_instance("MyClass", '[]')),
                        tr.assert_not(o.check_identity(o.get_scope_var("a"), o.get_scope_var("b"))),
                    ]),
                ]),
                tr.test_scope("The same instance stored in two variables IS identical", [
                    o.create_var_scope([
                        o.create_class_at("MyClass", []),
                        o.set_scope_var("a", o.create_instance("MyClass", '[]')),
                        o.set_scope_var("b", o.get_scope_var("a")),
                        tr.assert_(o.check_identity(o.get_scope_var("a"), o.get_scope_var("b"))),
                    ]),
                ]),
                tr.test_scope("Nothing is identical to itself", [
                    tr.assert_(o.check_identity(o.nothing(), o.nothing())),
                ]),
                tr.test_scope("Nothing is not identical to a function", [
                    tr.assert_not(o.check_identity(
                        o.nothing(),
                        o.create_function_named("h", [o.return_value("z")]),
                    )),
                ]),
                tr.test_scope("Two separately created functions are NOT identical", [
                    o.create_var_scope([
                        o.set_scope_var("f1", o.create_function_named("fn1", [o.return_value("r")])),
                        o.set_scope_var("f2", o.create_function_named("fn2", [o.return_value("r")])),
                        tr.assert_not(o.check_identity(o.get_scope_var("f1"), o.get_scope_var("f2"))),
                    ]),
                ]),
                tr.test_scope("Primitive strings identical", [
                    tr.assert_(o.check_identity("hello", "hello")),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("executeExpression", [
                tr.test_scope("Evaluate a reporter block as a command (no error)", [
                    tr.assert_does_not_throw([
                        o.execute_expression(o.nothing()),
                    ]),
                ]),
                tr.test_scope("executeExpression propagates errors from its subexpression", [
                    tr.assert_throws([
                        o.execute_expression(o.get_scope_var("__missing__")),
                    ]),
                ]),
                tr.test_scope("executeExpression can evaluate any reporter", [
                    tr.assert_does_not_throw([
                        o.execute_expression(o.typeof_value("test")),
                    ]),
                    tr.assert_does_not_throw([
                        o.execute_expression(o.object_as_string("hello")),
                    ]),
                ]),
                tr.test_scope("executeExpression can call a function and discard the return value", [
                    o.create_var_scope([
                        o.create_function_at("noopFn", [
                            o.return_value("done"),
                        ]),
                        tr.assert_does_not_throw([
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
        tr.test_scope("Instance Methods", [

            tr.test_scope("basic method call", [
                tr.test_scope("Define class with methods, call them on an instance", [
                    o.create_var_scope([
                        o.create_class_at("Greeter", [
                            o.configure_next_function_args('["name"]', '[]'),
                            o.define_instance_method("greet", [
                                o.return_value(h.operator.join3("Hello, ", o.get_scope_var("name"), "!")),
                            ]),
                            o.define_instance_method("getType", [
                                o.return_value(o.typeof_value(o.self_value())),
                            ]),
                            o.define_instance_method("getAttr", [
                                o.return_value(o.get_attribute("label", o.self_value())),
                            ]),
                        ]),
                        o.set_scope_var("g", o.create_instance("Greeter", '[]')),
                        o.set_attribute(o.get_scope_var("g"), "label", "test-label"),

                        tr.test_scope("Method with arg", [
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "greet", '["World"]'),
                                "Hello, World!",
                            ),
                        ]),
                        tr.test_scope("Same method with different arg", [
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "greet", '["Alice"]'),
                                "Hello, Alice!",
                            ),
                        ]),
                        tr.test_scope("No-arg method returns correct type string", [
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "getType", '[]'),
                                o.typeof_value_selection("Class Instance (GCE)"),
                            ),
                        ]),
                        tr.test_scope("Method reads self attribute", [
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "getAttr", '[]'),
                                "test-label",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("self is the correct instance", [
                tr.test_scope("Two instances with different attribute values", [
                    o.create_var_scope([
                        o.create_class_at("Box", [
                            o.define_instance_method("describe", [
                                o.return_value(h.operator.join("Box-", o.get_attribute("id", o.self_value()))),
                            ]),
                        ]),
                        o.set_scope_var("b1", o.create_instance("Box", '[]')),
                        o.set_scope_var("b2", o.create_instance("Box", '[]')),
                        o.set_attribute(o.get_scope_var("b1"), "id", "AAA"),
                        o.set_attribute(o.get_scope_var("b2"), "id", "BBB"),
                        tr.assert_unstrict_equal(o.call_method(o.get_scope_var("b1"), "describe", '[]'), "Box-AAA"),
                        tr.assert_unstrict_equal(o.call_method(o.get_scope_var("b2"), "describe", '[]'), "Box-BBB"),
                        tr.test_scope("self is distinct for each instance", [
                            tr.assert_not(o.check_identity(o.get_scope_var("b1"), o.get_scope_var("b2"))),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("error cases", [
                tr.test_scope("Calling an undefined method throws", [
                    o.create_var_scope([
                        o.create_class_at("Empty", []),
                        o.set_scope_var("e", o.create_instance("Empty", '[]')),
                        tr.assert_throws([
                            o.execute_expression(o.call_method(o.get_scope_var("e"), "nonExistent", '[]')),
                        ]),
                    ]),
                ]),
                tr.test_scope("Calling a method on a non-instance throws", [
                    tr.assert_throws([
                        o.execute_expression(o.call_method("not-an-instance", "anyMethod", '[]')),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("method with yield point", [
                tr.test_scope("Method body that includes sayforsecs (yielding block) returns correctly and waits", [
                    o.create_var_scope([
                        o.create_class_at("Speaker", [
                            o.configure_next_function_args('["msg"]', '[]'),
                            o.define_instance_method("speak", [
                                h.looks.sayforsecs(o.get_scope_var("msg"), "0.5"),
                                o.return_value(h.operator.join("said: ", o.get_scope_var("msg"))),
                            ]),
                        ]),
                        o.set_scope_var("s", o.create_instance("Speaker", '[]')),
                        tr.test_scope("Return value is correct after yield", [
                            h.sensing.resettimer(),
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("s"), "speak", '["hello"]'),
                                "said: hello",
                            ),
                            tr.test_scope("At least 0.4s elapsed (sayforsecs 0.5s actually waited)", [
                                tr.assert_(h.operator.gt(h.sensing.timer(), "0.4")),
                            ]),
                        ]),
                        tr.test_scope("Second call also returns correctly and also waits", [
                            h.sensing.resettimer(),
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("s"), "speak", '["world"]'),
                                "said: world",
                            ),
                            tr.test_scope("At least 0.4s elapsed on second call too", [
                                tr.assert_(h.operator.gt(h.sensing.timer(), "0.4")),
                            ]),
                        ]),
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
        tr.test_scope("Special Method: init", [

            tr.test_scope("init sets attributes from args", [
                tr.test_scope("Define class whose init sets x and y from positional args", [
                    o.create_var_scope([
                        o.create_class_at("Point", [
                            o.configure_next_function_args('["x","y"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self_value(), "x", o.get_scope_var("x")),
                                o.set_attribute(o.self_value(), "y", o.get_scope_var("y")),
                            ]),
                        ]),
                        o.set_scope_var("p", o.create_instance("Point", '["3","4"]')),
                        tr.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("p")), "3"),
                        tr.assert_unstrict_equal(o.get_attribute("y", o.get_scope_var("p")), "4"),
                        tr.test_scope("Second instance has independent values", [
                            o.set_scope_var("q", o.create_instance("Point", '["10","20"]')),
                            tr.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("q")), "10"),
                            tr.assert_unstrict_equal(o.get_attribute("y", o.get_scope_var("q")), "20"),
                        ]),
                        tr.test_scope("First instance unchanged after second is created", [
                            tr.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("p")), "3"),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("init with default args", [
                tr.test_scope("Defaults fill in when args omitted", [
                    o.create_var_scope([
                        o.create_class_at("Color", [
                            o.configure_next_function_args('["r","g","b"]', '["0","0","0"]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self_value(), "r", o.get_scope_var("r")),
                                o.set_attribute(o.self_value(), "g", o.get_scope_var("g")),
                                o.set_attribute(o.self_value(), "b", o.get_scope_var("b")),
                            ]),
                        ]),
                        tr.test_scope("All defaults: r=0, g=0, b=0", [
                            o.set_scope_var("black", o.create_instance("Color", '[]')),
                            tr.assert_unstrict_equal(o.get_attribute("r", o.get_scope_var("black")), "0"),
                            tr.assert_unstrict_equal(o.get_attribute("g", o.get_scope_var("black")), "0"),
                            tr.assert_unstrict_equal(o.get_attribute("b", o.get_scope_var("black")), "0"),
                        ]),
                        tr.test_scope("Partial override: r=255", [
                            o.set_scope_var("red", o.create_instance("Color", '["255"]')),
                            tr.assert_unstrict_equal(o.get_attribute("r", o.get_scope_var("red")), "255"),
                            tr.assert_unstrict_equal(o.get_attribute("g", o.get_scope_var("red")), "0"),
                        ]),
                        tr.test_scope("Full args", [
                            o.set_scope_var("custom", o.create_instance("Color", '["10","20","30"]')),
                            tr.assert_unstrict_equal(o.get_attribute("b", o.get_scope_var("custom")), "30"),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("subclass init calls super init", [
                tr.test_scope("Subclass init calls callSuperInitMethod", [
                    o.create_var_scope([
                        o.create_class_at("Shape", [
                            o.configure_next_function_args('["color"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self_value(), "color", o.get_scope_var("color")),
                            ]),
                        ]),
                        o.create_subclass_at("Circle", "Shape", [
                            o.configure_next_function_args('["radius","color"]', '[]'),
                            o.define_special_method("init", [
                                o.execute_expression(o.call_super_init_method('["blue"]')),
                                o.set_attribute(o.self_value(), "radius", o.get_scope_var("radius")),
                            ]),
                        ]),
                        o.set_scope_var("c", o.create_instance("Circle", '["5","ignored"]')),
                        tr.test_scope("radius set by Circle init", [
                            tr.assert_unstrict_equal(o.get_attribute("radius", o.get_scope_var("c")), "5"),
                        ]),
                        tr.test_scope("color set by super (Shape) init with hardcoded value", [
                            tr.assert_unstrict_equal(o.get_attribute("color", o.get_scope_var("c")), "blue"),
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
        tr.test_scope("Inheritance and Super", [

            tr.test_scope("isSubclass", [
                o.create_var_scope([
                    o.create_class_at("A", []),
                    o.create_subclass_at("B", "A", []),
                    o.create_subclass_at("C", "B", []),
                    tr.test_scope("Direct subclass", [
                        tr.assert_(o.is_subclass("B", "A")),
                    ]),
                    tr.test_scope("Transitive subclass", [
                        tr.assert_(o.is_subclass("C", "A")),
                        tr.assert_(o.is_subclass("C", "B")),
                    ]),
                    tr.test_scope("Reverse is false", [
                        tr.assert_not(o.is_subclass("A", "B")),
                        tr.assert_not(o.is_subclass("A", "C")),
                    ]),
                    tr.test_scope("A class is a subclass of itself", [
                        tr.assert_(o.is_subclass("A", "A")),
                    ]),
                ]),
            ]),

            tr.test_scope("isInstance with inheritance", [
                o.create_var_scope([
                    o.create_class_at("Vehicle", []),
                    o.create_subclass_at("Car", "Vehicle", []),
                    o.set_scope_var("v", o.create_instance("Vehicle", '[]')),
                    o.set_scope_var("c", o.create_instance("Car", '[]')),
                    tr.test_scope("Instance is instance of own class", [
                        tr.assert_(o.is_instance(o.get_scope_var("v"), "Vehicle")),
                        tr.assert_(o.is_instance(o.get_scope_var("c"), "Car")),
                    ]),
                    tr.test_scope("Subclass instance is instance of superclass", [
                        tr.assert_(o.is_instance(o.get_scope_var("c"), "Vehicle")),
                    ]),
                    tr.test_scope("Superclass instance is NOT instance of subclass", [
                        tr.assert_not(o.is_instance(o.get_scope_var("v"), "Car")),
                    ]),
                ]),
            ]),

            tr.test_scope("method override and super", [
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
                    tr.test_scope("Overridden method returns augmented result", [
                        tr.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("d"), "speak", '[]'),
                            "generic sound (but louder)",
                        ),
                    ]),
                    tr.test_scope("Parent method still returns original", [
                        tr.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("a"), "speak", '[]'),
                            "generic sound",
                        ),
                    ]),
                    tr.test_scope("Inherited (non-overridden) method works on subclass", [
                        tr.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("d"), "breathe", '[]'),
                            "breathing",
                        ),
                    ]),
                ]),
            ]),

            tr.test_scope("getSuperclass", [
                o.create_var_scope([
                    o.create_class_at("Base", []),
                    o.create_subclass_at("Child", "Base", []),
                    tr.test_scope("Superclass of Child is Base", [
                        tr.assert_text_in_value("Base", o.get_superclass("Child")),
                    ]),
                    tr.test_scope("Superclass of Base is built-in Superclass", [
                        tr.assert_text_in_value("Superclass", o.get_superclass("Base")),
                    ]),
                    tr.test_scope("getSuperclass on a missing class name throws", [
                        tr.assert_throws([
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
        tr.test_scope("Getters and Setters", [

            tr.test_scope("setter transforms and stores, getter retrieves", [
                tr.test_scope("Setter prepends 'set:'; getter appends ':get'", [
                    o.create_var_scope([
                        o.create_class_at("Box", [
                            o.define_setter("size", [
                                o.set_attribute(
                                    o.self_value(), "_size",
                                    h.operator.join("set:", o.define_setter_value()),
                                ),
                            ]),
                            o.define_getter("size", [
                                o.return_value(
                                    h.operator.join(o.get_attribute("_size", o.self_value()), ":get"),
                                ),
                            ]),
                        ]),
                        o.set_scope_var("b", o.create_instance("Box", '[]')),
                        tr.test_scope("setAttribute goes through setter", [
                            o.set_attribute(o.get_scope_var("b"), "size", "42"),
                        ]),
                        tr.test_scope("Raw _size attribute reflects setter transformation", [
                            tr.assert_unstrict_equal(o.get_attribute("_size", o.get_scope_var("b")), "set:42"),
                        ]),
                        tr.test_scope("getAttribute goes through getter", [
                            tr.assert_unstrict_equal(o.get_attribute("size", o.get_scope_var("b")), "set:42:get"),
                        ]),
                        tr.test_scope("Update via setter replaces stored value", [
                            o.set_attribute(o.get_scope_var("b"), "size", "hello"),
                            tr.assert_unstrict_equal(o.get_attribute("_size", o.get_scope_var("b")), "set:hello"),
                            tr.assert_unstrict_equal(o.get_attribute("size", o.get_scope_var("b")), "set:hello:get"),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("getter-only attribute", [
                tr.test_scope("Getter for computed read-only value", [
                    o.create_var_scope([
                        o.create_class_at("Circle", [
                            o.define_getter("doubled", [
                                o.return_value(h.operator.multiply(
                                    o.get_attribute("_val", o.self_value()), "2",
                                )),
                            ]),
                        ]),
                        o.set_scope_var("c", o.create_instance("Circle", '[]')),
                        o.set_attribute(o.get_scope_var("c"), "_val", "7"),
                        tr.test_scope("getter doubles _val", [
                            tr.assert_strict_equal(o.get_attribute("doubled", o.get_scope_var("c")), "14"),
                        ]),
                        tr.test_scope("Raw _val unaffected", [
                            tr.assert_strict_equal(o.get_attribute("_val", o.get_scope_var("c")), "7"),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("attributes without getter/setter bypass directly", [
                tr.test_scope("setAttribute and getAttribute on plain attributes", [
                    o.create_var_scope([
                        o.create_class_at("Plain", []),
                        o.set_scope_var("p", o.create_instance("Plain", '[]')),
                        o.set_attribute(o.get_scope_var("p"), "x", "99"),
                        tr.assert_unstrict_equal(o.get_attribute("x", o.get_scope_var("p")), "99"),
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
        tr.test_scope("Operator Methods", [

            tr.test_scope("left add operator", [
                tr.test_scope("Custom class with left add: returns val + operand", [
                    o.create_var_scope([
                        o.create_class_at("MyNum", [
                            o.configure_next_function_args('["val"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self_value(), "val", o.get_scope_var("val")),
                            ]),
                            o.define_operator_method("left add", [
                                o.return_value(h.operator.add(
                                    o.get_attribute("val", o.self_value()),
                                    o.operator_operator_value(),
                                )),
                            ]),
                            o.define_operator_method("left subtract", [
                                o.return_value(h.operator.subtract(
                                    o.get_attribute("val", o.self_value()),
                                    o.operator_operator_value(),
                                )),
                            ]),
                        ]),
                        o.set_scope_var("n", o.create_instance("MyNum", '["10"]')),
                        tr.test_scope("left add: 10 + 5 = 15", [
                            tr.assert_strict_equal(h.operator.add(o.get_scope_var("n"), "5"), "15"),
                        ]),
                        tr.test_scope("left add: 10 + 0 = 10", [
                            tr.assert_strict_equal(h.operator.add(o.get_scope_var("n"), "0"), "10"),
                        ]),
                        tr.test_scope("left subtract: 10 - 3 = 7", [
                            tr.assert_strict_equal(h.operator.subtract(o.get_scope_var("n"), "3"), "7"),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("equals operator", [
                tr.test_scope("Custom equals: compares val attribute", [
                    o.create_var_scope([
                        o.create_class_at("Token", [
                            o.configure_next_function_args('["id"]', '[]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self_value(), "id", o.get_scope_var("id")),
                            ]),
                            o.define_operator_method("equals", [
                                o.return_value(h.operator.equals(
                                    o.get_attribute("id", o.self_value()),
                                    o.operator_operator_value(),
                                )),
                            ]),
                        ]),
                        o.set_scope_var("tok", o.create_instance("Token", '["abc"]')),
                        tr.test_scope("Equals the stored id", [
                            tr.assert_(h.operator.equals(o.get_scope_var("tok"), "abc")),
                        ]),
                        tr.test_scope("Does not equal a different value", [
                            tr.assert_not(h.operator.equals(o.get_scope_var("tok"), "xyz")),
                            tr.assert_not(h.operator.equals(o.get_scope_var("tok"), "")),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("reverse operations", [
                tr.test_scope("Right-side method is used when left operand has no matching method", [
                    o.create_var_scope([
                        o.create_class_at("RightOnly", [
                            # Only defines right add; no left add
                            o.define_operator_method("right add", [
                                o.return_value(h.operator.join("R+", o.operator_operator_value())),
                            ]),
                        ]),
                        o.set_scope_var("r", o.create_instance("RightOnly", '[]')),
                        tr.test_scope("plain_number + instance: triggers right add", [
                            # operator_operator_value() in right add is the left operand ("7")
                            tr.assert_unstrict_equal(
                                h.operator.add("7", o.get_scope_var("r")),
                                "R+7",
                            ),
                        ]),
                    ]),
                ]),
                tr.test_scope("Comparison reverse: op.greater triggers right-side less-than method", [
                    o.create_var_scope([
                        o.create_class_at("CompRight", [
                            # Only defines less than; when used as right of >, operator_value = left operand
                            o.define_operator_method("less than", [
                                o.return_value(h.operator.lt(
                                    o.operator_operator_value(),
                                    o.get_attribute("threshold", o.self_value()),
                                )),
                            ]),
                        ]),
                        o.set_scope_var("c", o.create_instance("CompRight", '[]')),
                        o.set_attribute(o.get_scope_var("c"), "threshold", "10"),
                        tr.test_scope("5 > c: triggers c's less-than with operator_value=5; 5<10 is true", [
                            tr.assert_(h.operator.gt("5", o.get_scope_var("c"))),
                        ]),
                        tr.test_scope("15 > c: operator_value=15; 15<10 is false", [
                            tr.assert_not(h.operator.gt("15", o.get_scope_var("c"))),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("all operator kinds", [
                tr.test_scope("Arithmetic operator kinds: each left/right variant is callable", [
                    o.create_var_scope([
                        o.create_class_at("ArithOps", [
                            o.define_operator_method("left add",       [o.return_value("L+")]),
                            o.define_operator_method("right add",      [o.return_value("R+")]),
                            o.define_operator_method("left subtract",  [o.return_value("L-")]),
                            o.define_operator_method("right subtract", [o.return_value("R-")]),
                            o.define_operator_method("left multiply",  [o.return_value("L*")]),
                            o.define_operator_method("right multiply", [o.return_value("R*")]),
                            o.define_operator_method("left divide",    [o.return_value("L/")]),
                            o.define_operator_method("right divide",   [o.return_value("R/")]),
                            o.define_operator_method("left power",     [o.return_value("L^")]),
                            o.define_operator_method("right power",    [o.return_value("R^")]),
                            o.define_operator_method("left mod",       [o.return_value("L%")]),
                            o.define_operator_method("right mod",      [o.return_value("R%")]),
                        ]),
                        o.set_scope_var("a", o.create_instance("ArithOps", '[]')),
                        tr.test_scope("Left-side arithmetic methods", [
                            tr.assert_strict_equal(h.operator.add(o.get_scope_var("a"), "0"),      "L+"),
                            tr.assert_strict_equal(h.operator.subtract(o.get_scope_var("a"), "0"), "L-"),
                            tr.assert_strict_equal(h.operator.multiply(o.get_scope_var("a"), "1"), "L*"),
                            tr.assert_strict_equal(h.operator.divide(o.get_scope_var("a"), "1"),   "L/"),
                            tr.assert_strict_equal(h.operator.power(o.get_scope_var("a"), "1"),    "L^"),
                            tr.assert_strict_equal(h.operator.mod(o.get_scope_var("a"), "1"),      "L%"),
                        ]),
                        tr.test_scope("Right-side arithmetic methods (plain number on left)", [
                            tr.assert_strict_equal(h.operator.add("0", o.get_scope_var("a")),      "R+"),
                            tr.assert_strict_equal(h.operator.subtract("0", o.get_scope_var("a")), "R-"),
                            tr.assert_strict_equal(h.operator.multiply("1", o.get_scope_var("a")), "R*"),
                            tr.assert_strict_equal(h.operator.divide("1", o.get_scope_var("a")),   "R/"),
                            tr.assert_strict_equal(h.operator.power("1", o.get_scope_var("a")),    "R^"),
                            tr.assert_strict_equal(h.operator.mod("1", o.get_scope_var("a")),      "R%"),
                        ]),
                    ]),
                ]),
                tr.test_scope("Comparison operator kinds: each kind is callable", [
                    o.create_var_scope([
                        o.create_class_at("CompOps", [
                            o.define_operator_method("equals",           [o.return_value(h.operator.true_boolean())]),
                            o.define_operator_method("not equals",       [o.return_value(h.operator.true_boolean())]),
                            o.define_operator_method("greater than",     [o.return_value(h.operator.true_boolean())]),
                            o.define_operator_method("greater or equal", [o.return_value(h.operator.true_boolean())]),
                            o.define_operator_method("less than",        [o.return_value(h.operator.true_boolean())]),
                            o.define_operator_method("less or equal",    [o.return_value(h.operator.true_boolean())]),
                        ]),
                        o.set_scope_var("c", o.create_instance("CompOps", '[]')),
                        tr.assert_(h.operator.equals(o.get_scope_var("c"), "x")),
                        tr.assert_(h.operator.notequal(o.get_scope_var("c"), "x")),
                        tr.assert_(h.operator.gt(o.get_scope_var("c"), "x")),
                        tr.assert_(h.operator.gtorequal(o.get_scope_var("c"), "x")),
                        tr.assert_(h.operator.lt(o.get_scope_var("c"), "x")),
                        tr.assert_(h.operator.ltorequal(o.get_scope_var("c"), "x")),
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
        tr.test_scope("Static Methods", [

            tr.test_scope("define and call a static method", [
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
                    tr.test_scope("callStaticMethod: square(4) = 16", [
                        tr.assert_strict_equal(
                            o.call_static_method("MathUtils", "square", '["4"]'),
                            "16",
                        ),
                    ]),
                    tr.test_scope("callStaticMethod: square(0) = 0", [
                        tr.assert_strict_equal(
                            o.call_static_method("MathUtils", "square", '["0"]'),
                            "0",
                        ),
                    ]),
                    tr.test_scope("callStaticMethod: add(3, 7) = 10", [
                        tr.assert_strict_equal(
                            o.call_static_method("MathUtils", "add", '["3","7"]'),
                            "10",
                        ),
                    ]),
                ]),
            ]),

            tr.test_scope("getStaticMethodFunc + callFunction", [
                o.create_var_scope([
                    o.create_class_at("Fmt", [
                        o.configure_next_function_args('["val"]', '[]'),
                        o.define_static_method("wrap", [
                            o.return_value(h.operator.join3(
                                "[", o.get_scope_var("val"), "]",
                            )),
                        ]),
                    ]),
                    tr.test_scope("getStaticMethodFunc returns a callable function", [
                        o.set_scope_var("wrapFn", o.get_static_method_func("wrap", "Fmt")),
                        tr.assert_unstrict_equal(o.typeof_value(o.get_scope_var("wrapFn")), o.typeof_value_selection("Function (GCE)")),
                    ]),
                    tr.test_scope("callFunction on retrieved static method", [
                        tr.assert_unstrict_equal(
                            o.call_function("wrapFn", '["hello"]'),
                            "[hello]",
                        ),
                    ]),
                    tr.test_scope("Both callStaticMethod and callFunction give same result", [
                        tr.assert_unstrict_equal(
                            o.call_static_method("Fmt", "wrap", '["world"]'),
                            o.call_function("wrapFn", '["world"]'),
                        ),
                    ]),
                ]),
            ]),

            tr.test_scope("error cases", [
                o.create_var_scope([
                    o.create_class_at("Solo", []),
                    tr.test_scope("Calling a non-existent static method throws", [
                        tr.assert_throws([
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
        tr.test_scope("Class Variables", [

            tr.test_scope("set and get class variable", [
                o.create_var_scope([
                    o.create_class_at("Counter", []),
                    tr.test_scope("Set and read a class variable", [
                        o.set_class_variable("Counter", "count", "0"),
                        tr.assert_unstrict_equal(o.get_class_variable("count", "Counter"), "0"),
                    ]),
                    tr.test_scope("Update the class variable", [
                        o.set_class_variable("Counter", "count", "42"),
                        tr.assert_unstrict_equal(o.get_class_variable("count", "Counter"), "42"),
                    ]),
                    tr.test_scope("Multiple class variables coexist", [
                        o.set_class_variable("Counter", "name", "MyCounter"),
                        tr.assert_unstrict_equal(o.get_class_variable("name", "Counter"), "MyCounter"),
                    ]),
                    tr.test_scope("Reading first variable unchanged", [
                        tr.assert_unstrict_equal(o.get_class_variable("count", "Counter"), "42"),
                    ]),
                ]),
            ]),

            tr.test_scope("propertyNamesOfClass reflects class variables", [
                o.create_var_scope([
                    o.create_class_at("Config", [
                        o.define_instance_method("doWork", [
                            o.return_value("done"),
                        ]),
                    ]),
                    o.set_class_variable("Config", "version", "1"),
                    o.set_class_variable("Config", "author", "test"),
                    tr.test_scope("Class variable names listed", [
                        tr.assert_text_in_value("version", o.property_names_of_class("class variable", "Config")),
                        tr.assert_text_in_value("author", o.property_names_of_class("class variable", "Config")),
                    ]),
                    tr.test_scope("Method names NOT in class variable list", [
                        tr.assert_text_not_in_value("doWork", o.property_names_of_class("class variable", "Config")),
                    ]),
                    tr.test_scope("Instance method names listed correctly", [
                        tr.assert_text_in_value("doWork", o.property_names_of_class("instance method", "Config")),
                    ]),
                    tr.test_scope("Class variable names NOT in instance method list", [
                        tr.assert_text_not_in_value("version", o.property_names_of_class("instance method", "Config")),
                    ]),
                ]),
            ]),

            tr.test_scope("delete class variable", [
                o.create_var_scope([
                    o.create_class_at("Bag", []),
                    o.set_class_variable("Bag", "keep", "yes"),
                    o.set_class_variable("Bag", "remove", "no"),
                    tr.test_scope("Both exist before delete", [
                        tr.assert_text_in_value("keep", o.property_names_of_class("class variable", "Bag")),
                        tr.assert_text_in_value("remove", o.property_names_of_class("class variable", "Bag")),
                    ]),
                    tr.test_scope("Delete one", [
                        o.delete_class_variable("Bag", "remove"),
                    ]),
                    tr.test_scope("Deleted variable throws on get", [
                        tr.assert_throws([
                            o.execute_expression(o.get_class_variable("remove", "Bag")),
                        ]),
                    ]),
                    tr.test_scope("Deleted variable absent from property names", [
                        tr.assert_text_not_in_value("remove", o.property_names_of_class("class variable", "Bag")),
                    ]),
                    tr.test_scope("Other variable unaffected", [
                        tr.assert_text_in_value("keep", o.property_names_of_class("class variable", "Bag")),
                        tr.assert_unstrict_equal(o.get_class_variable("keep", "Bag"), "yes"),
                    ]),
                ]),
            ]),

            tr.test_scope("class variables are shared across instances", [
                o.create_var_scope([
                    o.create_class_at("Shared", [
                        o.define_instance_method("getVar", [
                            o.return_value(o.get_class_variable("shared", "Shared")),
                        ]),
                    ]),
                    o.set_class_variable("Shared", "shared", "initial"),
                    o.set_scope_var("i1", o.create_instance("Shared", '[]')),
                    o.set_scope_var("i2", o.create_instance("Shared", '[]')),
                    tr.test_scope("Both instances see the same class variable", [
                        tr.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("i1"), "getVar", '[]'),
                            "initial",
                        ),
                        tr.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("i2"), "getVar", '[]'),
                            "initial",
                        ),
                    ]),
                    tr.test_scope("Update class variable - both instances see new value", [
                        o.set_class_variable("Shared", "shared", "updated"),
                        tr.assert_unstrict_equal(
                            o.call_method(o.get_scope_var("i1"), "getVar", '[]'),
                            "updated",
                        ),
                        tr.assert_unstrict_equal(
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


def test_class_definitions() -> TestProject:
    blocks = [
        tr.test_scope("Class Definition and Inheritance Blocks", [

            # ------------------------------------------------------------------ #
            tr.test_scope("createClassAt", [
                tr.test_scope("Class is accessible by name and typeof is Class (GCE)", [
                    o.create_var_scope([
                        o.create_class_at("MyClass", []),
                        tr.assert_unstrict_equal(o.typeof_value(o.get_scope_var("MyClass")), o.typeof_value_selection("Class (GCE)")),
                        tr.test_scope("Can create an instance immediately", [
                            o.set_scope_var("inst", o.create_instance("MyClass", '[]')),
                            tr.assert_(o.typeof_value_is_menu(o.get_scope_var("inst"), "Class Instance (GCE)")),
                            tr.assert_(o.is_instance(o.get_scope_var("inst"), "MyClass")),
                        ]),
                    ]),
                ]),
                tr.test_scope("Class with methods and init defined inline", [
                    o.create_var_scope([
                        o.create_class_at("Counter", [
                            o.configure_next_function_args('["start"]', '["0"]'),
                            o.define_special_method("init", [
                                o.set_attribute(o.self_value(), "count", o.get_scope_var("start")),
                            ]),
                            o.define_instance_method("value", [
                                o.return_value(o.get_attribute("count", o.self_value())),
                            ]),
                        ]),
                        o.set_scope_var("c", o.create_instance("Counter", '["5"]')),
                        tr.assert_unstrict_equal(o.call_method(o.get_scope_var("c"), "value", '[]'), "5"),
                        tr.test_scope("Default arg: no args uses default 0", [
                            o.set_scope_var("d", o.create_instance("Counter", '[]')),
                            tr.assert_unstrict_equal(o.call_method(o.get_scope_var("d"), "value", '[]'), "0"),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("createClassNamed (reporter)", [
                tr.test_scope("Create class inline as a reporter value, store and use it", [
                    o.create_var_scope([
                        o.set_scope_var("Dyn", o.create_class_named("DynClass", [
                            o.define_instance_method("ping", [
                                o.return_value("pong"),
                            ]),
                        ])),
                        tr.test_scope("Stored value is a Class (GCE)", [
                            tr.assert_unstrict_equal(o.typeof_value(o.get_scope_var("Dyn")), o.typeof_value_selection("Class (GCE)")),
                        ]),
                        tr.test_scope("Class can be instantiated", [
                            o.set_scope_var("inst", o.create_instance(o.get_scope_var("Dyn"), '[]')),
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("inst"), "ping", '[]'),
                                "pong",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("currentClass", [
                tr.test_scope("currentClass inside createClassAt returns the class being defined", [
                    o.create_var_scope([
                        o.create_class_at("Stamped", [
                            o.set_class_variable(o.current_class(), "tag", "stamped-value"),
                        ]),
                        tr.test_scope("Class variable set via currentClass is accessible by name", [
                            tr.assert_unstrict_equal(o.get_class_variable("tag", "Stamped"), "stamped-value"),
                        ]),
                    ]),
                ]),
                tr.test_scope("currentClass inside createClassNamed also works", [
                    o.create_var_scope([
                        o.set_scope_var("NC", o.create_class_named("NamedCls", [
                            o.set_class_variable(o.current_class(), "info", "from-named"),
                        ])),
                        tr.assert_unstrict_equal(o.get_class_variable("info", o.get_scope_var("NC")), "from-named"),
                    ]),
                ]),
                tr.test_scope("currentClass inside onClass returns the correct class", [
                    o.create_var_scope([
                        o.create_class_at("Extendable", []),
                        o.on_class("Extendable", [
                            o.set_class_variable(o.current_class(), "addedTag", "via-on-class"),
                        ]),
                        tr.assert_unstrict_equal(o.get_class_variable("addedTag", "Extendable"), "via-on-class"),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("createSubclassAt", [
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
                    tr.test_scope("isSubclass reflects the relationship", [
                        tr.assert_(o.is_subclass("Dog", "Animal")),
                        tr.assert_not(o.is_subclass("Animal", "Dog")),
                    ]),
                    tr.test_scope("getSuperclass of Dog is Animal", [
                        tr.assert_text_in_value("Animal", o.get_superclass("Dog")),
                    ]),
                    tr.test_scope("Dog instance can call both inherited and own methods", [
                        o.set_scope_var("d", o.create_instance("Dog", '[]')),
                        tr.assert_unstrict_equal(o.call_method(o.get_scope_var("d"), "breathe", '[]'), "breathing"),
                        tr.assert_unstrict_equal(o.call_method(o.get_scope_var("d"), "bark", '[]'), "woof"),
                    ]),
                    tr.test_scope("currentClass inside subclass body returns the subclass", [
                        o.create_subclass_at("Puppy", "Dog", [
                            o.set_class_variable(o.current_class(), "size", "small"),
                        ]),
                        tr.assert_unstrict_equal(o.get_class_variable("size", "Puppy"), "small"),
                    ]),
                    tr.test_scope("isSubclass is transitive", [
                        tr.assert_(o.is_subclass("Puppy", "Animal")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("createSubclassNamed (reporter)", [
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
                    tr.test_scope("Stored value is a Class (GCE)", [
                        tr.assert_unstrict_equal(o.typeof_value(o.get_scope_var("Sub")), o.typeof_value_selection("Class (GCE)")),
                    ]),
                    tr.test_scope("isSubclass works for reporter-created subclass", [
                        tr.assert_(o.is_subclass(o.get_scope_var("Sub"), "BaseR")),
                    ]),
                    tr.test_scope("Instance inherits from base and has own method", [
                        o.set_scope_var("inst", o.create_instance(o.get_scope_var("Sub"), '[]')),
                        tr.assert_unstrict_equal(o.call_method(o.get_scope_var("inst"), "base", '[]'), "from-base"),
                        tr.assert_unstrict_equal(o.call_method(o.get_scope_var("inst"), "child", '[]'), "from-child"),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("isSubclass", [
                o.create_var_scope([
                    o.create_class_at("A", []),
                    o.create_subclass_at("B", "A", []),
                    o.create_subclass_at("C", "B", []),
                    tr.test_scope("Direct and transitive subclass", [
                        tr.assert_(o.is_subclass("B", "A")),
                        tr.assert_(o.is_subclass("C", "A")),
                        tr.assert_(o.is_subclass("C", "B")),
                    ]),
                    tr.test_scope("Reverse is false", [
                        tr.assert_not(o.is_subclass("A", "B")),
                        tr.assert_not(o.is_subclass("A", "C")),
                    ]),
                    tr.test_scope("A class is kinda a subclass of itself", [
                        tr.assert_(o.is_subclass("A", "A")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("getSuperclass", [
                o.create_var_scope([
                    o.create_class_at("Root", []),
                    o.create_subclass_at("Branch", "Root", []),
                    tr.test_scope("Superclass of Branch is Root", [
                        tr.assert_text_in_value("Root", o.get_superclass("Branch")),
                    ]),
                    tr.test_scope("Root's superclass is the built-in Superclass", [
                        tr.assert_text_in_value("Superclass", o.get_superclass("Root")),
                    ]),
                    tr.test_scope("Superclass of the built-in Superclass is Nothing", [
                        tr.assert_(o.typeof_value_is_menu(o.get_superclass(o.get_superclass("Root")), "Nothing (GCE)")),
                    ]),
                    tr.test_scope("Missing class throws", [
                        tr.assert_throws([
                            o.execute_expression(o.get_superclass("__no_such_class__")),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("onClass: add instance method", [
                tr.test_scope("Define class with no methods, then add one via onClass", [
                    o.create_var_scope([
                        o.create_class_at("Greeter", []),
                        o.on_class("Greeter", [
                            o.configure_next_function_args('["name"]', '[]'),
                            o.define_instance_method("hello", [
                                o.return_value(h.operator.join("Hello, ", o.get_scope_var("name"))),
                            ]),
                        ]),
                        o.set_scope_var("g", o.create_instance("Greeter", '[]')),
                        tr.test_scope("Method added via onClass is callable", [
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("g"), "hello", '["World"]'),
                                "Hello, World",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("onClass: add static method", [
                o.create_var_scope([
                    o.create_class_at("Util", []),
                    o.on_class("Util", [
                        o.configure_next_function_args('["x"]', '[]'),
                        o.define_static_method("double", [
                            o.return_value(h.operator.multiply(o.get_scope_var("x"), "2")),
                        ]),
                    ]),
                    tr.test_scope("Static method added via onClass is callable", [
                        tr.assert_unstrict_equal(
                            o.call_static_method("Util", "double", '["7"]'),
                            "14",
                        ),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("onClass: currentClass inside body", [
                tr.test_scope("currentClass used inside onClass body sets a class variable", [
                    o.create_var_scope([
                        o.create_class_at("Tagged", []),
                        o.on_class("Tagged", [
                            o.set_class_variable(o.current_class(), "source", "on-class"),
                        ]),
                        tr.assert_unstrict_equal(o.get_class_variable("source", "Tagged"), "on-class"),
                        tr.test_scope("Multiple onClass calls accumulate class variables", [
                            o.on_class("Tagged", [
                                o.set_class_variable(o.current_class(), "extra", "second"),
                            ]),
                            tr.assert_unstrict_equal(o.get_class_variable("source", "Tagged"), "on-class"),
                            tr.assert_unstrict_equal(o.get_class_variable("extra", "Tagged"), "second"),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("onClass: visible in propertyNamesOfClass", [
                tr.test_scope("Method added via onClass appears in property list", [
                    o.create_var_scope([
                        o.create_class_at("Widget", []),
                        tr.test_scope("No methods yet", [
                            tr.assert_text_not_in_value("render", o.property_names_of_class("instance method", "Widget")),
                            o.on_class("Widget", [
                                o.define_instance_method("render", [
                                    o.return_value("rendered"),
                                ]),
                            ]),
                        ]),
                        tr.test_scope("Method now listed after onClass", [
                            tr.assert_text_in_value("render", o.property_names_of_class("instance method", "Widget")),
                        ]),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("onClass: cleanup on error", [
                tr.test_scope("class def scope cleanup runs even when body throws", [
                    o.create_var_scope([
                        o.create_class_at("Safe", []),
                        tr.assert_throws([
                            o.on_class("Safe", [
                                o.execute_expression(o.get_scope_var("__missing__")),
                            ]),
                        ]),
                        tr.test_scope("After the error, onClass on same class still works", [
                            tr.assert_does_not_throw([
                                o.on_class("Safe", [
                                    o.define_instance_method("ok", [
                                        o.return_value("ok"),
                                    ]),
                                ]),
                            ]),
                            tr.assert_unstrict_equal(
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
        tr.test_scope("Introspection", [

            tr.test_scope("getAttribute and setAttribute (direct)", [
                o.create_var_scope([
                    o.create_class_at("Person", [
                        o.configure_next_function_args('["name"]', '[]'),
                        o.define_special_method("init", [
                            o.set_attribute(o.self_value(), "name", o.get_scope_var("name")),
                        ]),
                        o.define_instance_method("greet", [
                            o.return_value(h.operator.join("Hi, ", o.get_attribute("name", o.self_value()))),
                        ]),
                    ]),
                    o.create_subclass_at("Employee", "Person", []),
                    o.set_scope_var("p", o.create_instance("Person", '["Bob"]')),
                    o.set_attribute(o.get_scope_var("p"), "age", "30"),
                    tr.test_scope("Attribute set via init", [
                        tr.assert_unstrict_equal(o.get_attribute("name", o.get_scope_var("p")), "Bob"),
                    ]),
                    tr.test_scope("Attribute set after creation", [
                        tr.assert_unstrict_equal(o.get_attribute("age", o.get_scope_var("p")), "30"),
                    ]),
                    tr.test_scope("Overwrite attribute", [
                        o.set_attribute(o.get_scope_var("p"), "name", "Robert"),
                        tr.assert_unstrict_equal(o.get_attribute("name", o.get_scope_var("p")), "Robert"),
                    ]),
                    tr.test_scope("Missing attribute throws", [
                        tr.assert_throws([
                            o.execute_expression(o.get_attribute("missing", o.get_scope_var("p"))),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("getClassOfInstance", [
                o.create_var_scope([
                    o.create_class_at("Cat", []),
                    o.create_subclass_at("Kitten", "Cat", []),
                    o.set_scope_var("c", o.create_instance("Cat", '[]')),
                    o.set_scope_var("k", o.create_instance("Kitten", '[]')),
                    tr.test_scope("getClassOfInstance contains the class name", [
                        tr.assert_text_in_value("Cat", o.get_class_of_instance(o.get_scope_var("c"))),
                        tr.assert_text_in_value("Kitten", o.get_class_of_instance(o.get_scope_var("k"))),
                    ]),
                    tr.test_scope("Cat instance does NOT report Kitten", [
                        tr.assert_text_not_in_value("Kitten", o.get_class_of_instance(o.get_scope_var("c"))),
                    ]),
                ]),
            ]),

            tr.test_scope("isInstance", [
                o.create_var_scope([
                    o.create_class_at("Fruit", []),
                    o.create_subclass_at("Apple", "Fruit", []),
                    o.set_scope_var("f", o.create_instance("Fruit", '[]')),
                    o.set_scope_var("a", o.create_instance("Apple", '[]')),
                    tr.test_scope("Instance of own class", [
                        tr.assert_(o.is_instance(o.get_scope_var("f"), "Fruit")),
                        tr.assert_(o.is_instance(o.get_scope_var("a"), "Apple")),
                    ]),
                    tr.test_scope("Subclass instance is instance of superclass", [
                        tr.assert_(o.is_instance(o.get_scope_var("a"), "Fruit")),
                    ]),
                    tr.test_scope("Superclass instance is NOT instance of subclass", [
                        tr.assert_not(o.is_instance(o.get_scope_var("f"), "Apple")),
                    ]),
                    tr.test_scope("Non-instance values return false", [
                        tr.assert_not(o.is_instance("hello", "Fruit")),
                        tr.assert_not(o.is_instance(o.nothing(), "Fruit")),
                    ]),
                ]),
            ]),

            tr.test_scope("propertyNamesOfClass", [
                o.create_var_scope([
                    o.create_class_at("Widget", [
                        o.define_instance_method("render", [
                            o.return_value("rendered"),
                        ]),
                        o.define_static_method("create", [
                            o.return_value("widget"),
                        ]),
                        o.define_getter("width", [
                            o.return_value(o.get_attribute("_w", o.self_value())),
                        ]),
                        o.define_setter("height", [
                            o.set_attribute(o.self_value(), "_h", o.define_setter_value()),
                        ]),
                    ]),
                    o.set_class_variable("Widget", "version", "2"),
                    tr.test_scope("Instance methods", [
                        tr.assert_text_in_value("render", o.property_names_of_class("instance method", "Widget")),
                        tr.assert_text_not_in_value("create", o.property_names_of_class("instance method", "Widget")),
                    ]),
                    tr.test_scope("Static methods", [
                        tr.assert_text_in_value("create", o.property_names_of_class("static method", "Widget")),
                        tr.assert_text_not_in_value("render", o.property_names_of_class("static method", "Widget")),
                    ]),
                    tr.test_scope("Getter methods", [
                        tr.assert_text_in_value("width", o.property_names_of_class("getter method", "Widget")),
                        tr.assert_text_not_in_value("height", o.property_names_of_class("getter method", "Widget")),
                    ]),
                    tr.test_scope("Setter methods", [
                        tr.assert_text_in_value("height", o.property_names_of_class("setter method", "Widget")),
                        tr.assert_text_not_in_value("width", o.property_names_of_class("setter method", "Widget")),
                    ]),
                    tr.test_scope("Class variables", [
                        tr.assert_text_in_value("version", o.property_names_of_class("class variable", "Widget")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("propertyNamesOfClass edge cases", [
                tr.test_scope("Empty class has no own instance methods (beyond built-in)", [
                    o.create_var_scope([
                        o.create_class_at("Empty", []),
                        tr.assert_text_not_in_value("render", o.property_names_of_class("instance method", "Empty")),
                        tr.assert_text_not_in_value("create", o.property_names_of_class("static method", "Empty")),
                        tr.assert_text_not_in_value("version", o.property_names_of_class("class variable", "Empty")),
                    ]),
                ]),
                tr.test_scope("Subclass without own methods still sees inherited methods", [
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
                        tr.test_scope("Inherited instance method visible on child", [
                            tr.assert_text_in_value("inherited", o.property_names_of_class("instance method", "ChildNoMethods")),
                        ]),
                        tr.test_scope("Inherited static method visible on child", [
                            tr.assert_text_in_value("parentStatic", o.property_names_of_class("static method", "ChildNoMethods")),
                        ]),
                        tr.test_scope("Parent's own methods also still visible on parent", [
                            tr.assert_text_in_value("inherited", o.property_names_of_class("instance method", "Parent")),
                        ]),
                    ]),
                ]),
                tr.test_scope("Overriding a method replaces it, not duplicates it", [
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
                        tr.test_scope("greet appears in child's instance methods", [
                            tr.assert_text_in_value("greet", o.property_names_of_class("instance method", "Child2")),
                        ]),
                        tr.test_scope("Override is active — child instance calls child version", [
                            o.set_scope_var("c", o.create_instance("Child2", '[]')),
                            tr.assert_unstrict_equal(
                                o.call_method(o.get_scope_var("c"), "greet", '[]'),
                                "child-greet",
                            ),
                        ]),
                    ]),
                ]),
            ]),

            tr.test_scope("getAllAttributes", [
                o.create_var_scope([
                    o.create_class_at("Data", []),
                    o.set_scope_var("d", o.create_instance("Data", '[]')),
                    o.set_attribute(o.get_scope_var("d"), "x", "1"),
                    o.set_attribute(o.get_scope_var("d"), "y", "2"),
                    tr.test_scope("getAllAttributes includes all set attributes", [
                        tr.assert_text_in_value("x", o.get_all_attributes(o.get_scope_var("d"))),
                        tr.assert_text_in_value("y", o.get_all_attributes(o.get_scope_var("d"))),
                        tr.assert_text_in_value("1", o.get_all_attributes(o.get_scope_var("d"))),
                        tr.assert_text_in_value("2", o.get_all_attributes(o.get_scope_var("d"))),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("propertyNamesOfClass: special method dropdown", [
                o.create_var_scope([
                    o.create_class_at("Nameable", [
                        o.define_special_method("init", []),
                        o.define_special_method("as string", [
                            o.return_value("nameable"),
                        ]),
                        o.define_operator_method("left add", [
                            o.return_value(h.operator.join("L+", o.operator_operator_value())),
                        ]),
                        o.define_operator_method("not equals", [
                            o.return_value(h.operator.true_boolean()),
                        ]),
                    ]),
                    tr.test_scope("init appears as 'init' in special method list", [
                        tr.assert_text_in_value("init", o.property_names_of_class("special method", "Nameable")),
                    ]),
                    tr.test_scope("as string appears as 'as string' in special method list", [
                        tr.assert_text_in_value("as string", o.property_names_of_class("special method", "Nameable")),
                    ]),
                    tr.test_scope("Special methods do NOT appear in instance method list", [
                        tr.assert_text_not_in_value("init", o.property_names_of_class("instance method", "Nameable")),
                        tr.assert_text_not_in_value("as string", o.property_names_of_class("instance method", "Nameable")),
                    ]),
                    tr.test_scope("Operator methods appear as public names in operator method list", [
                        tr.assert_text_in_value("left add", o.property_names_of_class("operator method", "Nameable")),
                        tr.assert_text_in_value("not equals", o.property_names_of_class("operator method", "Nameable")),
                    ]),
                    tr.test_scope("Operator methods do NOT appear in instance or special method list", [
                        tr.assert_text_not_in_value("left add", o.property_names_of_class("instance method", "Nameable")),
                        tr.assert_text_not_in_value("left add", o.property_names_of_class("special method", "Nameable")),
                    ]),
                ]),
            ]),

            # ------------------------------------------------------------------ #
            tr.test_scope("propertyNamesOfClass: special method inheritance", [
                o.create_var_scope([
                    tr.test_scope("Empty class always has init from common superclass", [
                        o.create_class_at("BareClass", []),
                        tr.assert_text_in_value("init", o.property_names_of_class("special method", "BareClass")),
                    ]),
                    tr.test_scope("Class with only as string still inherits init", [
                        o.create_class_at("AsStringOnly", [
                            o.define_special_method("as string", [
                                o.return_value("str"),
                            ]),
                        ]),
                        tr.assert_text_in_value("init", o.property_names_of_class("special method", "AsStringOnly")),
                        tr.assert_text_in_value("as string", o.property_names_of_class("special method", "AsStringOnly")),
                    ]),
                    tr.test_scope("Subclass inherits special methods from parent", [
                        o.create_class_at("SpBase", [
                            o.define_special_method("as string", [
                                o.return_value("base"),
                            ]),
                        ]),
                        o.create_subclass_at("SpChild", "SpBase", []),
                        tr.assert_text_in_value("as string", o.property_names_of_class("special method", "SpChild")),
                        tr.assert_text_in_value("init", o.property_names_of_class("special method", "SpChild")),
                    ]),
                    tr.test_scope("Subclass overriding as string replaces, not duplicates", [
                        o.create_class_at("SpBase2", [
                            o.define_special_method("as string", [
                                o.return_value("base2"),
                            ]),
                        ]),
                        o.create_subclass_at("SpChild2", "SpBase2", [
                            o.define_special_method("as string", [
                                o.return_value("child2"),
                            ]),
                        ]),
                        tr.assert_text_in_value("as string", o.property_names_of_class("special method", "SpChild2")),
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
    
    projects.append((test_TypeChecker(), test_projects_dir / "test_TypeChecker.pmp"))
    projects.append((test_Cast(), test_projects_dir / "test_Cast.pmp"))
    projects.append((test_scoped_variables(), test_projects_dir / "test_scoped_variables.pmp"))
    projects.append((test_functions(), test_projects_dir / "test_functions.pmp"))
    projects.append((test_utilities(), test_projects_dir / "test_utilities.pmp"))
    projects.append((test_class_definitions(), test_projects_dir / "test_class_definitions.pmp"))
    projects.append((test_instance_methods(), test_projects_dir / "test_instance_methods.pmp"))
    projects.append((test_special_method_init(), test_projects_dir / "test_special_method_init.pmp"))
    projects.append((test_inheritance_and_super(), test_projects_dir / "test_inheritance_and_super.pmp"))
    projects.append((test_getters_and_setters(), test_projects_dir / "test_getters_and_setters.pmp"))
    projects.append((test_operator_methods(), test_projects_dir / "test_operator_methods.pmp"))
    projects.append((test_static_methods(), test_projects_dir / "test_static_methods.pmp"))
    projects.append((test_class_variables(), test_projects_dir / "test_class_variables.pmp"))
    projects.append((test_introspection(), test_projects_dir / "test_introspection.pmp"))

    for project, path in projects:
        write_project_to_file(project, path)
    
    united_project = TestProject.join_projects([p for p, _ in projects])
    write_project_to_file(united_project, test_projects_dir / "test_united.pmp")

if __name__ == "__main__":
    main()
