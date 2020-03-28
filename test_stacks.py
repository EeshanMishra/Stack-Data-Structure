import unittest
from stacks import *


class MyTest(unittest.TestCase):

    def test_stackarray(self):
        stack = StackArray()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(0)
        self.assertEqual(stack.peek(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 2)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        stack.push(3)
        self.assertEqual(stack.pop(), 3)

    def test_stacklinked(self):
        stack = StackLinked()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push(0)
        self.assertEqual(stack.peek(), 0)
        stack.push(1)
        self.assertEqual(stack.size(), 2)
        self.assertFalse(stack.is_empty())
        stack.push(3)
        self.assertEqual(stack.pop(), 3)


if __name__ == '__main__':
    unittest.main()
