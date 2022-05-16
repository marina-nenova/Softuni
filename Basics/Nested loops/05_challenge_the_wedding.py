number_of_men = int(input())
number_of_women = int(input())
number_of_tables = int(input())
table = ""
for man in range(1, number_of_men + 1):
    for woman in range(1, number_of_women + 1):
        if number_of_tables > 0:
            print(f"({man} <-> {woman})", end = " ")
        number_of_tables -= 1



