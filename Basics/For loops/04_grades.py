number_of_students = int(input())
top_student = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail = 0
all_grades = 0


for student in range(number_of_students):
    grade = float(input())
    all_grades += grade
    if grade >= 5:
        top_student += 1
    elif 4 <= grade <= 4.99:
        between_4_and_5 += 1
    elif 3 <= grade <= 3.99:
        between_3_and_4 += 1
    elif 2 <= grade <= 2.99:
        fail += 1

top_student_percent = (top_student / number_of_students) * 100
between_4_and_5_percent = (between_4_and_5 / number_of_students) * 100
between_3_and_4_percent = (between_3_and_4 / number_of_students) * 100
fail_percent = (fail / number_of_students) * 100
average_grade = all_grades / number_of_students

print(f"Top students: {top_student_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average_grade:.2f}")