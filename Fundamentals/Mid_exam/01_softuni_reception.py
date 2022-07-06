employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())
students = int(input())

total_students_per_hour = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency
time_needed = 0

while students > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        continue
    students -= total_students_per_hour

print(f"Time needed: {time_needed}h.")
