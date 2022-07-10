from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def test_vehicle_fuel_initialized_correctly_with_integer_value(self):
        car = Vehicle(40, 120)
        self.assertEqual(40, car.fuel)

    def test_vehicle_fuel_initialized_correctly_with_float_value(self):
        car = Vehicle(40.5, 120)
        self.assertEqual(40.5, car.fuel)

    def test_vehicle_fuel_capacity_initialized_correctly_with_integer_value(self):
        car = Vehicle(40, 120)
        self.assertEqual(40, car.capacity)

    def test_vehicle_fuel_capacity_initialized_correctly_with_float_value(self):
        car = Vehicle(40.5, 120)
        self.assertEqual(40.5, car.capacity)

    def test_vehicle_horse_power_initialized_correctly_with_integer_value(self):
        car = Vehicle(40, 120)
        self.assertEqual(120, car.horse_power)

    def test_vehicle_horse_power_initialized_correctly_with_float_value(self):
        car = Vehicle(40.5, 120.5)
        self.assertEqual(120.5, car.horse_power)

    def test_vehicle_fuel_consumption_initialized_correctly_with_default_value(self):
        car = Vehicle(40.5, 120.5)
        self.assertEqual(1.25, car.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, car.fuel_consumption)

    def test_drive_vehicle_with_enough_fuel_fuel_amount_decremented(self):
        car = Vehicle(40, 120)
        car.drive(20)
        self.assertEqual(15 ,car.fuel)

        car.drive(10)
        self.assertEqual(2.5, car.fuel)

    def test_drive_vehicle_with_not_enough_fuel_raises(self):
        car = Vehicle(40, 120)

        with self.assertRaises(Exception) as ex:
            car.drive(40)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_vehicle_with_fuel_less_than_capacity(self):
        car = Vehicle(40, 120)
        car.drive(20)
        self.assertEqual(40, car.capacity)
        self.assertEqual(15, car.fuel)

        car.refuel(15)
        self.assertEqual(30, car.fuel)

        car.refuel(5)
        self.assertEqual(35, car.fuel)

    def test_refuel_vehicle_with_fuel_more_than_capacity_raises(self):
        car = Vehicle(40, 120)
        car.drive(20)
        self.assertEqual(40, car.capacity)
        self.assertEqual(15, car.fuel)

        with self.assertRaises(Exception) as ex:
            car.refuel(30)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_string_representation_returns_correctly(self):
        car = Vehicle(40, 120)
        result = str(car)
        self.assertEqual("The vehicle has 120 horse power with 40 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    main()