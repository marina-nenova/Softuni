from Classes_and_objects.exercise.library.project.library import Library
from Classes_and_objects.exercise.library.project.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if any([existing_user.user_id == user.user_id for existing_user in library.user_records]):
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for existing_user in library.user_records:
            if existing_user.user_id == user_id:
                if existing_user.username == new_username:
                    return "Please check again the provided username - " \
                           "it should be different than the username used so far!"
                else:
                    if existing_user.username in library.rented_books:
                        library.rented_books[new_username] = library.rented_books.pop(existing_user.username)
                    existing_user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {existing_user.user_id}"
        return f"There is no user with id = {user_id}!"
