# python-orm-setup

### Overview
A Python project demonstrating the use of modern ORM (Object Relational Mapping) techniques with SQLAlchemy to manage a relational database. The project leverages the repository pattern for clean and maintainable data access logic and includes a CRUD interface for managing movie data in a PostgreSQL database.

### Tools Used
* `PDM` For python package management
* `SQLAlchemy` For object relational mapping to database
* `Postgres` For relational data storage

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

### repository pattern

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

### Running the program

<img width="887" alt="Screenshot 2024-11-21 at 1 03 10 AM" src="https://github.com/user-attachments/assets/41e1e2cb-850c-456e-9be1-d84f1ab91edd">

### Database end state
<img width="497" alt="Screenshot 2024-11-21 at 1 00 19 AM" src="https://github.com/user-attachments/assets/e859f79f-3aa7-4a51-8107-76ff1169bc18">


