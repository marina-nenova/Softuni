class Validator:
    @staticmethod
    def raise_if_string_is_empty(string, message):
        if not string:
            raise ValueError(message)

    @staticmethod
    def raise_if_price_is_negative_or_zero(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def validate_fish_type(fish_type):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish_types:
            return False
        return True

    @staticmethod
    def validate_decoration_type(decoration_type):
        valid_decoration_types = ["Ornament", "Plant"]
        if decoration_type not in valid_decoration_types:
            return False
        return True

    @staticmethod
    def validate_aquarium_type(aquarium_type):
        valid_aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_aquarium_types:
            return False
        return True
