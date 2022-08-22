class Validator:
    @staticmethod
    def raise_if_phone_number_not_valid(phone_number):
        if not phone_number.startswith("0") or not len(phone_number) == 10 or not phone_number.isdigit():
            raise ValueError("Invalid phone number!")

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_less_than_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_phone_number_already_exists_in_collection(collection, phone_number, message):
        if any([obj.phone_number == phone_number for obj in collection]):
            raise Exception(message)

    @staticmethod
    def raise_if_menu_doesnt_have_enough_items(menu, min_items, message):
        if len(menu) < min_items:
            raise Exception(message)

    @staticmethod
    def raise_if_meal_doesnt_exist(collection, meal_name, message):
        if not any([obj.name == meal_name for obj in collection]):
            raise Exception(message)

    @staticmethod
    def raise_if_not_enough_meal_quantity(meal, wanted_quantity, message):
        if meal.quantity < wanted_quantity:
            raise Exception(message)

    @staticmethod
    def raise_if_no_meals_in_shopping_cart(shopping_cart, message):
        if not shopping_cart:
            raise Exception(message)

    @staticmethod
    def raise_if_not_meal(meal, meal_name, wanted_quantity):
        if meal is None:
            raise Exception(f"{meal_name} is not on the menu!")
        elif meal.quantity < wanted_quantity:
            raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
