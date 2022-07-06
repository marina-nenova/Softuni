n = int(input())

for text in range(n):
    info = input()
    name_start = info.index("@")
    name_end = info.index("|")
    name = info[name_start + 1: name_end]
    age_start = info.index("#")
    age_end = info.index("*")
    age = info[age_start + 1: age_end]
    print(f"{name} is {age} years old.")