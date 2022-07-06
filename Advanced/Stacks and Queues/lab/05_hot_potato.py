from collections import deque

kids = deque(input().split())
n = int(input())

while len(kids) > 1:
    kids.rotate(-(n-1))
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")