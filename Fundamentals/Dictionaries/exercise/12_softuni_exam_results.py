def student_exists(student, language):
    if student in exam_results[language]:
        return True

    return False


def remove_student(student):
    for student_info in exam_results.values():
        if student in student_info:
            del student_info[student]


command = input()
exam_results = {}
exam_submissions = {}

while not command == "exam finished":
    data = command.split("-")
    student_name = data[0]
    language = data[1]

    if language == "banned":
        remove_student(student_name)

    else:
        points = int(data[2])
        if language not in exam_results and language not in exam_submissions:
            exam_results[language] = {}
            exam_submissions[language] = 0

        if not student_exists(student_name, language):
            exam_results[language][student_name] = points
        else:
            if points > exam_results[language][student_name]:
                exam_results[language][student_name] = points

        exam_submissions[language] += 1
    command = input()

print("Results:")

for student_info in exam_results.values():
    if len(student_info) > 0:
        for student, points in student_info.items():
            print(f"{student} | {points}")

print("Submissions:")

for language, count in exam_submissions.items():
    print(f"{language} - {count}")
