first_num_beginning = int(input())
second_num_beginning = int(input())
first_num_end = int(input())
second_num_end = int(input())
num1_is_prime = False
num2_is_prime = False

for num1 in range(first_num_beginning, (first_num_beginning + first_num_end) + 1):
    for num2 in range(second_num_beginning, (second_num_beginning + second_num_end) + 1):
        counter1 = 0
        for digit1 in range(1, num1 + 1):
            if num1 % digit1 == 0:
                counter1 +=1
                if counter1 > 2:
                    num1_is_prime = False
                    break
                if counter1 == 2:
                    num1_is_prime = True
        counter2 = 0
        for digit2 in range(1, num2 + 1):
            if num2 % digit2 == 0:
                counter2 += 1
                if counter2 > 2:
                    num2_is_prime = False
                    break
                if counter2 == 2:
                    num2_is_prime = True
        if num1_is_prime and num2_is_prime:
            print(f"{num1}{num2}")


