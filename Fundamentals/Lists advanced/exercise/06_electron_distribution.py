number_of_electrons = int(input())

shells = []
index = 1
while number_of_electrons > 0:
    electrons = 2 * (index ** 2)
    if electrons <= number_of_electrons:
        shells.append(electrons)
        number_of_electrons -= electrons
    else:
        shells.append(number_of_electrons)
        number_of_electrons = 0
    index += 1
print(shells)