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

    def save_to_CSV(self):
        with open(f"{self.name}.txt", "w") as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(f"{movie.title}, {movie.genre}, {str(movie.watched)}")

    @classmethod
    def read_from_CSV(cls, filename):
        with open(filename, "r") as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")
                movies.append(
                    Movie(movie_data[0], movie_data[1], movie_data[2] == "True")
                )

        user = cls(username)
        user.movies = movies
        return user

    def json(self):
        return {"name": self.name, "movies": [movie.json() for movie in self.movies]}

    @classmethod
    def read_from_json(cls, json_data):
        user = User(json_data["name"])
        movies = []
        for movie in json_data["movies"]:
            movies.append(Movie(movie["name"], movie["genre"], movie["watched"]))
        user.movies = movies

        return user
