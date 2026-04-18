from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import copy
import pmp_manip as p
from gceutils import AbstractTreePath

from helpers.event import event
from helpers.gceFuncsScopes import gceFuncsScopes as fs
from helpers.gceOOP import gceOOP as c
from helpers.gceTestRunner import gceTestRunner as t


EXTENSION_URL_BASE = (
    #"https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/"
    #"refs/heads/main/extensions"
    "http://localhost:5173/extensions"
)

def own_extension_url(filename: str) -> str:
    return f"{EXTENSION_URL_BASE}/{filename}"

GCE_EXTENSIONS = [
    p.SRCustomExtension(
        id="gceOOP",
            url=own_extension_url("gceOOP.js"),
    ),
    p.SRCustomExtension(
        id="gceFuncsScopes",
        url=own_extension_url("gceFuncsScopes.js"),
    ),
    p.SRCustomExtension(
        id="gceTestRunner",
        url=own_extension_url("gceTestRunner.js"),
    ),
]


def describe_suite(name: str, *tests: p.SRBlock) -> p.SRBlock:
    return t.test_scope(name, list(tests))


def run_case(name: str, *blocks: p.SRBlock) -> p.SRBlock:
    return t.test_scope(name, list(blocks))

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

def create_test_project(extensions: list[p.SRCustomExtension|p.SRBuiltinExtension], scripts: list[p.SRScript], output_file: Path) -> None:
    cfg = p.get_default_config()
    handler = (
        lambda url: url.startswith(EXTENSION_URL_BASE)
    )
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    p.init_config(cfg)

    project = p.SRProject.create_empty()
    project.stage.scripts = scripts
    project.extensions = extensions

    project.add_all_extensions_to_info_api(p.info_api)

    # Tricks to avoid errors for invalid extension URLs (currently too strict)
    extensions_before = copy.deepcopy(project.extensions)
    for extension in project.extensions:
        extension.url = "https://example.com/"

    project.validate(AbstractTreePath(), p.info_api)
    project.extensions = extensions_before

    frproject = project.to_first(p.info_api)
    frproject.to_file(str(output_file))

def test_TypeChecker() -> None:
    script = create_script(
        event.whenflagclicked(),
    )
    extensions = [*GCE_EXTENSIONS]
    create_test_project(extensions, [script], Path("test_TypeChecker.pmp"))

def main() -> None:
    test_TypeChecker()

if __name__ == "__main__":
    main()
