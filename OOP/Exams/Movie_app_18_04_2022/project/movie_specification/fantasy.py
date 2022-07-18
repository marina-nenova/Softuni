from project.core.validator.validator import Validator
from project.movie_specification.movie import Movie


class Fantasy(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.raise_if_value_is_less_than_min_value(value, 6,
                                                        "Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}," \
               f" Year:{self.year}," \
               f" Age restriction:{self.age_restriction}," \
               f" Likes:{self.likes}," \
               f" Owned by:{self.owner.username}"
