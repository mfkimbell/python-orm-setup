# create_db.py
from db import engine, Base
from models.movies import Movie  # Import all models here

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
