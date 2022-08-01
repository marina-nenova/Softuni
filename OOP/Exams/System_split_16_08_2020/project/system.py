from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_instance_by_name(hardware_name, System._hardware)
        if hardware is None:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_instance_by_name(hardware_name, System._hardware)
        if hardware is None:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_instance_by_name(hardware_name, System._hardware)
        software = System.find_instance_by_name(software_name, System._software)
        if hardware is None and software is None:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def find_instance_by_name(name, collection):
        for instance in collection:
            if instance.name == name:
                return instance
        return None

    @staticmethod
    def analyze():
        total_hardware_capacity = sum([hw.capacity for hw in System._hardware])
        total_hardware_memory = sum([hw.memory for hw in System._hardware])
        capacity_taken = sum([sw.capacity_consumption for sw in System._software])
        memory_taken = sum([sw.memory_consumption for sw in System._software])

        output = f"System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {memory_taken} / {total_hardware_memory}\n" \
                 f"Total Capacity Taken: {capacity_taken} / {total_hardware_capacity}"
        return output

    @staticmethod
    def system_split():
        output = ""

        for hardware in System._hardware:
            express_software_installed = [sw for sw in hardware.software_components if sw.software_type == "Express"]
            light_software_installed = [sw for sw in hardware.software_components if sw.software_type == "Light"]
            memory_usage = sum([sw.memory_consumption for sw in hardware.software_components])
            capacity_usage = sum([sw.capacity_consumption for sw in hardware.software_components])
            software_components_names = [sw.name for sw in
                                         hardware.software_components] if hardware.software_components else "None"

            output += f"Hardware Component - {hardware.name}\n"
            output += f"Express Software Components: {len(express_software_installed)}\n"
            output += f"Light Software Components: {len(light_software_installed)}\n"
            output += f"Memory Usage: {memory_usage} / {hardware.memory}\n"
            output += f"Capacity Usage: {capacity_usage} / {hardware.capacity}\n"
            output += f"Type: {hardware.hardware_type}\n"
            output += f"Software Components: {', '.join(software_components_names)}\n"

        return output.strip()
