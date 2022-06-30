from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, money_for_care=45)
