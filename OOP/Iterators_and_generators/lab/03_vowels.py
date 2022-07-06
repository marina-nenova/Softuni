class vowels:
    def __init__(self, string):
        self.string = string
        self.i = 0
        self.end = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            current = self.string[self.i]
            self.i += 1
            if current.lower() in "aeiouy":
                return current
        else:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
