import subprocess
from pathlib import Path

def init_git(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True)
    subprocess.run(["git", "add", "."], cwd=path, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=path, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=path, check=True)
