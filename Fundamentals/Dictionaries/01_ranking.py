command = input()
contests = {}

while not command == "end of contests":

    contest_name, password = command.split(":")
    contests[contest_name] = password

    command = input()

submissions_data = input()
candidates_info = {}

while not submissions_data == "end of submissions":
    contest_name, password, username, points = submissions_data.split("=>")

    if contest_name in contests and contests[contest_name] == password:
        if username not in candidates_info:
            candidates_info[username] = {}

        if contest_name not in candidates_info[username]:
            candidates_info[username][contest_name] = int(points)
        else:
            if int(points) > candidates_info[username][contest_name]:
                candidates_info[username][contest_name] = int(points)

    submissions_data = input()

best_candidate_points = 0
best_candidate = ""
for candidate, info in candidates_info.items():
    candidate_points = sum(info.values())
    if candidate_points >= best_candidate_points:
        best_candidate_points = candidate_points
        best_candidate = candidate

print(f"Best candidate is {best_candidate} with total {best_candidate_points} points.")
print("Ranking:")

candidates_info = dict(sorted(candidates_info.items(), key=lambda k: k[0]))

for candidate, info in candidates_info.items():
    print(candidate)
    info = dict(sorted(info.items(), key=lambda kvp: -kvp[1]))
    for contest, points in info.items():
        print(f"#  {contest} -> {points}")
print(candidates_info)