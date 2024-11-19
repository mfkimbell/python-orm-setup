# crud/movies.py
from sqlalchemy.orm import Session
from models.movies import Movie


def get_movies(db: Session):
    return db.query(Movie).all()


def get_movie_by_id(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()


def create_movie(db: Session, title: str, director: str, year: int):
    new_movie = Movie(title=title, director=director, year=year)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


# crud/movies.py
def update_movie(db: Session, movie_id: int, title: str, director: str, year: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        return None  # Return None if the movie doesn't exist
    movie.title = title
    movie.director = director
    movie.year = year
    db.commit()
    db.refresh(movie)
    return movie


def delete_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        db.delete(movie)
        db.commit()
    return movie
