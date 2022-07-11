from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        available_memory = self.memory - sum(x.memory_consumption for x in self.software_components)
        available_capacity = self.capacity - sum(x.capacity_consumption for x in self.software_components)
        if software.memory_consumption <= available_memory and software.capacity_consumption <= available_capacity:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
