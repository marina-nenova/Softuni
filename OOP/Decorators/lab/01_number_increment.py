def number_increment(numbers):
    def increase():
        return [num + 1 for num in numbers]
    return increase()


print(number_increment([2, 3, 4]))