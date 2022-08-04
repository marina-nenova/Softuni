from abc import ABC, abstractmethod

from project.core.validator.validator import Validator


class Movie(ABC):
    MIN_AGE = 0

    @abstractmethod
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "The title cannot be empty string!")
        self.__title = value
        
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        Validator.raise_if_value_is_less_than_min_value(value, 1888, "Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        Validator.raise_if_object_not_correct_type(value, "User", "The owner must be an object of type User!")
        self.__owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.raise_if_value_is_less_than_min_value(
            value,
            self.MIN_AGE,
            f"{self.__class__.__name__} movies must be restricted for audience under {self.MIN_AGE} years!"
        )
        self.__age_restriction = value

    def details(self):
        return f"{self.__class__.__name__} - Title:{self.title}," \
               f" Year:{self.year}," \
               f" Age restriction:{self.age_restriction}," \
               f" Likes:{self.likes}," \
               f" Owned by:{self.owner.username}"
