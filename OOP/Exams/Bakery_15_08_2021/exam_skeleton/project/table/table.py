from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.core.validator.validator import Validator
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_value_is_zero_or_less(value, "Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total_food_price = sum([food.price for food in self.food_orders])
        total_drink_price = sum([drink.price for drink in self.drink_orders])
        return total_food_price + total_drink_price

    def clear(self):
        self.is_reserved = False
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"
