class sequence_repeat:
    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == self.number:
            raise StopIteration
        current_char = self.text[self.i % len(self.text)]
        self.i += 1
        return current_char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
