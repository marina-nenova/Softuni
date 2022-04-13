command = input()
courses = {}
while ":" in command:
    name, i_d, course = command.split(":")
    if course not in courses:
        courses[course] = {}
    courses[course][name] = int(i_d)
    command = input()

searched_course = command
if "_" in searched_course:
    searched_course = searched_course.replace("_", " ")

for name, i_d in courses[searched_course].items():
    print(f"{name} - {i_d}")
