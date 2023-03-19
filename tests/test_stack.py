import unittest
from src.stack import Stack, Node


class TestNode(unittest.TestCase):
    def test_init(self):
        node_5 = Node(5, None)
        self.assertIsInstance(node_5, Node)
        self.assertEqual(node_5.data, 5)
        self.assertIsNone(node_5.next_node)
        node_a = Node('a', node_5)
        self.assertEqual(node_a.next_node, node_5)


class TestStack(unittest.TestCase):
    def test_init(self):
        my_stack = Stack()
        self.assertIsInstance(my_stack, Stack)
        self.assertIsNone(my_stack.top)

    def test_push(self):
        my_stack = Stack()
        my_stack.push(5)
        self.assertIsInstance(my_stack.top, Node)
        self.assertEqual(my_stack.top.data, 5)
        self.assertIsNone(my_stack.top.next_node)
        my_stack.push('a')
        self.assertEqual(my_stack.top.data, 'a')
        self.assertEqual(my_stack.top.next_node.data, 5)
        self.assertIsNone(my_stack.top.next_node.next_node)


if __name__ == '__main__':
    unittest.main()
