from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class FoodFactory:
    food_types = {
        "Bread": Bread,
        "Cake": Cake
    }

    @staticmethod
    def create_food(food_type, name, price):
        return FoodFactory.food_types[food_type](name, price)
