# python-orm-setup

uses Pyscopg2 and SQLAlchemy

```
project_root/
├── crud/
│   └── movies.py       # CRUD operations for the "movies" table
├── models/
│   └── __init__.py     # Base and engine setup
│   └── movies.py       # Movies table definition
├── db.py               # Database session management
├── main.py             # Entry point to demonstrate the functionality
├── pyproject.toml      # PDM project file
```