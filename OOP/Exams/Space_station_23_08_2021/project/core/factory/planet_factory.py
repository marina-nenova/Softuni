from project.planet.planet import Planet


class PlanetFactory:
    @staticmethod
    def create_planet(name, items):
        planet = Planet(name)
        planet.items = (items.split(", "))
        return planet
