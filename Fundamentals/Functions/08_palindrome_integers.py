def palindrome_check(numbers_list):
    for num in numbers_list:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


number = input().split(", ")
palindrome_check(number)
