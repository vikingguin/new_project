import getpass
from pathlib import Path
from new_project.utils.utils import clear_console


def confirm(prompt: str) -> bool:
    """Fragt nach einer Bestätigung (J/n)."""
    answer = input(f"{prompt} [J/n]: ").strip().lower()
    return answer in ("j", "")


def get_path(default_path: Path, language: str) -> Path:
    """Fragt ab, ob der Standardpfad genutzt werden soll oder ein eigener."""
    project_path = default_path / language

    if confirm(f"Standardpfad verwenden: {project_path}?"):
        return project_path

    while True:
        custom = Path(input("Benutzerdefinierter Pfad: ").strip()).expanduser()
        if custom.exists() or confirm("Pfad existiert nicht. Trotzdem verwenden?"):
            return custom


def get_facts() -> dict[str, str]:
    """Fragt alle Projektdaten interaktiv ab und gibt sie als Dictionary zurück."""
    
    user = getpass.getuser()
    default_path = Path(f"/home/{user}/Projekte").expanduser()

    while True:
        clear_console()

        language = "Python" 
        name = input("Projektname: ").strip()
        desc = input("Kurze Projektbeschreibung: ").strip()

        author = user if confirm(f"Author: {user}?") else input("Author: ").strip()
        version = "0.1.0" if confirm('Version "0.1.0" verwenden?') else input("Version: ").strip()

        path = get_path(default_path, language)

        clear_console()
        print(
            f"\nProgrammiersprache: {language}"
            f"\nProjektname: {name}"
            f"\nAuthor: {author}"
            f"\nBeschreibung: {desc}"
            f"\nVersion: {version}"
            f"\nPfad: {path}"
        )

        if confirm("\nAngaben korrekt?"):
            return {
                "projectname": name,
                "author": author,
                "description": desc,
                "language": language,
                "version": version,
                "path": str(path)
            }
