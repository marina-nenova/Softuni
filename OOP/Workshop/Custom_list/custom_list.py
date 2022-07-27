from copy import deepcopy

class CustomList:
    def __init__(self):
        self.__values = []

    def append(self, value):
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

