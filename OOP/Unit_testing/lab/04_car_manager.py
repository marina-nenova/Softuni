class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


from unittest import TestCase, main


class CarTests(TestCase):
    def test_make_is_initialized_correctly_with_valid_data(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual("a", car.make)

    def test_make_is_initialized_with_invalid_data_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "b", 1, 4)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_is_initialized_correctly_with_valid_data(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual("b", car.model)

    def test_model_is_initialized_with_invalid_data_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("a", "", 1, 4)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_is_initialized_correctly_with_valid_data(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(1, car.fuel_consumption)

    def test_fuel_consumption_is_initialized_with_zero_or_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", 0, 4)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", -5, 4)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_is_initialized_correctly_with_valid_data(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(4, car.fuel_capacity)

    def test_fuel_capacity_is_initialized_with_zero_or_negative_value_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", 1, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("a", "b", 1, -5)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_is_initialized_correctly(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)

    def test_fuel_amount_assigned_new_value_correctly_with_valid_data(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        car.fuel_amount = 10
        self.assertEqual(10, car.fuel_amount)

    def test_fuel_amount_assigned_new_value_with_invalid_data_raises(self):
        car = Car("a", "b", 1, 4)
        self.assertEqual(0, car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_car_refuel_with_negative_or_zero_amount_raises(self):
        car = Car("a", "b", 1, 4)

        with self.assertRaises(Exception) as ex:
            car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_car_refuel_with_positive_amount_less_than_fuel_capacity(self):
        car = Car("a", "b", 1, 40)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(30)
        self.assertEqual(30, car.fuel_amount)

    def test_car_refuel_with_positive_amount_more_than_fuel_capacity(self):
        car = Car("a", "b", 1, 40)
        self.assertEqual(0, car.fuel_amount)
        car.refuel(50)
        self.assertEqual(40, car.fuel_amount)

    def test_car_drives_with_enough_fuel_for_provided_distance(self):
        car = Car("a", "b", 6.5, 40)
        car.refuel(30)
        self.assertEqual(30, car.fuel_amount)
        car.drive(400)
        self.assertEqual(4, car.fuel_amount)

    def test_car_drives_with_not_enough_fuel_amount_for_provided_distance_raises(self):
        car = Car("a", "b", 6.5, 40)
        car.refuel(30)
        self.assertEqual(30, car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            car.drive(600)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
