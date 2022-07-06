a = int(input())
b = int(input())
number_of_passwords = int(input())
B = 64
A = 35


for x in range(1, a + 1):
    for y in range(1, b + 1):
        if number_of_passwords == 0:
            break
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end= "")
        number_of_passwords -= 1
        B += 1
        A += 1
        if A > 55:
            A= 35
        if B > 96:
            B = 64

