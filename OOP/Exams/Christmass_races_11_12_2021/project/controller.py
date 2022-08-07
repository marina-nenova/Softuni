from project.core.factory.car_factory import CarFactory
from project.core.factory.driver_factory import DriverFactory
from project.core.factory.race_factory import RaceFactory
from project.core.validator.validator import Validator


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if Validator.check_if_valid_car_type(car_type):
            Validator.raise_if_car_model_exists(self.cars, model, f"Car {model} is already created!")
            car = CarFactory.create_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        Validator.raise_if_driver_name_exists(self.drivers, driver_name, f"Driver {driver_name} is already created!")

        driver = DriverFactory.create_driver(driver_name)
        self.drivers.append(driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        Validator.raise_if_race_name_exists(self.races, race_name, f"Race {race_name} is already created!")

        race = RaceFactory.create_race(race_name)
        self.races.append(race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = Validator.find_driver_by_name(self.drivers, driver_name, f"Driver {driver_name} could not be found!")
        car = Validator.find_available_car(self.cars, car_type, f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False
            car.is_taken = True
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model} to {driver.car.model}."

        car.is_taken = True
        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = Validator.find_race_by_name(self.races, race_name, f"Race {race_name} could not be found!")
        driver = Validator.find_driver_by_name(self.drivers, driver_name, f"Driver {driver_name} could not be found!")

        Validator.raise_if_driver_doesnt_have_a_car(driver, f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = Validator.find_race_by_name(self.races, race_name, f"Race {race_name} could not be found!")

        Validator.raise_if_not_enough_drivers_in_race(
            race,
            3,
            f"Race {race_name} cannot start with less than 3 participants!"
        )

        racers = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        output = ""

        for driver in racers[:3]:
            driver.number_of_wins += 1
            output += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"

        return output.strip()
