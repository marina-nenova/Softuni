from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingTests(TestCase):
    def test_shopping_cart_initialized_correctly_with_valid_data(self):
        sc = ShoppingCart("Test", 500)
        self.assertEqual("Test", sc.shop_name)
        self.assertEqual(500, sc.budget)
        self.assertEqual({}, sc.products)

    def test_shop_name_not_alpha_raises(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("Test1", 500)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_not_capitalized_raises(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("test", 500)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_product_price_100_or_more_raises(self):
        sc = ShoppingCart("Test", 500)
        with self.assertRaises(ValueError) as ve:
            for price in range(100, 105):
                sc.add_to_cart("apple", price)
        self.assertEqual("Product apple cost too much!", str(ve.exception))

    def test_add_to_cart_if_product_doesnt_exist(self):
        sc = ShoppingCart("Test", 500)
        self.assertEqual({}, sc.products)
        result = sc.add_to_cart("Apple", 50)
        self.assertEqual({"Apple": 50}, sc.products)
        self.assertEqual("Apple product was successfully added to the cart!", result)

    def test_add_to_cart_if_product_exists(self):
        sc = ShoppingCart("Test", 500)
        sc.products = {"Apple": 50}
        result = sc.add_to_cart("Apple", 10)
        self.assertEqual({"Apple": 10}, sc.products)
        self.assertEqual("Apple product was successfully added to the cart!", result)

        sc.add_to_cart("Orange", 15)
        self.assertEqual({"Apple": 10, "Orange": 15}, sc.products)

    def test_remove_from_cart_if_product_doesnt_exist_raises(self):
        sc = ShoppingCart("Test", 500)
        sc.products = {"Apple": 50}
        self.assertEqual({"Apple": 50}, sc.products)
        with self.assertRaises(ValueError) as ve:
            sc.remove_from_cart("Orange")
        self.assertEqual("No product with name Orange in the cart!", str(ve.exception))

    def test_remove_from_cart_if_product_exists(self):
        sc = ShoppingCart("Test", 500)
        sc.products = {"Apple": 50, "Orange": 10}
        result = sc.remove_from_cart("Apple")
        self.assertEqual({"Orange": 10}, sc.products)
        self.assertEqual("Product Apple was successfully removed from the cart!", result)

        result = sc.remove_from_cart("Orange")
        self.assertEqual({}, sc.products)
        self.assertEqual("Product Orange was successfully removed from the cart!", result)

    def test_add_method_returns_new_shopping_cart(self):
        sc = ShoppingCart("Fresh", 500)
        sc.products = {"Apple": 10, "Orange": 15}
        sc2 = ShoppingCart("Shop", 300)
        sc2.products = {"Pear": 25}
        new_shop = sc + sc2
        self.assertEqual("FreshShop", new_shop.shop_name)
        self.assertEqual(800, new_shop.budget)
        self.assertEqual({"Apple": 10, "Orange": 15, "Pear": 25}, new_shop.products)

    def test_buy_products_if_not_enough_budget_raises(self):
        sc = ShoppingCart("Fresh", 50)
        sc.products = {"Apple": 25, "Orange": 35}
        with self.assertRaises(ValueError) as ve:
            sc.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ve.exception))

    def test_buy_products_if_enough_budget(self):
        sc = ShoppingCart("Fresh", 60)
        sc.products = {"Apple": 25, "Orange": 35}
        result = sc.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 60.00lv.", result)

        sc = ShoppingCart("Fresh", 70)
        sc.products = {"Apple": 25, "Orange": 35}
        result = sc.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 60.00lv.", result)


if __name__ == "__main__":
    main()
