from models.movie_model import MovieModel


class MovieService:
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        return self.db.query(MovieModel).all()

    def get_movie(self, id: int):
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()