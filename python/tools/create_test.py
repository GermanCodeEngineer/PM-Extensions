from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import copy
import pmp_manip as p
from gceutils import AbstractTreePath

from helpers.operator import operator
from helpers.event import event
from helpers.operator import operator
from helpers.gceFuncsScopes import gceFuncsScopes
from helpers.gceOOP import gceOOP
from helpers.gceTestRunner import gceTestRunner as t
from helpers.jwArray import jwArray as array
from helpers.jwProto import jwProto as labels
from helpers.SPjavascriptV2 import SPjavascriptV2
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

GCE_EXTENSIONS = {
    "gceOOP": own_extension_url("gceOOP.js"),
    "gceFuncsScopes": own_extension_url("gceFuncsScopes.js"),
    "gceTestRunner": own_extension_url("gceTestRunner.js"),
}



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

def create_test_project(extensions: dict[str, str | None], scripts: list[p.SRScript], output_file: Path) -> None:
    cfg = p.get_default_config()
    handler = (
        lambda url: url.startswith(EXTENSION_URL_BASE)
    )
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    p.init_config(cfg)

    project = p.SRProject.create_empty()
    project.stage.scripts = scripts
    project.extensions = [
        p.SRCustomExtension(id, url) if url is not None else p.SRBuiltinExtension(id=id)
        for id, url in extensions.items()
    ]

    project.add_all_extensions_to_info_api(p.info_api)

    # Tricks to avoid errors for invalid extension URLs (currently too strict)
    extensions_before = copy.deepcopy(project.extensions)
    for extension in project.extensions:
        extension.url = "https://example.com/"

    project.validate(AbstractTreePath(), p.info_api)
    project.extensions = extensions_before

    frproject = project.to_first(p.info_api)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    frproject.to_file(str(output_file))

def test_TypeChecker(output_path: Path) -> None:
    script = create_script(
        event.whenflagclicked(),
        t.test_scope("TypeChecker", [
            labels.label_command("My Types"),
            t.assert_(o.typeof_value_is_menu(o.create_function_named("myFn", []), "Function (GCE)")),
            labels.label_command("Methods can not be accessed from a reporter"),
            t.assert_(o.typeof_value_is_menu(o.create_class_named("MyClass", []), "Class (GCE)")),
            t.assert_(o.typeof_value_is_menu(o.create_instance(o.create_class_named("MyClass", []), array.blank()), "Class Instance (GCE)")),
            t.assert_(o.typeof_value_is_menu(o.nothing(), "Nothing (GCE)")),
            labels.label_command("Common/Safe JS data types"),
            t.assert_(o.typeof_value_is_menu(SPjavascriptV2.js_reporter("undefined"), "JavaScript Undefined")),
            t.assert_(o.typeof_value_is_menu(SPjavascriptV2.js_reporter("null"), "JavaScript Null")),
            t.assert_(o.typeof_value_is_menu(operator.true_boolean(), "Boolean")),
            t.assert_(o.typeof_value_is_menu("777", "Number")),
            t.assert_(o.typeof_value_is_menu("hello", "String")),
            labels.label_command("Custom Extension Types"),
            t.assert_(o.typeof_value_is_menu(h.agBuffer.new_buffer("0"), "Buffer (AndrewGaming587)")),
        ])
    )
    extensions = GCE_EXTENSIONS | {
        "agBuffer": "https://extensions.penguinmod.com/extensions/AndrewGaming587/agBuffer.js",
        # agBuffer: vm.agBuffer.Type
        # agBufferPointer: vm.agBuffer.PointerType
        "ddeDateFormat": "https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormat.js",
        "ddeDateFormatV2": "https://extensions.penguinmod.com/extensions/ddededodediamante/dateFormatV2.js",
        "divEffect": "https://extensions.penguinmod.com/extensions/Div/divAlgEffects.js",
        # divEffect: vm.divAlgEffects.Effect
        "divIterator": "https://extensions.penguinmod.com/extensions/Div/divIterators.js",
        # divIterator: vm.divIterator.Type
        "dogeiscutObject": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutObject.js",
        "dogeiscutRegularExpression": "https://extensions.penguinmod.com/extensions/DogeisCut/dogeiscutRegularExpressions.js",
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


        "jwProto": None,
        "SPjavascriptV2": None,
    }
    create_test_project(extensions, [script], output_path)

def main() -> None:
    test_projects_dir = Path("test_projects")
    test_TypeChecker(test_projects_dir / "test_TypeChecker.pmp")

if __name__ == "__main__":
    main()
