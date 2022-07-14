from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Test", 5)

    def test_train_initialized_correctly(self):
        train = Train("Test", 10)
        self.assertEqual("Test", train.name)
        self.assertEqual(10, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_passenger_capacity_full_raises(self):
        self.train.passengers = ["A", "B", "C", "D", "E"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("F")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_passenger_that_already_exists_raises(self):
        self.train.passengers = ["A", "B", "C", "D"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("A")
        self.assertEqual("Passenger A Exists", str(ex.exception))

    def test_add_passenger_adds_passenger_and_returns_correct_string(self):
        self.train.passengers = ["A", "B", "C"]
        result = self.train.add("D")
        self.assertEqual(["A", "B", "C", "D"], self.train.passengers)
        self.assertEqual("Added passenger D", result)

        result = self.train.add("E")
        self.assertEqual(["A", "B", "C", "D", "E"], self.train.passengers)
        self.assertEqual("Added passenger E", result)

    def test_remove_passenger_who_does_not_exist_raises(self):
        self.train.passengers = ["A", "B", "C"]
        with self.assertRaises(ValueError) as ex:
            self.train.remove("D")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_passenger_removes_passenger_from_list(self):
        self.train.passengers = ["A", "B", "C"]
        result = self.train.remove("B")
        self.assertEqual(["A", "C"], self.train.passengers)
        self.assertEqual("Removed B", result)


if __name__ == "__main__":
    main()
