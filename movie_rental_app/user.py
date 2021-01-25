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

    def delete_movie(self):
        pass

    def watched_movies(self):
        pass

    def save_to_file(self):
        pass

    @classmethod
    def read_from_file(cls, filename):
        pass
