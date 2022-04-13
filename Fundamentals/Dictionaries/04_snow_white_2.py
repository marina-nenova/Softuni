class Dwarfs:

    def __init__(self, name, color, physics):
        self.name = name
        self.color = color
        self.physics = int(physics)


command = input()
dwarfs = {}
while not command == "Once upon a time":
    name, color, physics = command.split(" <:> ")
    dwarf = Dwarfs(name, color, physics)
    if color not in dwarfs:
        dwarfs[color] = [dwarf]
    for dwarf_info in dwarfs[color]:
        if dwarf_info.name == name:
            dwarf_info.physics = max(dwarf_info.physics, int(physics))
        else:
            dwarfs[color].append(dwarf)

    command = input()
sorted_dwarfs = sorted(dwarfs.items(), key=lambda d: d[color].physics)

for dwarf in sorted_dwarfs:
    print(f"({dwarf.color}) {dwarf.name} <-> {dwarf.physics}")