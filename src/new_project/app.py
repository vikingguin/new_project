import sys
from typing import Tuple, Dict
from pathlib import Path

from new_project.utils.mk_py_fs import set_py_path, mk_py_fs, mk_py_files
from new_project.utils.get_facts import get_facts
from new_project.utils.edit_files import edit_readme, edit_app, edit_gitignore, edit_pyproject, edit_project_init, edit_activate_script
from new_project.utils.init_venv import create_venv
from new_project.utils.init_git import init_git


def set_vars() -> Tuple[dict, Dict[str, Path], Dict[str, Path], Dict[str, Path]]:
    """Liest die Projektfakten ein und erzeugt die Pfadstrukturen."""

    facts = get_facts()

    if facts.get("language") != "Python":
        print("Derzeit wird nur die Python-Projekterstellung unterstützt.")
        sys.exit(1)

    dirs, files, res_files = set_py_path(
        facts["path"],
        facts["projectname"]
    )

    return facts, dirs, files, res_files


def main() -> None:
    facts, dirs, files, res_files = set_vars()

    # Verzeichnisse und Dateien anlegen
    mk_py_fs(dirs)
    mk_py_files(files)

    # Templates bearbeiten
    edit_readme(facts, files["readme"])
    edit_app(files["app"])
    edit_gitignore(files["gitignore"], facts["projectname"])
    edit_pyproject(files["pyproject"], facts["projectname"], facts["version"], facts["description"], facts["author"])
    edit_project_init(files["project_init"], facts["version"])
    create_venv(Path(dirs["base"]), f"{facts["projectname"]}-venv")
    edit_activate_script(files["activate"], facts["projectname"])
    init_git(dirs["base"])
    



if __name__ == "__main__":
    main()
