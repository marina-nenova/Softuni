def perfect_number_finder(num):
    aliquot_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            aliquot_sum += divisor
    if aliquot_sum == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number_finder(number)
