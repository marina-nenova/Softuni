number_of_judges = int(input())

presentation = input()
total_grade_all_students = 0
counter = 0
while presentation != "Finish":
    total_grade = 0
    for num in range(number_of_judges):
        grade = float(input())
        total_grade += grade
        total_grade_all_students += grade
        counter += 1
    average_grade = total_grade / number_of_judges
    print(f"{presentation} - {average_grade:.2f}.")
    total_grade = 0
    presentation = input()

average_grade_all_students = total_grade_all_students / counter
print(f"Student's final assessment is {average_grade_all_students:.2f}.")
