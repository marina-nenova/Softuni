from project.core.validator.validator import Validator


class Player:
    __used_names = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Name not valid!")
        Validator.raise_if_player_name_exists(Player.__used_names, value, f"Name {value} is already used!")
        self.__name = value
        Player.__used_names.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_value_is_less_than_min_value(value, 12, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.raise_if_value_out_if_range(value, 0, 100, "Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def __gt__(self, other):
        return self.stamina > other.stamina
