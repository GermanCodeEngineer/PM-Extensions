from __future__ import annotations

import importlib.util
from pathlib import Path
import pmp_manip as p
from pmp_manip.opcode_info.api import OpcodeInfoAPI
import sys
import shutil

PROJECT_SCRIPT_NAME = "project.py"

PYTHON_ROOT = Path(__file__).resolve().parent.parent
if str(PYTHON_ROOT) not in sys.path:
    sys.path.append(str(PYTHON_ROOT))

import third

def configure() -> None:
    cfg = p.get_default_config()
    handler = (
        #lambda url: url.startswith(
        #    "https://raw.githubusercontent.com/GermanCodeEngineer/PM-Extensions/"
        #)
        lambda url: True
    )
    cfg.ext_info_gen.is_trusted_extension_origin_handler = handler
    cfg.ext_info_gen.node_js_exec_timeout = 10.0
    try:
        p.init_config(cfg)
    except p.MANIP_ConfigurationError as error:
        if "has already been initialized" in str(error):
            pass
        else:
            raise

def fr_to_tr_project(frproject: p.FRProject) -> third.ThirdProject:
    opcode_info_copy = p.info_api.opcode_info.copy()
    info_api_copy = OpcodeInfoAPI(opcode_info_copy)
    frproject.add_all_extensions_to_info_api(info_api_copy)

    # Ensure Third block subclasses are available before Third conversion.
    import helpers  # noqa: F401

    srproject = frproject.to_second(info_api_copy)
    return third.ThirdProject.from_second(srproject)


def tr_to_fr_project(trproject: third.ThirdProject) -> p.FRProject:
    srproject = trproject.to_second()
    opcode_info_copy = p.info_api.opcode_info.copy()
    info_api_copy = OpcodeInfoAPI(opcode_info_copy)
    srproject.add_all_extensions_to_info_api(info_api_copy)
    return srproject.to_first(info_api_copy)


def load_tr_project_from_script(script_path: Path) -> third.ThirdProject:
    module_name = f"pm_project_{script_path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, script_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module spec from {script_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    project = getattr(module, "PROJECT", None)
    if not isinstance(project, third.ThirdProject):
        raise ValueError(f"{script_path} must define PROJECT as a third.ThirdProject")
    return project

def unpack_project(packed_file: Path, unpacked_dir: Path) -> None:
    configure()

    frproject = p.FRProject.from_file(str(packed_file))
    trproject = fr_to_tr_project(frproject)

    shutil.rmtree(unpacked_dir, ignore_errors=True)
    unpacked_dir.mkdir(parents=True, exist_ok=True)
    output_script = unpacked_dir / PROJECT_SCRIPT_NAME
    output_script.write_text(third.third_repr(trproject), encoding="utf-8")


def pack_project(packed_file: Path, unpacked_dir: Path) -> None:
    configure()

    script_path = unpacked_dir / PROJECT_SCRIPT_NAME
    if not script_path.exists():
        raise FileNotFoundError(f"Expected {PROJECT_SCRIPT_NAME} in {unpacked_dir}")

    trproject = load_tr_project_from_script(script_path)
    frproject = tr_to_fr_project(trproject)
    frproject.to_file(str(packed_file))

def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Convert PM save files to a better format.")
    parser.add_argument("mode", choices=["pack", "unpack"], help="Operation mode: 'pack' or 'unpack'")
    parser.add_argument("packed_file", help="Path to the packed PM file")
    parser.add_argument("unpacked_dir", help="Path to the unpacked directory")

    args = parser.parse_args()

    if args.mode == "unpack":
        unpack_project(Path(args.packed_file), Path(args.unpacked_dir))
    else:
        pack_project(Path(args.packed_file), Path(args.unpacked_dir))


if __name__ == "__main__":
    main()
