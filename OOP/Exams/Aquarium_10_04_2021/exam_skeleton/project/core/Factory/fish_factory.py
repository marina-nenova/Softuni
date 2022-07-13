from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class FishFactory:
    fish_types = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    @staticmethod
    def create_fish(fish_type, name, species, price):
        return FishFactory.fish_types[fish_type](name, species, price)
