employees = [int(num) for num in input().split()]
factor = int(input())
happiness = [num * factor for num in employees]
average_happiness = sum(happiness) / len(happiness)

happy_employees = [value for value in happiness if value >= average_happiness]

if len(happy_employees) >= len(employees) / 2:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees)}. Employees are not happy!")
