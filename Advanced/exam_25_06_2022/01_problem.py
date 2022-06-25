from collections import deque

eggs = deque([int(el) for el in input().split(", ")])
paper_sizes = deque([int(el) for el in input().split(", ")])
box_size = 50
filled_boxes = 0

while eggs and paper_sizes:
    current_egg = eggs.popleft()
    current_paper = paper_sizes.pop()

    if current_egg <= 0:
        paper_sizes.append(current_paper)
        continue

    if current_egg == 13:
        paper_sizes.append(paper_sizes.popleft())
        paper_sizes.appendleft(current_paper)
        continue

    current_sum = current_egg + current_paper

    if current_sum <= box_size:
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(str(el) for el in eggs)}')
if paper_sizes:
    print(f'Pieces of paper left: {", ".join(str(el) for el in paper_sizes)}')