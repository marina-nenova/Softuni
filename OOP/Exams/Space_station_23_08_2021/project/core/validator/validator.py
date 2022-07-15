class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_astronaut_type_is_not_valid(valid_astronaut_types, astronaut_type, message):
        if astronaut_type not in valid_astronaut_types:
            raise Exception(message)

    @staticmethod
    def raise_if_astronaut_doesnt_exist(astronaut_repository, name, message):
        if not astronaut_repository.find_by_name(name):
            raise Exception(message)

    @staticmethod
    def raise_if_planet_doesnt_exist(planet_repository, name, message):
        if not planet_repository.find_by_name(name):
            raise Exception(message)

    @staticmethod
    def raise_if_not_suitable_astronauts(astronaut_repository, message):
        if not any([ast.oxygen > 30 for ast in astronaut_repository.astronauts]):
            raise Exception(message)
