from project.system import System

System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.release_software_component("HDD", "Test")
System.release_software_component("HDD", "Test")
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())

#output
# 3
# Group Special with members Elon Musk, Warren Musk
# Person 0: Aliko Dangote
# Person 0: Aliko Dangote
# Person 1: Bill Gates
# Person 2: Warren Buffet
# Person 3: Elon Musk
# Person 4: Warren Musk