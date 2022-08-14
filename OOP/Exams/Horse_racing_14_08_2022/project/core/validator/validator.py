class Validator:
    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_less_than_min_value(value, min_value, message):
        if value < min_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_is_less_than_min_symbols(name, min_symbols, message):
        if len(name) < min_symbols:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_bigger_than_max_value(value, max_value, message):
        if value > max_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_race_type_not_valid(race_type, message):
        valid_race_types = ["Winter", "Spring", "Autumn", "Summer"]
        if race_type not in valid_race_types:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_already_exists_in_collection(collection, name, message):
        if any([obj.name == name for obj in collection]):
            raise Exception(message)

    @staticmethod
    def raise_if_race_type_already_exists(collection, race_type, message):
        if any([obj.race_type == race_type for obj in collection]):
            raise Exception(message)

    @staticmethod
    def find_available_jockey_raise_if_none(jockeys, name, message):
        for j in jockeys:
            if j.name == name:
                return j
        raise Exception(message)

    @staticmethod
    def find_available_horse_raise_if_none(horses, horse_type, message):
        for idx in range(len(horses) - 1, -1, -1):
            horse = horses[idx]
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                return horse
        raise Exception(message)

    @staticmethod
    def find_available_race_raise_if_none(races, race_type, message):
        for race in races:
            if race.race_type == race_type:
                return race
        raise Exception(message)

    @staticmethod
    def raise_if_jockey_doesnt_have_a_horse(jockey, message):
        if jockey.horse is None:
            raise Exception(message)

    @staticmethod
    def raise_if_not_enough_jockeys_in_race(race, message):
        if len(race.jockeys) < 2:
            raise Exception(message)
