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
    def raise_if_value_out_if_range(value, min_value, max_value, message):
        if not min_value <= value <= max_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_player_name_exists(player_names, player_name, message):
        if player_name in player_names:
            raise Exception(message)

    @staticmethod
    def raise_if_supply_type_is_not_available(supplies, supply_type):
        messages_by_supply_type = {
            "Food": "There are no food supplies left!",
            "Drink": "There are no drink supplies left!"
        }

        for index in range(len(supplies)-1, -1, -1):
            supply = supplies[index]
            if supply.__class__.__name__ == supply_type:
                return supplies.pop(index)

        raise Exception(messages_by_supply_type[supply_type])
