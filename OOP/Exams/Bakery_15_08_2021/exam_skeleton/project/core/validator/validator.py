class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_zero_or_less(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_inside_table_number_outside_of_range(value, message):
        if not 1 <= value <= 50:
            raise ValueError(message)

    @staticmethod
    def raise_if_outside_table_number_outside_of_range(value, message):
        if not 51 <= value <= 100:
            raise ValueError(message)

    @staticmethod
    def raise_if_food_already_exists(food_menu, food_name, message):
        for food in food_menu:
            if food.name == food_name:
                raise Exception(message)

    @staticmethod
    def raise_if_drink_already_exists(drink_menu, drink_name, message):
        for drink in drink_menu:
            if drink.name == drink_name:
                raise Exception(message)

    @staticmethod
    def raise_if_table_already_exists(tables, table_number, message):
        for table in tables:
            if table.table_number == table_number:
                raise Exception(message)
