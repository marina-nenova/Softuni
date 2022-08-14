from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        try:
            self.speed += 3
        except ValueError:
            self.speed = self.MAX_SPEED
