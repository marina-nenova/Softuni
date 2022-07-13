from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationFactory:
    decoration_types = {
        "Ornament": Ornament,
        "Plant": Plant
    }

    @staticmethod
    def create_decoration(decoration_type):
        return DecorationFactory.decoration_types[decoration_type]()
