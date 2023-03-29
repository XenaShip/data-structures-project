import unittest
from src.queue import Queue, Node


class TestQueue(unittest.TestCase):
    def test_init(self):
        my_queue = Queue()
        assert my_queue.head is None

    def test_enqueue(self):
        my_queue = Queue()
        my_queue.enqueue(8)
        my_queue.enqueue(9)
        assert my_queue.tail.next_node is None
        assert my_queue.head.data == 8
        assert my_queue.head.next_node.data == 9

    def test_dequeue(self):
        my_queue = Queue()
        my_queue.enqueue(8)
        my_queue.enqueue(9)
        my_queue.enqueue(10)
        help_element = my_queue.dequeue()
        assert help_element == 8
        assert my_queue.head.data == 9

    if __name__ == '__main__':
        unittest.main()

