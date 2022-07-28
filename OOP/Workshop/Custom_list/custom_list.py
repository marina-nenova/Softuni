from copy import deepcopy


class CustomIntList:
    def __init__(self):
        self.__values = []

    def append(self, value):
        if not isinstance(value, int):
            raise ValueError("Only ints accepted")
        self.__values.append(value)
        return self.__values

    def remove(self, index):
        try:
            element = self.__values.pop(index)
            return element
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def get(self, index):
        try:
            el = self.__values[index]
            return el
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def extend(self, values):
        try:
            for el in values:
                if not isinstance(el, int):
                    raise ValueError("Only ints accepted")
            self.__values.extend(values)
            return deepcopy(self.__values)
        except TypeError:
            raise ValueError("Extend method works only with iterable objects")

    def insert(self, index, value):
        try:
            if index < 0 or index >= len(self.__values):
                raise IndexError
            self.__values.insert(index, value)
            return self.__values
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer")

    def pop(self):
        try:
            el = self.__values.pop()
            return el
        except IndexError:
            raise IndexError("No elements in list")

    def clear(self):
        self.__values.clear()

    def index_left(self, value):
        for index in range(len(self.__values)):
            el = self.__values[index]
            if el == value:
                return index
        raise ValueError("Value is not in list")

    def index_right(self, value):
        for index in range(len(self.__values) - 1, -1, -1):
            el = self.__values[index]
            if el == value:
                return index
        raise ValueError("Value is not in list")

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        if not isinstance(value, int):
            raise ValueError("Only ints accepted")
        self.__values.insert(0, value)

    def dictionize(self):
        result = {}
        for index in range(0, len(self.__values), 2):
            key = self.__values[index]
            val = self.__values[index + 1] if index < len(self.__values) - 1 else 0
            result[key] = val
        return result

    def move(self, amount):
        left_side = self.__values[:amount]
        right_side = self.__values[amount:]
        self.__values = right_side + left_side
        return self.__values

    def sum(self):
        return sum(self.__values)

    def overbound(self):
        return self.__values.index(max(self.__values))

    def underbound(self):
        return self.__values.index(min(self.__values))
