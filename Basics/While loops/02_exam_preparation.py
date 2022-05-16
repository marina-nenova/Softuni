# number_of_fails = int(input())
# command = ""
# problem = ""
# fail_counter = 0
# total_score = 0
# number_of_problems = 0
# while command != "Enough":
#     problem = command
#     command = input()
#     if command == "Enough":
#         average_score = total_score / number_of_problems
#         print(f"Average score: {average_score:.2f}")
#         print(f"Number of problems: {number_of_problems}")
#         print(f"Last problem: {problem}")
#         break
#     grade = int(input())
#     if grade <= 4:
#         fail_counter += 1
#         if fail_counter == number_of_fails:
#             print(f"You need a break, {fail_counter} poor grades.")
#             break
#     number_of_problems += 1
#     total_score += grade

failed_threshhold = int(input())
failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ""
has_failed = True

while failed_times < failed_threshhold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break

    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_threshhold} poor grades.")
else:
    print(f"Average score: {grades_sum / solved_problems_count:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")

