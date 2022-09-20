from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def __init__(self, budget: int):
        super().__init__(budget)
        self.expenses = 250000

    def calculate_revenue_after_race(self, race_pos: int):
        sponsors_positions = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
        revenue = 0
        for sponsor, positions in sponsors_positions.items():
            for position in positions:
                if race_pos <= position:
                    revenue += positions[position]
                    break

        revenue -= self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
