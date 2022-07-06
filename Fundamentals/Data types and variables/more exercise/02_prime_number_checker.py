number = int(input())
number_is_prime = True

for i in range(2, number):
    if number % i == 0:
        number_is_prime = False
        break
if not number_is_prime:
    print("False")
else:
    print("True")
