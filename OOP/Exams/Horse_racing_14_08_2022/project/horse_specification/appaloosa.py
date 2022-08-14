from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        try:
            self.speed += 2
        except ValueError:
            self.speed = self.MAX_SPEED
