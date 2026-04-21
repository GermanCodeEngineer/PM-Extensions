from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import copy
import pmp_manip as p
from pmp_manip.opcode_info.api import OpcodeInfoAPI
from gceutils import AbstractTreePath

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
                t.assert_(o.typeof_value_is_menu(o.create_instance(o.create_class_named("MyClass", []), h.jwArray.blank()), "Class Instance (GCE)")),
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
            t.test_scope("Foreign", [
                t.assert_type(o.all_variables("all scopes"), "Array (jwklong)"),
    
            ])
        ])
    )
    
    return create_test_project(scripts=[script], extension_ids=[
        "gceOOP", "gceFuncsScopes", "gceTestRunner", "jwProto",
    ])

def main() -> None:
    configure()
    test_projects_dir = Path("test_projects")
    write_project_to_file(test_TypeChecker(), test_projects_dir / "test_TypeChecker.pmp")
    write_project_to_file(test_Cast(), test_projects_dir / "test_Cast.pmp")

if __name__ == "__main__":
    main()
