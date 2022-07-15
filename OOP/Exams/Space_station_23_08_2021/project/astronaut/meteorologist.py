from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, oxygen=90)

    def breathe(self):
        self.oxygen -= 15
