# command = input()
# companies_info = {}
#
# while not command == "End":
#     company, employee_id = command.split(" -> ")
#     if company not in companies_info:
#         companies_info[company] = []
#     if employee_id not in companies_info[company]:
#         companies_info[company].append(employee_id)
#     command = input()
#
# for company, employee_ids in companies_info.items():
#     print(company)
#     for employee in employee_ids:
#         print(f'-- {employee}')


data = input().split(" -> ")
comp_dict = {}

while data[0] != 'End':
    if data[0] not in comp_dict:
        comp_dict[data[0]] = []
    if data[1] not in comp_dict[data[0]]:
        comp_dict[data[0]].append(data[1])

    data = input().split(" -> ")

for key, value in comp_dict.items():
    print(f'{key}')
    for num in value:
        print(f"-- {num}")