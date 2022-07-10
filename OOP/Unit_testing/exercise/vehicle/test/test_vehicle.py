from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self) -> None:
        self.car = Vehicle(40, 120)

    def test_vehicle_init(self):
        car = Vehicle(40, 120)
        self.assertEqual(40, car.fuel)
        self.assertEqual(40, car.capacity)
        self.assertEqual(120, car.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, car.fuel_consumption)

    def test_drive_vehicle_with_enough_fuel_fuel_amount_decremented(self):
        distance = 20
        burned_fuel = distance * self.car.fuel_consumption
        expected = self.car.fuel - burned_fuel
        self.car.drive(distance)
        self.assertEqual(expected, self.car.fuel)

        distance = 10
        burned_fuel = distance * self.car.fuel_consumption
        expected = self.car.fuel - burned_fuel
        self.car.drive(distance)
        self.assertEqual(expected, self.car.fuel)

    def test_drive_vehicle_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(self.car.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_vehicle_with_fuel_less_than_capacity(self):
        self.car.fuel = 20

        self.car.refuel(15)
        self.assertEqual(35, self.car.fuel)

        self.car.refuel(5)
        self.assertEqual(40, self.car.fuel)

    def test_refuel_vehicle_with_fuel_more_than_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(30)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_string_representation_returns_correctly(self):
        result = str(self.car)
        expected = f"The vehicle has {self.car.horse_power} horse power with {self.car.fuel} fuel left and {self.car.fuel_consumption} fuel consumption"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()