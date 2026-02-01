from pathlib import Path
from typing import Dict
from importlib.resources import files


def load_resource(name: str) -> str:
    """Lädt eine Template-Datei aus new_project/resources."""
    return files("new_project.resources").joinpath(name).read_text(encoding="utf-8")


def replace_placeholders(content: str, replacements: Dict[str, str]) -> str:
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    return content


def edit_readme(facts: Dict[str, str], readme: Path) -> None:
    content = load_resource("readme.txt")

    replacements = {
        "$1": facts["projectname"],
        "$2": facts["language"],
        "$3": facts["author"],
        "$4": facts["description"],
        "$5": facts["version"],
    }

    new_content = replace_placeholders(content, replacements)

    readme.parent.mkdir(parents=True, exist_ok=True)
    readme.write_text(new_content, encoding="utf-8")


def edit_app(file: Path) -> None:
    content = load_resource("app.txt")

    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content, encoding="utf-8")


def edit_gitignore(file: Path, projectname: str) -> None:
    content = load_resource("gitignore.txt")

    new_content = content.replace("$1", projectname)

    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(new_content, encoding="utf-8")

def edit_pyproject(file: Path, projectname: str, version: str, desc: str, author: str, ) -> None:
    content = load_resource("pyproject.txt")

    new_content = content.replace("$1", projectname).replace("$2", version).replace("$3", desc).replace("$4", author)

    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(new_content, encoding="utf-8")
