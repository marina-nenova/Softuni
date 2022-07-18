
class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_less_than_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_object_not_correct_type(value, object_type, message):
        if not value.__class__.__name__ == object_type:
            raise ValueError(message)

    @staticmethod
    def raise_if_username_exists(users_collection, username, message):
        if any([user.username == username for user in users_collection]):
            raise Exception(message)

    @staticmethod
    def raise_if_username_doesnt_exist(users_collection, username, message):
        if not any([user.username == username for user in users_collection]):
            raise Exception(message)

    @staticmethod
    def raise_if_username_is_not_movie_owner(movie, username, message):
        if not movie.owner.username == username:
            raise Exception(message)

    @staticmethod
    def raise_if_username_is_movie_owner(movie, username, message):
        if movie.owner.username == username:
            raise Exception(message)

    @staticmethod
    def raise_if_movie_already_liked_by_user(user, movie, message):
        if movie in user.movies_liked:
            raise Exception(message)

    @staticmethod
    def raise_if_movie_not_liked_by_user(user, movie, message):
        if movie not in user.movies_liked:
            raise Exception(message)

    @staticmethod
    def raise_if_movie_already_in_collection(movies_collection, movie, message):
        if movie in movies_collection:
            raise Exception(message)

    @staticmethod
    def raise_if_movie_not_in_collection(movies_collection, movie, message):
        if movie not in movies_collection:
            raise Exception(message)
