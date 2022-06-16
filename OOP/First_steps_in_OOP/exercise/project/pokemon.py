class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        pokemon_name = self.name
        pokemon_health = self.health
        return f"{pokemon_name} with health {pokemon_health}"