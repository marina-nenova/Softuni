from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:
    valid_car_types = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    @staticmethod
    def create_car(car_type, model, speed_limit):
        return CarFactory.valid_car_types[car_type](model, speed_limit)
