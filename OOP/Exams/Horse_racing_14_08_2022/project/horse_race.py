from project.core.validator.validator import Validator


class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validator.raise_if_race_type_not_valid(value, "Race type does not exist!")
        self.__race_type = value
