import unittest
from task2 import CustomMeta


class TestCustomMeta(unittest.TestCase):

    def setUp(self):

        class C(metaclass=CustomMeta):
            a = [1, 2, 3]
            tape = 100

            def func(self):
                return "Hello"

        class Vehicle(metaclass=CustomMeta):

            doors = 4

            def __eq__(self, other):
                return "Hi from __eq__"

            def brake(self):
                return "Braking"

            def drive(self):
                return "I'm driving!"

        self.c = C()
        self.v1 = Vehicle()
        self.v2 = Vehicle()

    def test_meta(self):

        self.assertEqual(self.c.custom_a, [1, 2, 3])
        self.assertEqual(self.c.custom_tape, 100)
        self.assertEqual(self.c.custom_func(), "Hello")

        self.assertRaises(AttributeError, getattr, self.c, "a")
        self.assertRaises(AttributeError, getattr, self.c, "tape")
        self.assertRaises(AttributeError, getattr, self.c, "f")

        self.assertEqual(self.v1.custom_doors, 4)
        self.assertEqual(self.v1.custom_brake(), "Braking")
        self.assertEqual(self.v2.custom_drive(), "I'm driving!")
        self.assertEqual(self.v1.__eq__(self.v2), "Hi from __eq__")

        self.assertRaises(AttributeError, getattr, self.v1, "doors")
        self.assertRaises(AttributeError, getattr, self.v1, "brake")
        self.assertRaises(AttributeError, getattr, self.v1, "drive")
        self.assertRaises(AttributeError, getattr, self.v1, "custom___eq__")
