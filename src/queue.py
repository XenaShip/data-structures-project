class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if (self.head is None) and (self.tail is None):
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            ans = self.head.data
            self.head = self.head.next_node
            return ans

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ''
        else:
            i = self.head
            ans = ''
            while not(i is None):
                if ans != '':
                    ans += '\n'
                ans += str(i.data)
                i = i.next_node
            return ans
