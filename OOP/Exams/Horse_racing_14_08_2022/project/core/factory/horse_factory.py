from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseFactory:
    valid_horse_types = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    @staticmethod
    def create_horse(horse_type: str, horse_name: str, horse_speed: int):
        return HorseFactory.valid_horse_types[horse_type](horse_name, horse_speed)
