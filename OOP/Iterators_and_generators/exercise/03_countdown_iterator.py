class countdown_iterator:
    def __init__(self, number):
        self.number = number
        self.i = number
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.end:
            current = self.i
            self.i -= 1
            return current
        else:
            raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
