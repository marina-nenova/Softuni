from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp():
    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        valid_team_names = {"Red Bull": RedBullTeam, "Mercedes": MercedesTeam}
        if team_name not in valid_team_names:
            raise ValueError("Invalid team name!")
        if team_name == "Red Bull":
            self.red_bull_team = valid_team_names[team_name](budget)
        elif team_name == "Mercedes":
            self.mercedes_team = valid_team_names[team_name](budget)
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.mercedes_team is None or self.red_bull_team is None:
            raise Exception("Not all teams have registered for the season.")

        better_position = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        mercedes_info = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)
        red_bull_info = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)

        return f"Red Bull: {red_bull_info}. Mercedes: {mercedes_info}. {better_position} is ahead at the " \
               f"{race_name} race."


