resource = input()
resources = {}

while not resource == "stop":
    quantity = int(input())
    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity
    resource = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
