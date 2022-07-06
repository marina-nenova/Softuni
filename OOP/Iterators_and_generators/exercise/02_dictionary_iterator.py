class dictionary_iter:
    def __init__(self, obj):
        self.obj = list(obj.items())
        self.i = 0
        self.end = len(obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            current_kvp = self.obj[self.i]
            self.i += 1
            return current_kvp
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
