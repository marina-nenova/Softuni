from copy import copy
from project.client import Client
from project.core.validator.validator import Validator
from project.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __find_client_by_phone_number(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client
        new_client = Client(phone_number)
        self.clients_list.append(new_client)
        return new_client

    def __find_meal_by_name(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def register_client(self, client_phone_number: str):
        Validator.raise_if_phone_number_already_exists_in_collection(
            self.clients_list,
            client_phone_number,
            "The client has already been registered!"
        )
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        valid_meal_types = ["Starter", "MainDish", "Dessert"]

        for meal in meals:
            if meal.__class__.__name__ in valid_meal_types:
                self.menu.append(meal)

    def show_menu(self):
        Validator.raise_if_menu_doesnt_have_enough_items(self.menu, 5, "The menu is not ready!")

        output = ""
        for meal in self.menu:
            output += meal.details() + '\n'
        return output.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        Validator.raise_if_menu_doesnt_have_enough_items(self.menu, 5, "The menu is not ready!")

        client = self.__find_client_by_phone_number(client_phone_number)

        meals_to_add = []
        for meal_name, wanted_quantity in meal_names_and_quantities.items():
            meal = self.__find_meal_by_name(meal_name)
            Validator.raise_if_not_meal(meal, meal_name, wanted_quantity)
            meal_to_cart = copy(meal)
            meal_to_cart.quantity = wanted_quantity
            meals_to_add.append(meal_to_cart)
            meal.quantity -= wanted_quantity

        client.shopping_cart.extend(meals_to_add)
        client.bill = sum([meal.price * meal.quantity for meal in client.shopping_cart])

        return f"Client {client.phone_number}" \
               f" successfully ordered {', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        Validator.raise_if_no_meals_in_shopping_cart(client.shopping_cart, "There are no ordered meals!")

        for meal_order in client.shopping_cart:
            meal = self.__find_meal_by_name(meal_order.name)
            meal.quantity += meal_order.quantity

        client.shopping_cart.clear()
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        Validator.raise_if_no_meals_in_shopping_cart(client.shopping_cart, "There are no ordered meals!")
        money_paid = client.bill
        client.shopping_cart.clear()
        client.bill = 0
        return f"Receipt #{Client.get_next_receipt_id()}" \
               f" with total amount of {money_paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
