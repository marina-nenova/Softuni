from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(20)

    def test_plantation_initialized_correctly_with_valid_data(self):
        size = 20
        plantation = Plantation(size)
        self.assertEqual(20, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_plantation_init_with_negative_size_raises(self):
        with self.assertRaises(ValueError) as ex:
            Plantation(-20)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_if_name_doesnt_exist_adds_worker_to_list(self):
        self.plantation.hire_worker("Adam")
        self.assertEqual(["Adam"], self.plantation.workers)

        result = self.plantation.hire_worker("Peter")
        self.assertEqual(["Adam", "Peter"], self.plantation.workers)
        self.assertEqual(f"Peter successfully hired.", result)

    def test_hire_worker_if_worker_exists_raises(self):
        self.plantation.hire_worker("Adam")
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Adam")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_len_method_returns_correctly(self):
        self.plantation.plants = {"Adam": ["Tomato", "Peppers"], "Peter": ["Cucumbers"]}
        self.assertEqual(3, len(self.plantation))

    def test_planting_if_worker_doesnt_exist_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Adam", "Tomato")
        self.assertEqual("Worker with name Adam is not hired!", str(ex.exception))

    def test_planting_if_plantation_is_full_raises(self):
        self.plantation.size = 5
        self.plantation.hire_worker("Adam")
        for index in range(5):
            self.plantation.planting("Adam", "Tomato" + str(index))

        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Adam", "Tomato5")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_if_space_and_worker_not_in_plants(self):
        self.plantation.hire_worker("Adam")
        result = self.plantation.planting("Adam", "Tomato")
        self.assertEqual({"Adam": ["Tomato"]}, self.plantation.plants)
        self.assertEqual("Adam planted it's first Tomato.", result)

    def test_planting_if_space_and_worker_in_plants(self):
        self.plantation.hire_worker("Adam")
        self.plantation.planting("Adam", "Peppers")
        result = self.plantation.planting("Adam", "Tomato")
        self.assertEqual({"Adam": ["Peppers", "Tomato"]}, self.plantation.plants)
        self.assertEqual(f"Adam planted Tomato.", result)

    def test_str_returns_correct_string(self):
        self.plantation.hire_worker("Adam")
        self.plantation.hire_worker("Peter")
        self.plantation.planting("Adam", "Tomato")
        self.plantation.planting("Adam", "Beans")
        self.plantation.planting("Peter", "Peppers")
        result = str(self.plantation)
        expected = "Plantation size: 20\n" \
                   "Adam, Peter\n" \
                   "Adam planted: Tomato, Beans\n" \
                   "Peter planted: Peppers"
        self.assertEqual(expected, result)

    def test_repr_returns_correct_string(self):
        self.plantation.hire_worker("Adam")
        self.plantation.hire_worker("Peter")
        result = repr(self.plantation)
        expected = 'Size: 20\nWorkers: Adam, Peter'

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
