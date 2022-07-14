from project.pet_shop import PetShop

from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Paws")

    def test_pet_shop_initialized_correctly(self):
        pet_shop = PetShop("Paws")
        self.assertEqual("Paws", pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_add_food_with_negative_or_zero_quantity_raises(self):
        for quantity in range(-5, 0):
            with self.assertRaises(ValueError) as ex:
                self.pet_shop.add_food("dog food", quantity)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_adds_food_that_does_not_already_exist(self):
        self.pet_shop.add_food("Dog food", 10)
        self.assertEqual({"Dog food": 10}, self.pet_shop.food)

    def test_add_food_adds_quantity_to_food_that_already_exist(self):
        self.pet_shop.add_food("Dog food", 10)
        self.pet_shop.add_food("Dog food", 10)
        self.assertEqual({"Dog food": 20}, self.pet_shop.food)
        self.pet_shop.add_food("Dog food", 10)
        self.assertEqual({"Dog food": 30}, self.pet_shop.food)

    def test_add_food_returns_correct_string(self):
        result = self.pet_shop.add_food("Dog food", 10)
        expected = "Successfully added 10.00 grams of Dog food."
        self.assertEqual(expected, result)

    def test_add_pet_with_name_that_already_exists_raises(self):
        self.pet_shop.add_pet("Loki")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Loki")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_adds_pet_name_to_list(self):
        self.pet_shop.add_pet("Loki")
        self.assertEqual(["Loki"], self.pet_shop.pets)
        self.pet_shop.add_pet("Milo")
        self.assertEqual(["Loki", "Milo"], self.pet_shop.pets)

    def test_add_pet_returns_correct_string(self):
        result = self.pet_shop.add_pet("Loki")
        expected = "Successfully added Loki."
        self.assertEqual(expected, result)

    def test_feed_pet_if_pet_name_not_in_pet_shop_raises(self):
        self.pet_shop.add_pet("Loki")
        self.pet_shop.add_food("Cat food", 100)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Dog food", "Milo")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_if_food_name_not_in_pet_shop(self):
        self.pet_shop.add_pet("Loki")
        self.pet_shop.add_food("Cat food", 100)
        result = self.pet_shop.feed_pet("Dog food", "Loki")
        self.assertEqual("You do not have Dog food", result)

    def test_feed_pet_if_food_quantity_less_than_100_restocks_food(self):
        self.pet_shop.add_pet("Loki")
        self.pet_shop.add_food("Dog food", 99)
        result = self.pet_shop.feed_pet("Dog food", "Loki")
        self.assertEqual(1099.00, self.pet_shop.food["Dog food"])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_if_enough_food_food_quantity_decreases(self):
        self.pet_shop.add_pet("Loki")
        self.pet_shop.add_food("Dog food", 500)

        self.pet_shop.feed_pet("Dog food", "Loki")
        self.assertEqual({"Dog food": 400}, self.pet_shop.food)

        self.pet_shop.feed_pet("Dog food", "Loki")
        self.assertEqual({"Dog food": 300}, self.pet_shop.food)

    def test_feed_pet_if_enough_food_returns_correct_string(self):
        self.pet_shop.add_pet("Loki")
        self.pet_shop.add_food("Dog food", 500)

        result = self.pet_shop.feed_pet("Dog food", "Loki")
        expected = "Loki was successfully fed"
        self.assertEqual(expected, result)

    def test_repr_returns_correct_string(self):
        self.pet_shop.add_pet("Loki")
        self.pet_shop.add_pet("Milo")
        expected = f'Shop Paws:\nPets: Loki, Milo'
        self.assertEqual(expected, str(self.pet_shop))


if __name__ == "__main__":
    main()
