from abc import ABC, abstractmethod

from project.core.validator.validator import Validator


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_value_is_less_than_min_value(value, 1, "Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        pass
