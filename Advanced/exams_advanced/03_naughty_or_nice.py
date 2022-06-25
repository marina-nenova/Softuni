from collections import Counter


def naughty_or_nice_list(names_list,*args, **kwargs):
    santa_list = {"Nice":[], "Naughty": [], "Not found": []}
    num_counter = Counter(el[0] for el in names_list)

    for el in args:
        data = el.split("-")
        number = int(data[0])
        kid_type = data[1]
        if num_counter[number] == 1:
            name = [name for num, name in names_list if num == number]
            santa_list[kid_type].extend(name)
            names_list = [el for el in names_list if el[0] != number]

    name_counter = Counter(el[1] for el in names_list)

    for name, type in kwargs.items():
        if name_counter[name] == 1:
            santa_list[type].append(name)
            names_list = [el for el in names_list if el[1] != name]

    for num, name in names_list:
        santa_list["Not found"].append(name)

    output = ""

    for type, kids in santa_list.items():
        if kids:
            output += f"{type}: {', '.join(kids)}\n"

    return output



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
