from pathlib import Path
import pathlib

def create_s_link(file: Path, linkpath: Path) -> None:
    target = Path(file)
    link = Path(linkpath)

    link.symlink_to(target)
