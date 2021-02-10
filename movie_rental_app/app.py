from user import User
import json
import os


def menu():
    name = input("Enter your name: ")
    filenames = [f"{name}.csv,", f"{name}.json"]
    if file_exists(filenames):
        with open(file_exists(filenames), "r") as f:
            json_data = json.load(f)
        user = User.read_from_json(json_data)
    else:
        user = User(name)

    selection = input(
        "Select your choice: \n"
        "'a' to add a new movie, \n"
        "'l' to list all movies (watched & unwatched), \n"
        "'n' to list all unwatched movies, \n"
        "'y' to list all watched movies, \n"
        "'d' to delete movie by its title, \n"
        "'w' to set movie as watched, \n"
        "'q' to exit: "
    )

    while selection != "q":
        if selection == "a":
            new_movie = input("Enter movie title: ")
            new_movie_genre = input("Enter movie genre: ")
            user.add_movie(new_movie, new_movie_genre)
        elif selection == "l":
            user.print_all_movies()
        elif selection == "n":
            print(user.unwatched_movies())
        elif selection == "y":
            print(user.watched_movies())
        elif selection == "d":
            to_delete = input("Enter a movie title you want to delete: ")
            if to_delete:
                user.delete_movie(to_delete)
            else:
                print("There is no movie with such title in your database.")
        elif selection == "w":
            watched = input("Enter a movie title you've watched: ")
            user.set_watched(watched)

        selection = input(
            "Select your choice: \n"
            "'a' to add a new movie, \n"
            "'l' to list all movies (watched & unwatched), \n"
            "'n' to list all unwatched movies, \n"
            "'y' to list all watched movies, \n"
            "'d' to delete movie by its title, \n"
            "'w' to set movie as watched, \n"
            "'q' to exit: "
        )


def file_exists(filenames):
    for filename in filenames:
        if filename:
            return os.path.isfile(filename)


if __name__ == "__main__":
    menu()
