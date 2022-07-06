# student_name = input()
# grade = 1
# total_result = 0
# counter = 0
#
# while grade <= 12:
#     result = float(input())
#     total_result += result
#     if grade == 12:
#         average_grade = total_result / grade
#         print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
#         break
#     grade += 1
#     if result < 4:
#         grade -= 1
#         counter += 1
#         total_result -= result
#         if counter == 2:
#             print(f"{student_name} has been excluded at {grade} grade")
#             break

student_name = input()
grade = 1
total_result = 0
fail_counter = 0
has_failed = False
while grade < 13:
    result = float(input())
    if result >= 4:
        grade += 1
        total_result += result
    else:
        fail_counter += 1
        if fail_counter == 2:
            print(f"{student_name} has been excluded at {grade} grade")
            has_failed = True
            break

if not has_failed:
    average_grade = total_result / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")






