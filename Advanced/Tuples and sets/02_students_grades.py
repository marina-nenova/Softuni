n = int(input())
students_info = {}

for _ in range(n):
    name, grade = input().split()
    if name not in students_info:
        students_info[name] = []
    students_info[name].append(float(grade))

for name, grades in students_info.items():
    print(f"{name} -> {' '.join([f'{gr:.2f}' for gr in grades])} (avg: {(sum(grades)/len(grades)):.2f})")
