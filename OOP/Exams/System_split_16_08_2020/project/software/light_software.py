import math

from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", math.floor(capacity_consumption * 1.5), math.floor(memory_consumption * 0.5))