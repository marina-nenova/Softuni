from abc import ABC, abstractmethod

from project.core.Validator.validator import Validator


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty(value, "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    @abstractmethod
    def add_fish(self, fish):
        pass

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fishes = "none" if not self.fish else ' '.join([fish.name for fish in self.fish])

        output = f"{self.name}:\n"
        output += f"Fish: {fishes}\n"
        output += f"Decorations: {len(self.decorations)}\n"
        output += f"Comfort: {self.calculate_comfort()}\n"

        return output
