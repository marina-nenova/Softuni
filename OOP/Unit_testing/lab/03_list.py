class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main

class IntegerListTests(TestCase):
    def test_integer_list_is_initialized_correctly_with_valid_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

    def test_integer_list_is_initialized_correctly_with_no_data(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_integer_list_is_initialized_correctly_with_invalid_data(self):
        integer = IntegerList(5, "5")
        self.assertEqual([5], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5)
        result = integer.get_data()
        self.assertEqual([5], result)

    def test_add_invalid_element_to_list_raises(self):
        integer = IntegerList(5)

        with self.assertRaises(ValueError) as ex:
            integer.add("5")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_valid_element_to_list(self):
        integer = IntegerList(5)
        integer.add(10)
        self.assertEqual([5, 10], integer.get_data())

    def test_remove_index_with_index_bigger_or_equal_to_list_length(self):
        integer = IntegerList(5, 10)

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))


    def test_remove_index_with_valid_data(self):
        integer = IntegerList(5, 10)
        integer.remove_index(1)
        self.assertEqual([5], integer.get_data())

    def test_remove_index_returns_removed_el(self):
        integer = IntegerList(5, 10)
        self.assertEqual(10, integer.remove_index(1))

    def test_get_method_with_invalid_index_raises(self):
        integer = IntegerList(5, 10)

        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method_with_valid_index(self):
        integer = IntegerList(5, 10)
        self.assertEqual(5, integer.get(0))

    def test_insert_element_on_an_invalid_index_raises(self):
        integer = IntegerList(5, 10)

        with self.assertRaises(IndexError) as ex:
            integer.insert(3, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_element_on_an_invalid_element_type_raises(self):
        integer = IntegerList(5, 10)

        with self.assertRaises(ValueError) as ex:
            integer.insert(1, '5')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_valid_element_on_valid_index(self):
        integer = IntegerList(5, 10)
        integer.insert(0, 6)
        self.assertEqual([6, 5, 10], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(-365, 37, 5, 10, 90, 100)
        result = integer.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        integer = IntegerList(5, 10)
        result = integer.get_index(5)
        self.assertEqual(0, result)


if __name__ == "__main__":
    main()