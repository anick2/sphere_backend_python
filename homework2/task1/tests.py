from task1 import CustomList
import unittest


class TestCustomList(unittest.TestCase):

    def test_add(self):

        l1 = CustomList([1, 2, 3])
        l2 = CustomList([2, 2, 8])
        self.assertEqual(list(l1 + l2), [3, 4, 11])
        self.assertEqual(isinstance(l1 + l2, CustomList), True)

        l1 = CustomList([1, -1, 2, 2])
        l2 = CustomList([2, 1])
        self.assertEqual(list(l1 + l2), [3, 0, 2, 2])
        self.assertEqual(isinstance(l1 + l2, CustomList), True)
        self.assertEqual(list(l1), [1, -1, 2, 2])
        self.assertEqual(list(l2), [2, 1])

        l1 = CustomList([1, 7])
        l2 = CustomList([2, 1, 3, 4])
        self.assertEqual(list(l1 + l2), [3, 8, 3, 4])
        self.assertEqual(isinstance(l1 + l2, CustomList), True)
        self.assertEqual(list(l1), [1, 7])
        self.assertEqual(list(l2), [2, 1, 3, 4])

        l1 = CustomList([1, 7])
        l2 = [1, 2, 3]
        self.assertEqual(list(l1 + l2), [2, 9, 3])
        self.assertEqual(isinstance(l1 + l2, CustomList), True)
        self.assertEqual(list(l1), [1, 7])

        l1 = CustomList([1, 3, -1])
        l2 = [1]
        self.assertEqual(list(l1 + l2), [2, 3, -1])
        self.assertEqual(isinstance(l1 + l2, CustomList), True)
        self.assertEqual(list(l1), [1, 3, -1])

        l1 = [-1, -1]
        l2 = CustomList([1, 3, -1])
        self.assertEqual(list(l1 + l2), [0, 2, -1])
        self.assertEqual(isinstance(l1 + l2, CustomList), True)
        self.assertEqual(list(l2), [1, 3, -1])

        l1 = [-1, 0, 3, 2]
        l2 = CustomList([1, 3])
        self.assertEqual(list(l1 + l2), [0, 3, 3, 2])
        self.assertEqual(isinstance(l1 + l2, CustomList), True)
        self.assertEqual(list(l2), [1, 3])

    def test_sub(self):

        l1 = CustomList([1, 2, 3])
        l2 = CustomList([2, 2, 8])
        self.assertEqual(list(l1 - l2), [-1, 0, -5])
        self.assertEqual(isinstance(l1 - l2, CustomList), True)

        l1 = CustomList([1, -1, 2, 2])
        l2 = CustomList([2, 1])
        self.assertEqual(list(l1 - l2), [-1, -2, 2, 2])
        self.assertEqual(isinstance(l1 - l2, CustomList), True)
        self.assertEqual(list(l1), [1, -1, 2, 2])
        self.assertEqual(list(l2), [2, 1])

        l1 = CustomList([1, 7])
        l2 = CustomList([2, 1, 3, 4])
        self.assertEqual(list(l1 - l2), [-1, 6, -3, -4])
        self.assertEqual(isinstance(l1 - l2, CustomList), True)
        self.assertEqual(list(l1), [1, 7])
        self.assertEqual(list(l2), [2, 1, 3, 4])

        l1 = CustomList([1, 7])
        l2 = [1, 2, 3]
        self.assertEqual(list(l1 - l2), [0, 5, -3])
        self.assertEqual(isinstance(l1 - l2, CustomList), True)
        self.assertEqual(list(l1), [1, 7])

        l1 = CustomList([1, 3, -1])
        l2 = [1]
        self.assertEqual(list(l1 - l2), [0, 3, -1])
        self.assertEqual(isinstance(l1 - l2, CustomList), True)
        self.assertEqual(list(l1), [1, 3, -1])

        l1 = [-1, -1]
        l2 = CustomList([1, 3, -1])
        self.assertEqual(list(l1 - l2), [-2, -4, 1])
        self.assertEqual(isinstance(l1 - l2, CustomList), True)
        self.assertEqual(list(l2), [1, 3, -1])

        l1 = [-1, 0, 3, 2]
        l2 = CustomList([1, 3])
        self.assertEqual(list(l1 - l2), [-2, -3, 3, 2])
        self.assertEqual(isinstance(l1 - l2, CustomList), True)
        self.assertEqual(list(l2), [1, 3])

    def test_comp(self):

        l1 = CustomList([1, 15])
        l2 = CustomList([-1, -2, -3, 5, 2])

        self.assertEqual(l1 < l2, False)
        self.assertEqual(l1 <= l2, False)
        self.assertEqual(l1 == l2, False)
        self.assertEqual(l1 > l2, True)
        self.assertEqual(l1 >= l2, True)

        l1 = CustomList([1, 2, -1, -1])
        l2 = CustomList([1, 1, 1])

        self.assertEqual(l1 < l2, True)
        self.assertEqual(l1 <= l2, True)
        self.assertEqual(l1 == l2, False)
        self.assertEqual(l1 > l2, False)
        self.assertEqual(l1 >= l2, False)

        l1 = CustomList([1, 2, 3, 10])
        l2 = CustomList([5, 17, -6])

        self.assertEqual(l1 < l2, False)
        self.assertEqual(l1 <= l2, True)
        self.assertEqual(l1 == l2, True)
        self.assertEqual(l1 > l2, False)
        self.assertEqual(l1 >= l2, True)
