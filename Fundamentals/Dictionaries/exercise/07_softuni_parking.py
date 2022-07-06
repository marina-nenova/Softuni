n = int(input())
users_info = {}

for _ in range(n):
    data = input().split()
    action = data[0]
    username = data[1]
    if action == "register":
        license_plate = data[2]
        if username not in users_info:
            users_info[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {users_info[username]}")
    elif action == "unregister":
        if username in users_info:
            del users_info[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate in users_info.items():
    print(f"{username} => {license_plate}")
    