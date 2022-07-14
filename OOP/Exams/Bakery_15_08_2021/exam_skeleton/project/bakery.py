from project.core.factory.drink_factory import DrinkFactory
from project.core.factory.food_factory import FoodFactory
from project.core.factory.table_factory import TableFactory
from project.core.validator.validator import Validator


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name cannot be empty string or white space!")

        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        Validator.raise_if_food_already_exists(self.food_menu, name, f"{food_type} {name} is already in the menu!")

        food = FoodFactory.create_food(food_type, name, price)
        self.food_menu.append(food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        Validator.raise_if_drink_already_exists(self.drinks_menu, name, f"{drink_type} {name} is already in the menu!")

        drink = DrinkFactory.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        Validator.raise_if_table_already_exists(self.tables_repository, table_number,
                                                f"Table {table_number} is already in the bakery!")

        table = TableFactory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:

                table.is_reserved = True
                table.number_of_people = number_of_people

                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.find_table_by_table_number(table_number)

        if table is None:
            return f"Could not find table {table_number}"

        ordered_food = f"Table {table_number} ordered:\n"
        non_existing_food = f"{self.name} does not have in the menu:\n"

        for food_name in food_names:
            food = Bakery.find_instance_by_name(food_name, self.food_menu)
            if food is not None:
                ordered_food += f"{repr(food)}\n"
                table.order_food(food)
            else:
                non_existing_food += f"{food_name}\n"

        output = ordered_food + non_existing_food
        return output.strip()

    @staticmethod
    def find_instance_by_name(name, collection):
        for item in collection:

            if item.name == name:
                return item

        return None

    def find_table_by_table_number(self, table_number):
        for table in self.tables_repository:

            if table.table_number == table_number:
                return table

        return None

    def order_drink(self, table_number: int, *drink_names):
        table = self.find_table_by_table_number(table_number)

        if table is None:
            return f"Could not find table {table_number}"

        ordered_drinks = f"Table {table_number} ordered:\n"
        non_existing_drinks = f"{self.name} does not have in the menu:\n"

        for drink_name in drink_names:
            drink = Bakery.find_instance_by_name(drink_name, self.drinks_menu)

            if drink is not None:
                ordered_drinks += f"{repr(drink)}\n"
                table.order_drink(drink)
            else:
                non_existing_drinks += f"{drink_name}\n"

        output = ordered_drinks + non_existing_drinks
        return output.strip()

    def leave_table(self, table_number: int):
        table = self.find_table_by_table_number(table_number)

        if table is not None:
            bill = table.get_bill()
            table.clear()
            self.total_income += bill
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        output = ""

        for table in self.tables_repository:
            if not table.is_reserved:
                output += table.free_table_info() + "\n"

        return output.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
