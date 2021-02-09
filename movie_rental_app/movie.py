class Movie:
    def __init__(self, title, genre, watched):
        self.title = title
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return f"{self.title}"

    def json(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "watched": self.watched
        }
