from collections import deque

bullet_price = int(input())
gun_barrel_capacity = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())
total_bullets_used = 0
bullets_count = 0

while locks and bullets:
    current_bullet = bullets.pop()
    total_bullets_used += 1
    bullets_count += 1
    if current_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    if bullets_count == gun_barrel_capacity and bullets:
        print("Reloading!")
        bullets_count = 0


if not locks:
    money_earned = intelligence_value - (total_bullets_used * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
elif not bullets:
    print(f"Couldn't get through. Locks left: {len(locks)}")
