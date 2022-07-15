from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.core.validator.validator import Validator


class AstronautFactory:
    valid_astronaut_types = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    @staticmethod
    def create_astronaut(astronaut_type, name):
        Validator.raise_if_astronaut_type_is_not_valid(AstronautFactory.valid_astronaut_types,
                                                       astronaut_type, "Astronaut type is not valid!")
        return AstronautFactory.valid_astronaut_types[astronaut_type](name)
