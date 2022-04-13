command = input()
courses_info = {}
while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses_info:
        courses_info[course_name] = []
    courses_info[course_name].append(student_name)
    command = input()

for course, students in courses_info.items():
    print(f"{course}: {len(courses_info[course])}")
    for student in students:
        print(f"-- {student}")
