from pathlib import Path
from typing import Dict, Tuple


def set_py_path(path: str, projectname: str) -> Tuple[Dict[str, Path], Dict[str, Path], Dict[str, Path]]:
    base = Path(path).expanduser().resolve() / projectname
    src = base / "src"
    code = src / projectname
    current_file = Path(__file__).resolve()
    mk_pyp_dir = current_file.parents[2]
    res_dir = mk_pyp_dir / "resources"
    


    dirs = {
        "base": base,
        "src": src,
        "project": code,
        "utils": code / "utils",
        "models": code / "models",
        "services": code / "services",
        "resources": code / "resources",
        "tests": base / "testing",
        "scripts": base / "scripts",
        "logs": base / "logs",
    }

    files = {
        "gitignore": base / ".gitignore",
        "pyproject": base / "pyproject.toml",
        "readme": base / "README.md",
        "app": base / src / projectname / "app.py",
        "project_init": code / "__init__.py",
        "models_init": code / "models" / "__init__.py",
        "services_init": code / "services" / "__init__.py",
        "utils_init": code / "utils" / "__init__.py",
        "scripts_gitkeep": base / "scripts" / ".gitkeep",
        "testing_gitkeep": base / "testing" / ".gitkeep",
        "resources_gitkeet": code / "resources" / ".gitkeep"
    }

    res_files = {
        "readme": res_dir / "readme.txt",
        "gitignore": res_dir / "gitignore.txt",
        "pyproject": res_dir / "pyproject.txt",
        "app": res_dir / "app.txt"
    }

    return dirs, files, res_files


def mk_py_fs(dirs: Dict[str, Path]) -> None:
    for path in dirs.values():
        path.mkdir(parents=True, exist_ok=True)


def mk_py_files(files: Dict[str, Path]) -> None:
    for path in files.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
