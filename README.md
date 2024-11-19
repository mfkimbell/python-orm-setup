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

## repository pattern

The repository pattern is a design approach to abstract data access logic and provide a clean interface for interacting with the underlying database. In your case, the crud.movies module acts as the repository.

```python
from crud.movies import (
    create_movie,
    get_movies,
    get_movie_by_id,
    update_movie,
    delete_movie,
)
from sqlalchemy.orm import Session


class Movie:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, director: str, year: int):
        new_movie = create_movie(self.db, title=title, director=director, year=year)
        return {
            "id": new_movie.id,
            "title": new_movie.title,
            "director": new_movie.director,
            "year": new_movie.year,
        }

```
We leave the creation logic to the repository `crud.movies` and we can keep business logic in this class (think LLD questions)
