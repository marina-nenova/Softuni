from project.core.factory.user_factory import UserFactory
from project.core.validator.validator import Validator
from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        Validator.raise_if_username_exists(self.users_collection, username, "User already exists!")
        user = UserFactory.create_user(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def __find_user_by_username(self, username):
        return [user for user in self.users_collection if user.username == username][0]

    def upload_movie(self, username: str, movie: Movie):
        Validator.raise_if_username_doesnt_exist(self.users_collection, username, "This user does not exist!")
        Validator.raise_if_username_is_not_movie_owner(
            movie,
            username,
            f"{username} is not the owner of the movie {movie.title}!"
        )
        Validator.raise_if_movie_already_in_collection(
            self.movies_collection,
            movie,
            "Movie already added to the collection!"
        )

        user = self.__find_user_by_username(username)
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        Validator.raise_if_movie_not_in_collection(
            self.movies_collection, movie,
            f"The movie {movie.title} is not uploaded!"
        )
        Validator.raise_if_username_is_not_movie_owner(
            movie,
            username,
            f"{username} is not the owner of the movie {movie.title}!"
        )

        for attribute, new_value in kwargs.items():
            setattr(movie, attribute, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        Validator.raise_if_movie_not_in_collection(
            self.movies_collection,
            movie,
            f"The movie {movie.title} is not uploaded!"
        )
        Validator.raise_if_username_is_not_movie_owner(
            movie,
            username,
            f"{username} is not the owner of the movie {movie.title}!"
        )

        user = self.__find_user_by_username(username)
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)

        Validator.raise_if_username_is_movie_owner(
            movie,
            username,
            f"{username} is the owner of the movie {movie.title}!"
        )
        Validator.raise_if_movie_already_liked_by_user(
            user,
            movie,
            f"{username} already liked the movie {movie.title}!"
        )

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        Validator.raise_if_movie_not_liked_by_user(user, movie, f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        if not self.movies_collection:
            return "No movies found."

        output = ""
        for movie in sorted_movies:
            output += movie.details() + "\n"

        return output.strip()

    def __str__(self):
        output = "All users: "
        if not self.users_collection:
            output += "No users.\n"
        else:
            output += ', '.join([user.username for user in self.users_collection]) + '\n'

        output += "All movies: "
        if not self.movies_collection:
            output += "No movies.\n"
        else:
            output += ', '.join([movie.title for movie in self.movies_collection])

        return output.strip()
