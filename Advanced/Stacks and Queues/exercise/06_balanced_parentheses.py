parentheses = input()
parentheses_pairs = {"(": ")", "{": "}", "[": "]"}
opening_brackets_stack = []
balanced = True

for bracket in parentheses:
    if bracket in parentheses_pairs:
        opening_brackets_stack.append(bracket)
    else:
        if not opening_brackets_stack:
            balanced = False
            break
        else:
            if bracket != parentheses_pairs[opening_brackets_stack.pop()]:
                balanced = False
                break


if balanced and not opening_brackets_stack:
    print("YES")
else:
    print("NO")
