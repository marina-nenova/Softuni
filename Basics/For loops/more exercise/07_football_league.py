stadium_capacity = int(input())
number_of_fans = int(input())
a = 0
b = 0
v = 0
g = 0

for fan in range(number_of_fans):
    sector = input()
    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1
a_percentage = (a / number_of_fans) * 100
b_percentage = (b / number_of_fans) * 100
v_percentage = (v / number_of_fans) * 100
g_percentage = (g / number_of_fans) * 100
fan_percentage = (number_of_fans / stadium_capacity) * 100

print(f"{a_percentage:.2f}%")
print(f"{b_percentage:.2f}%")
print(f"{v_percentage:.2f}%")
print(f"{g_percentage:.2f}%")
print(f"{fan_percentage:.2f}%")