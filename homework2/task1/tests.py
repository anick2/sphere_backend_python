from task1 import CustomList
import unittest

class TestCustomList(unittest.TestCase):

    def test_add(self):

        self.assertEqual(CustomList([1,2,3]) + CustomList([2,2,8]), [3,4,11])
        self.assertEqual(list(CustomList([1, -1, 2, 2]) + CustomList([2,1])), [3,0,2,2])
