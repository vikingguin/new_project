<!--    new_project = Projektname
        Python = Porgrammiersprache
        awetzel = Author
        Erstellung neuer Projekte mit Templat-Struktur. Verfügbar sind: Python (PowerShell, C/C++ noch nicht implementiert!) = Projektbeschreibung
        0.1.0 = Version
-->

# Python-Projekt
## new_project - ein moderner Projektgenerator für Python

## Projektdetails

- Projektname: new_project
- Porgrammiersprache: Python
- Author: awetzel
- Version: 0.1.0

## Projektstruktur

```None
new_project/
├── src/                  
│   └── new_project/           
│       ├── \_\_init\_\_.py
│       ├── app.py        
│       ├── resources/
│       ├── models/
│       │   └── \_\_init\_\_.py
│       ├── utils/        
│       │   └── \_\_init\_\_.py
│       └── services/     
│           └── \_\_init\_\_.py           
├── scripts/              
├── testing/               
├── logs/                 
├── new_project-venv/ 
├── .git/          
├── pyproject.toml      
├── .gitignore
└── README.md
```

## Beschreibung
Das Projekt ist ein leichtgewichtiges, aber leistungsstarkes CLI‑Tool, das automatisch eine komplette, professionelle Python‑Projektstruktur erzeugt.
Es nimmt dir die repetitive Setup‑Arbeit ab und erstellt ein sofort nutzbares Grundgerüst inklusive:

- Projektordner
- src/‑Layout
- Templates für README, App‑Starter und .gitignore
- Virtual Environment
- Git‑Initialisierung
- saubere Paketstruktur
- pyproject.toml

Ideal für alle, die regelmäßig neue Python‑Projekte starten und dabei Zeit sparen möchten.

## 🚀 Features
### ✔ Automatische Projektstruktur
new_project erzeugt ein modernes, sauberes src/‑Layout:

```None
new_project/
├── src/                  
│   └── new_project/           
│       ├── \_\_init\_\_.py
│       ├── app.py        
│       ├── resources/
│       ├── models/
│       │   └── \_\_init\_\_.py
│       ├── utils/        
│       │   └── \_\_init\_\_.py
│       └── services/     
│           └── \_\_init\_\_.py           
├── scripts/              
├── testing/               
├── logs/                 
├── new_project-venv/ 
├── .git/          
├── pyproject.toml      
├── .gitignore
└── README.md
```

### ✔ Template‑basierte Dateigenerierung
Alle wichtigen Dateien werden aus Templates erzeugt:

- README.md
- app.py
- .gitignore
- pypjrojec.toml
- \_\_init\_\_.py

Platzhalter wie $1, $2, $3 werden automatisch ersetzt.

### ✔ Eingebaute Virtualenv‑Erstellung
mk_pyp erzeugt ein isoliertes Virtualenv direkt im Projekt:

```None
myproject-venv/
```

✔ Git‑Initialisierung
Optional wird automatisch ein Git‑Repository erstellt:

```None
git init
```

#### ✔ Ressourcen sicher eingebettet
Templates werden über importlib.resources geladen — zuverlässig, egal ob lokal oder installiert.

### ✔ CLI‑Tool
Nach Installation steht der Befehl:

```None
new_project
```

systemweit zur Verfügung.

## 🛠 Installation
### 1. Repository klonen

```None
git clone <repo-url>
cd new_project
```

## 2. Installation im aktuellen System / venv

```None
pip install .
```

Danach steht der Befehl mk_pyp zur Verfügung.

## 🧩 Verwendung
Starte einfach:

```None
mk_pyp
```

Das Tool fragt dich interaktiv nach:

- Projektname
- Programmiersprache
- Autor
- Beschreibung
- Version

Anschließend wird das komplette Projektgerüst erzeugt.

## 🧠 Technische Details

- Python-Version: ≥ 3.11
- Build-System: setuptools
- CLI‑Entry‑Point: mk_pyp = "mk_pyp.app:main"
- Templates: eingebettet unter mk_pyp/resources/
- Import‑Struktur: saubere relative Imports
- Ressourcen‑Laden: importlib.resources.files("mk_pyp.resources")

## 🤝 Mitwirken
Pull Requests, Issues und Vorschläge sind willkommen.
Das Projekt ist bewusst modular aufgebaut, sodass neue Templates, Features oder Strukturen leicht ergänzt werden können.

## 📄 Lizenz
MIT License – frei nutzbar für private und kommerzielle Projekte.
