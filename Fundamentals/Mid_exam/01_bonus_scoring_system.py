from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())

max_bonus_points = 0
student_attendance = 0

for student in range(students):
    attendance = int(input())
    total_bonus = ceil((attendance/lectures) * (5 + bonus))
    if total_bonus >= max_bonus_points:
        max_bonus_points = total_bonus
        student_attendance = attendance

print(f"Max Bonus: {max_bonus_points}.")
print(f"The student has attended {student_attendance} lectures.")