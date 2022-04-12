version = [int(num) for num in input().split(".")]

for index in range(len(version) - 1, -1, -1):
    version[index] = version[index] + 1
    if version[index] < 10:
        print(*version, sep=".")
        break
    else:
        version[index] = 0
