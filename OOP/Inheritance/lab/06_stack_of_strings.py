class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


ll = Stack()
ll.push("a")
ll.push("b")
ll.push("c")
ll.push("d")
print(ll)
print(ll.top())
print(ll.pop())
print(ll.is_empty())
print(ll)