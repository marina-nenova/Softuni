from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumFactory:
    aquarium_types = {
        "FreshwaterAquarium": FreshwaterAquarium,
        "SaltwaterAquarium": SaltwaterAquarium
    }

    @staticmethod
    def create_aquarium(aquarium_type: str, aquarium_name: str):
        return AquariumFactory.aquarium_types[aquarium_type](aquarium_name)
