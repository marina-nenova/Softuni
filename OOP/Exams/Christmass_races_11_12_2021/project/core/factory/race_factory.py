from project.race import Race


class RaceFactory:

    @staticmethod
    def create_race(name):
        return Race(name)
