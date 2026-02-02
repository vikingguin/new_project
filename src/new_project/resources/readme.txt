<!--    $1 = Projektname
        $2 = Porgrammiersprache
        $3 = Author
        $4 = Projektbeschreibung
        $5 = Version
-->

# $2-Projekt
# $1 - $4

## Projektdetails

- Projektname: $1
- Porgrammiersprache: $2
- Author: $3
- Version: $5

## Projektstruktur

```None
$1/
├── src/                  
│   └── $1/           
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
