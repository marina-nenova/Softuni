n = int(input())
guest_list = set()

for _ in range(n):
    reservation_code = input()
    guest_list.add(reservation_code)

guest = input()

while not guest == "END":
    guest_list.discard(guest)
    guest = input()

print(len(guest_list))
print(*sorted(guest_list), sep="\n")
