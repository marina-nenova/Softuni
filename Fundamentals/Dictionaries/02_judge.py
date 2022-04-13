command = input()
contests_info = {}
users_info = {}

while not command == "no more time":
    data = command.split(" -> ")
    user_name = data[0]
    contest = data[1]
    points = int(data[2])

    if contest not in contests_info:
        contests_info[contest] = {}
    if user_name not in contests_info[contest]:
        contests_info[contest][user_name] = points
    else:
        if points > contests_info[contest][user_name]:
            contests_info[contest][user_name] = points

    command = input()

for contest, users in contests_info.items():
    for user_name, points in users.items():
        if user_name not in users_info:
            users_info[user_name] = points
        else:
            users_info[user_name] += points

for contest, users in contests_info.items():
    print(f"{contest}: {len(users)} participants")
    count = 1
    for user_name, points in dict(sorted(users.items(), key=lambda kvp: (-kvp[1], kvp[0]))).items():
        print(f"{count}. {user_name} <::> {points}")
        count += 1

print("Individual standings:")

count_users = 1
for username, points in sorted(users_info.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{count_users}. {username} -> {points}")
    count_users += 1

# Peter -> OOP -> 350
# George -> OOP -> 250
# George -> Advanced -> 600
# George -> OOP -> 300
# Prakash -> OOP -> 300
# Prakash -> Advanced -> 250
# Ani -> JSCore -> 600
# no more time
