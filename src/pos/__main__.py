from db import get_db
from create_db import init_db
from crud.movies import (
    create_movie,
    get_movies,
    get_movie_by_id,
    update_movie,
    delete_movie,
)

def main():
    # Get the database session generator
    init_db()
    db_gen = get_db()
    db = next(db_gen)

    try:
        # Create a movie
        new_movie = create_movie(
            db, title="The Godfather", director="Francis Ford Coppola", year=1972
        )
        print(
            "Created Movie:",
            {
                "id": new_movie.id,
                "title": new_movie.title,
                "director": new_movie.director,
                "year": new_movie.year,
            },
        )

        # Retrieve all movies
        movies = get_movies(db)
        print(
            "\n  All Movies:",
            [
                {
                    "id": movie.id,
                    "title": movie.title,
                    "director": movie.director,
                    "year": movie.year,
                }
                for movie in movies
            ],
        )

        # Retrieve a movie by ID
        movie = get_movie_by_id(db, movie_id=new_movie.id)
        if movie:
            print(
                "Retrieved Movie:",
                {
                    "id": movie.id,
                    "title": movie.title,
                    "director": movie.director,
                    "year": movie.year,
                },
            )
        else:
            print(f"Movie with ID {new_movie.id} not found.")

        # Update the movie
        updated_movie = update_movie(
            db,
            movie_id=new_movie.id,
            title="The Godfather Part II",
            director="Francis Ford Coppola",
            year=1974,
        )
        if updated_movie:
            print(
                "Updated Movie:",
                {
                    "id": updated_movie.id,
                    "title": updated_movie.title,
                    "director": updated_movie.director,
                    "year": updated_movie.year,
                },
            )
        else:
            print("Failed to update: Movie not found.")

        # # Delete the movie
        # if updated_movie:
        #     deleted_movie = delete_movie(db, movie_id=updated_movie.id)
        #     if deleted_movie:
        #         print(
        #             "Deleted Movie:",
        #             {"id": deleted_movie.id, "title": deleted_movie.title},
        #         )
        #     else:
        #         print(f"Failed to delete movie with ID {updated_movie.id}.")
        # else:
        #     print("Cannot delete: Updated movie is None.")
    finally:
        db_gen.close()


if __name__ == "__main__":
    main()
