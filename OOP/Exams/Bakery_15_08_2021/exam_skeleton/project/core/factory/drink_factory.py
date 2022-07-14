from project.drink.tea import Tea
from project.drink.water import Water


class DrinkFactory:
    drink_types = {
        "Tea": Tea,
        "Water": Water
    }

    @staticmethod
    def create_drink(drink_type, name, portion, brand):
        return DrinkFactory.drink_types[drink_type](name, portion, brand)
