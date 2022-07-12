from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for list in args:
            for el in list:
                total_expenses += el.get_monthly_expense()
        self.expenses = total_expenses
