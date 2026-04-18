from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import copy
import pmp_manip as p
from gceutils import AbstractTreePath

p.init_config(p.get_default_config())

def print_fr(path: Path) -> None:
    frproject = p.FRProject.from_file(str(path))
    print(100*"=")
    print(frproject)

def main() -> None:
    test_projects_dir = Path("test_projects")
    print_fr(test_projects_dir / "test_TypeChecker.pmp")
    print_fr(test_projects_dir / "from_editor.pmp")

if __name__ == "__main__":
    main()
