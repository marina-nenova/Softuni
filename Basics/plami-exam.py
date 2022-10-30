# n = int(input())
# result = ''
# for a in range(1, 9):
#     for b in range(9, a, -1):
#         for c in range(0, 9):
#             for d in range(9, c, -1):
#                 sum_nums = a + b + c + d
#                 prod_nums = a * b * c * d
#                 if sum_nums == prod_nums and (n % 10 == 5):
#                     result = f'{a}{b}{c}{d}'
#                     break
#                 elif prod_nums // sum_nums == 3 and (n % 3 == 0):
#                     result = f'{d}{c}{b}{a}'
#                     break
#             if result:
#                 break
#         if result:
#             break
#     if result:
#         break
#
# if not result:
#     print("Nothing found")
# else:
#     print(result)


# current_height = 5364
# goal = 8848
# max_days = 5
# days_climbing = 1
#
# success = False
# command = input()
# while command != 'END':
#     meters_climbed = int(input())
#
#     if command == 'Yes':
#         days_climbing += 1
#         if days_climbing > max_days:
#             break
#         current_height += meters_climbed
#
#     else:
#         current_height += meters_climbed
#
#     if current_height >= goal:
#         success = True
#         break
#
#     command = input()
#
# if success:
#     print(f"Goal reached for {days_climbing} days!")
# else:
#     print("Failed!")
#     print(current_height)

# dancers = int(input())
# points = float(input())
# season = input()
# location = input()
#
# prize = points * dancers
#
# if location == 'Bulgaria':
#     if season == 'summer':
#         prize = prize - (prize * 0.05)
#     elif season == 'winter':
#         prize = prize - (prize * 0.08)
#
# elif location == 'Abroad':
#     prize = prize + (prize * 0.5)
#     if season == 'summer':
#         prize = prize - (prize * 0.1)
#     elif season == 'winter':
#         prize = prize - (prize * 0.15)
#
# charity_sum = prize * 0.75
# money_per_dancer = (prize - charity_sum) / dancers
#
# print(f"Charity - {charity_sum:.2f}")
# print(f"Money per dancer - {money_per_dancer:.2f}")


# students = int(input())
#
# fail = 0
# between_3_and_4 = 0
# between_4_and_5 = 0
# top = 0
#
# total_score = 0
#
# for i in range(students):
#
#     result = float(input())
#     total_score += result
#
#     if result < 3:
#         fail += 1
#     elif result < 4:
#         between_3_and_4 += 1
#     elif result < 5:
#         between_4_and_5 += 1
#     else:
#         top += 1
#
# average_score = total_score / students
#
# failed_students = (fail / students) * 100
# between_3_and_4_students = (between_3_and_4 / students) * 100
# between_4_and_5_students = (between_4_and_5 / students) * 100
# top_students = (top / students) * 100
#
# print(f"Top students: {top_students:.2f}%")
# print(f"Between 4.00 and 4.99: {between_4_and_5_students:.2f}%")
# print(f"Between 3.00 and 3.99: {between_3_and_4_students:.2f}%")
# print(f"Fail: {failed_students:.2f}%")
# print(f"Average: {average_score:.2f}")
