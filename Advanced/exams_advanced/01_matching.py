from collections import deque

males = [int(el) for el in input().split()]
females = deque(int(el) for el in input().split())
matches_count = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()

    if current_female <= 0 and current_male <= 0:
        continue
    if current_female <= 0:
        males.append(current_male)
        continue
    if current_male <= 0:
        females.appendleft(current_female)
        continue

    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue
    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_male != current_female:
        males.append(current_male - 2)
    else:
        matches_count += 1

print(f"Matches: {matches_count}")

if males:
    print(f"Males left: {', '.join([str(el) for el in reversed(males)])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")
