n = int(input())
students_info = {}

for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in students_info:
        students_info[student_name] = []
    students_info[student_name].append(grade)

for student, grades in students_info.items():
    average_grade = sum(grades) / len(grades)
    students_info[student] = average_grade
    if students_info[student] >= 4.5:
        print(f"{student} -> {students_info[student]:.2f}")
