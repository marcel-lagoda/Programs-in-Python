from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f"{self.name}"

    def add_movie(self, genre=None, title=None):
        movie = Movie(title, genre, False)
        self.movies.append(movie)

    def delete_movie(self, title=None):
        self.movies = list(filter(lambda movie: movie.title != title, self.movies))

    def watched_movies(self):
        self.movies = list(filter(lambda movie: movie.watched, self.movies))

    def save_to_file(self):
        pass

    @classmethod
    def read_from_file(cls, filename):
        pass
