from project.user import User


class UserFactory:
    @staticmethod
    def create_user(username, age):
        return User(username, age)
