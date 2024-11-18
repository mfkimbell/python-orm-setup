# python-orm-setup

uses Pyscopg2 and SQLAlchemy

```
my_project/
├── app/
│   ├── __init__.py        # App initialization
│   ├── db.py              # Database setup
│   ├── models.py          # SQLAlchemy models
│   ├── crud.py            # CRUD operations
│   ├── config.py          # Configuration (DB URL, etc.)
│   └── tests/             # Unit tests
└── main.py                # Entry point for application
```

```
my_project/
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   ├── crud.py
│   ├── config.py
│   └── tests/
│       ├── test_models.py
│       └── test_crud.py
├── main.py
├── pyproject.toml         # PDM configuration
├── pdm.lock               # PDM lockfile
└── requirements.txt       # Exported dependencies (optional)
```
