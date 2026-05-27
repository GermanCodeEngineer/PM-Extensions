from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import pmp_manip as p
from pmp_manip.opcode_info.api import OpcodeInfoAPI
import third


EXTENSION_URL_BASE = (
    #"https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/"
    #"refs/heads/main/extensions"
    "http://localhost:5173/extensions"
)

def configure() -> None:
    cfg = p.get_default_config()
    handler = (
        lambda url: url.startswith(EXTENSION_URL_BASE)
    )
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    p.init_config(cfg)
    
def convert_project(frproject: p.FRProject) -> third.ThirdProject:
    # Prepare
    opcode_info_copy = p.info_api.opcode_info.copy()
    info_api_copy = OpcodeInfoAPI(opcode_info_copy)
    frproject.add_all_extensions_to_info_api(info_api_copy)

    # Convert FR to SR
    srproject = frproject.to_second(info_api_copy)

    # Convert SR to Third
    import helpers # Important: Register subclasses of ThirdBlock before converting to Third
    trproject = third.ThirdProject.from_second(srproject)
    return trproject

def load_project_from_file(input_file: Path) -> third.ThirdProject:
    frproject = p.FRProject.from_file(str(input_file))
    trproject = convert_project(frproject)
    return trproject

def main() -> None:
    configure()
    test_projects_dir = Path("test_projects")
    trproject = load_project_from_file(test_projects_dir / "test_united.pmp")
    (test_projects_dir.parent / "python" / "output" / "test_united.py").write_text(third.third_repr(trproject))

if __name__ == "__main__":
    main()
