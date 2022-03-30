persons = int(input())
capacity = int(input())

courses = persons // capacity
left = persons % capacity
if left > 0:
    courses += 1

print(courses)

