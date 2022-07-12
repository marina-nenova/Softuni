from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Test", 10)

    def test_paint_factory_init(self):
        name = "Test"
        capacity = 10
        paint_factory = PaintFactory(name, capacity)

        self.assertEqual(name, paint_factory.name)
        self.assertEqual(capacity, paint_factory.capacity)
        self.assertEqual({}, paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], paint_factory.valid_ingredients)

    def test_can_add_returns_true_if_quantity(self):
        result = self.paint_factory.can_add(5)
        self.assertEqual(True, result)

        result = self.paint_factory.can_add(10)
        self.assertEqual(True, result)

    def test_can_add_returns_false_if_not_valid_quantity(self):
        result = self.paint_factory.can_add(15)
        self.assertEqual(False, result)

    def test_add_ingredient_if_product_type_not_valid_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("purple", 5)
        self.assertEqual(f"Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_if_product_quantity_not_valid_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 15)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_if_product_and_quantity_are_valid(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual({"white": 5}, self.paint_factory.ingredients)

        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual({"white": 10}, self.paint_factory.ingredients)

    def test_remove_ingredient_if_product_type_not_existing_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("white", 10)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_if_product_quantity_more_than_existing_raises(self):
        self.paint_factory.add_ingredient("white", 5)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 10)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_if_valid_product_type_and_quantity(self):
        self.paint_factory.add_ingredient("white", 10)
        self.paint_factory.remove_ingredient("white", 10)
        result = self.paint_factory.ingredients["white"]
        self.assertEqual(0, result)

    def test_products_property_returns_correct_ingredients(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.add_ingredient("yellow", 5)
        result = self.paint_factory.products
        expected = {"white": 5, "yellow": 5}
        self.assertEqual(expected, result)

    def test_represent_method_returns_correct_string(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.add_ingredient("yellow", 5)
        result = str(self.paint_factory)
        expected = f"Factory name: Test with capacity 10.\nwhite: 5\nyellow: 5\n"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()