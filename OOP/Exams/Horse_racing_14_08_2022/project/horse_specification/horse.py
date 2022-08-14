from abc import ABC, abstractmethod

from project.core.validator.validator import Validator


class Horse(ABC):
    MAX_SPEED = 0

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_name_is_less_than_min_symbols(value, 4, f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.raise_if_value_is_bigger_than_max_value(value, self.MAX_SPEED, "Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        pass
