command = input()
dwarfs = {}
colors = {}
while command != "Once upon a time":
    data = command.split(" <:> ")
    name = data[0]
    color = data[1]
    physics = int(data[2])
    i_d = name + ":" + color
    if i_d not in dwarfs:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        dwarfs[i_d] = [0, color]
    dwarfs[i_d][0] = max([dwarfs[i_d][0], physics])
    command = input()

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))
for key, value in sorted_dwarfs.items():
    data = key.split(":")
    print(f"({data[1]}) {data[0]} <-> {value[0]}")
