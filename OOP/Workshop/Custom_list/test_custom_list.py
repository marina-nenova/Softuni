from unittest import TestCase, main
from Custom_list.custom_list import CustomIntList

CUSTOM_INDEX_ERROR_MESSAGE = "Invalid index"
CUSTOM_INVALID_INTEGER_MESSAGE = "Index is not a valid integer"
CUSTOM_EMPTY_LIST_MESSAGE = "No elements in list"
CUSTOM_VALUE_ERROR = "Value is not in list"
CUSTOM_INT_VALUE_ERROR_MESSAGE = "Only ints accepted"


class CustomListTest(TestCase):
    def setUp(self) -> None:
        self.custom_list = CustomIntList()

    def test_append_adds_element_at_end_of_list(self):
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        result = self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)
        self.assertEqual([5], result)

    def test_append_non_int_value_raises(self):
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.append(5.5)
        self.assertEqual(CUSTOM_INT_VALUE_ERROR_MESSAGE, str(ex.exception))

    def test_remove_removes_el_invalid_index_raises(self):
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(IndexError) as ex:
            self.custom_list.remove(1)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_remove_pass_invalid_integer_raises(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.remove("0")
        self.assertEqual(CUSTOM_INVALID_INTEGER_MESSAGE, str(ex.exception))

    def test_remove_index_removes_and_returns_element(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)
        returned_element = self.custom_list.remove(0)
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        self.assertEqual(5, returned_element)

    def test_get_returns_element(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)

        el = self.custom_list.get(0)
        self.assertEqual(5, el)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)

    def test_get_invalid_index_raises(self):
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(IndexError) as ex:
            self.custom_list.get(1)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_get_invalid_integer_raises(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.get("0")
        self.assertEqual(CUSTOM_INVALID_INTEGER_MESSAGE, str(ex.exception))

    def test_extend_appends_new_values_to_end_of_list(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)

        self.custom_list.extend([2, 3, 4])
        self.assertListEqual([5, 2, 3, 4], self.custom_list._CustomIntList__values)

    def test_extend_with_noniterable_raises(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)

        with self.assertRaises(ValueError) as ex:
            self.custom_list.extend(15)
        self.assertEqual("Extend method works only with iterable objects", str(ex.exception))

    def test_extend_non_int_value_in_iterable_raises(self):
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.extend(["i", 5.5])
        self.assertEqual(CUSTOM_INT_VALUE_ERROR_MESSAGE, str(ex.exception))

    def test_extend_returns_new_list(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)
        result = self.custom_list.extend([2, 3, 4])
        self.assertListEqual([5, 2, 3, 4], self.custom_list._CustomIntList__values)
        self.assertNotEqual(id(result), id(self.custom_list._CustomIntList__values))
        self.assertEqual([5, 2, 3, 4], result)

    def test_insert_places_value_at_index(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)
        result = self.custom_list.insert(0, 1)
        self.assertEqual([1, 5], self.custom_list._CustomIntList__values)
        self.assertEqual([1, 5], result)

    def test_insert_invalid_integer_index_raises(self):
        self.custom_list.append(5)
        self.assertListEqual([5], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.insert("2", 1)
        self.assertEqual(CUSTOM_INVALID_INTEGER_MESSAGE, str(ex.exception))

    def test_insert_invalid_index_raises(self):
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(IndexError) as ex:
            self.custom_list.insert(2, 1)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(ex.exception))

    def test_pop_removes_last_element_and_returns_it(self):
        self.custom_list.extend([5, 2, 3, 4])
        self.assertListEqual([5, 2, 3, 4], self.custom_list._CustomIntList__values)
        result = self.custom_list.pop()
        self.assertEqual(4, result)
        self.assertListEqual([5, 2, 3], self.custom_list._CustomIntList__values)

    def test_pop_if_list_is_empty_raises(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        with self.assertRaises(IndexError) as ex:
            self.custom_list.pop()
        self.assertEqual(CUSTOM_EMPTY_LIST_MESSAGE, str(ex.exception))

    def test_clear_no_elements_returns_empty_list(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomIntList__values)

    def test_clear_empties_the_list(self):
        self.custom_list.extend([5, 2, 3, 4])
        self.assertListEqual([5, 2, 3, 4], self.custom_list._CustomIntList__values)
        self.custom_list.clear()
        self.assertListEqual([], self.custom_list._CustomIntList__values)

    def test_index_left_if_value_in_list_returns_left_most_index(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        result = self.custom_list.index_left(2)
        self.assertEqual(1, result)

    def test_index_right_if_value_in_list_returns_right_most_index(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        result = self.custom_list.index_right(2)
        self.assertEqual(2, result)

    def test_index_left_if_value_not_in_list_raises(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.index_left(3)
        self.assertEqual(CUSTOM_VALUE_ERROR, str(ex.exception))

    def test_index_right_if_value_not_in_list_raises(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        with self.assertRaises(ValueError) as ex:
            self.custom_list.index_right(3)
        self.assertEqual(CUSTOM_VALUE_ERROR, str(ex.exception))

    def test_count_returns_count_of_element_in_list(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        result = self.custom_list.count(2)
        self.assertEqual(2, result)

    def test_count_if_element_not_in_list_returns_zero(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        result = self.custom_list.count(3)
        self.assertEqual(0, result)

    def test_reverse_reverses_the_values_in_the_list(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        reversed = self.custom_list.reverse()
        self.assertEqual([4, 2, 2, 5], reversed)
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)

    def test_reverse_empty_list_returns_empty_list(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        reversed = self.custom_list.reverse()
        self.assertEqual([], reversed)

    def test_copy_returns_same_elements_different_list(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)

        result = self.custom_list.copy()
        self.assertEqual([5, 2, 2, 4], result)
        self.assertNotEqual(id(result), id(self.custom_list._CustomIntList__values))

    def test_size_returns_elements_count(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        result = self.custom_list.size()
        self.assertEqual(0, result)

        self.custom_list.extend([5, 2, 2, 4])
        self.assertListEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        result = self.custom_list.size()
        self.assertEqual(4, result)

    def test_add_first_adds_element_at_beginning_of_list(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        self.custom_list.add_first(3)
        self.assertEqual([3, 5, 2, 2, 4], self.custom_list._CustomIntList__values)

    def test_add_first_no_elements_append(self):
        self.assertEqual([], self.custom_list._CustomIntList__values)
        self.custom_list.add_first(3)
        self.assertEqual([3], self.custom_list._CustomIntList__values)

    def test_add_first_non_int_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.add_first("3")
        self.assertEqual(CUSTOM_INT_VALUE_ERROR_MESSAGE, str(ex.exception))

    def test_dictionize_with_empty_list_returns_empty_dict(self):
        self.assertListEqual([], self.custom_list._CustomIntList__values)
        result = self.custom_list.dictionize()
        self.assertEqual({}, result)

    def test_dictionize_with_even_len_list_returns_correct_dict(self):
        self.custom_list.extend([5, 2, 2, 4])
        self.assertEqual([5, 2, 2, 4], self.custom_list._CustomIntList__values)
        result = self.custom_list.dictionize()
        self.assertEqual({5: 2, 2: 4}, result)

    def test_dictionize_with_odd_len_list_returns_correct_dict(self):
        self.custom_list.extend([5, 2, 2, 4, 3])
        self.assertEqual([5, 2, 2, 4, 3], self.custom_list._CustomIntList__values)
        result = self.custom_list.dictionize()
        self.assertEqual({5: 2, 2: 4, 3: 0}, result)

    def test_move_moves_first_count_el_to_end_of_list(self):
        self.custom_list.extend([5, 2, 2, 4, 3])
        self.assertEqual([5, 2, 2, 4, 3], self.custom_list._CustomIntList__values)
        result = self.custom_list.move(2)
        self.assertEqual([2, 4, 3, 5, 2], result)
        self.assertEqual([2, 4, 3, 5, 2], self.custom_list._CustomIntList__values)

    def test_sum_returns_sum_of_elements_in_list(self):
        self.custom_list.extend([5, 2, 2, 4, 3])
        self.assertEqual([5, 2, 2, 4, 3], self.custom_list._CustomIntList__values)
        result = self.custom_list.sum()
        self.assertEqual(16, result)

    def test_overbound_returns_index_of_max_num(self):
        self.custom_list.extend([5, 2, 2, 4, 3])
        self.assertEqual([5, 2, 2, 4, 3], self.custom_list._CustomIntList__values)
        result = self.custom_list.overbound()
        self.assertEqual(0, result)

    def test_underbound_returns_index_of_min_num(self):
        self.custom_list.extend([5, 2, 2, 4, 3])
        self.assertEqual([5, 2, 2, 4, 3], self.custom_list._CustomIntList__values)
        result = self.custom_list.underbound()
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
