from pathlib import Path
import venv

def create_venv(project_dir: Path, projectname: str) -> None:
    venv_path = project_dir / projectname
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(venv_path)
