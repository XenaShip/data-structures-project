import unittest
from src.linkedlist import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    def test_init_node(self):
        my_node = Node(3)
        assert my_node.num == 3
        assert my_node.next is None

    def test_init_list(self):
        my_list = LinkedList()
        assert my_list.head is None
        assert my_list.tail is None

    def test_insert_at_end_and_beginning(self):
        my_list = LinkedList()
        my_list.insert_beginning(1)
        my_list.insert_at_end(2)
        my_list.insert_at_end(3)
        my_list.insert_beginning(0)
        assert my_list.tail.num == 0


    def test_to_list(self):
        my_list = LinkedList()
        my_list.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        my_list.insert_at_end({'id': 2, 'username': 'mik.roz'})
        lst = my_list.to_list()
        self.assertEqual(lst, [{'id': 1, 'username': 'lazzy508509'}, {'id': 2, 'username': 'mik.roz'}])

    def test_get_data_by_id(self):
        my_list = LinkedList()
        my_list.insert_at_end('idusername')
        my_list.insert_at_end({'id': 2, 'username': 'mosh_s'})
        user_data = my_list.get_data_by_id(2)
        assert 'Данные не являются словарем или в словаре нет id.'
        self.assertEqual(user_data, {'id': 2, 'username': 'mosh_s'})