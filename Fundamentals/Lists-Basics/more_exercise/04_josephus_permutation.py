people = [int(el) for el in input().split()]
step = int(input())
index = step - 1
executions = []
while len(people) > 0:
    if index > len(people) - 1:
        index = index - len(people)
        continue
    executions.append(people.pop(index))
    index += step - 1

print(str(executions).replace(" ", ""))
