from project.aquarium.base_aquarium import BaseAquarium
from project.fish.saltwater_fish import SaltwaterFish


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 25)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        if isinstance(fish, SaltwaterFish):
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        else:
            return "Water not suitable."
