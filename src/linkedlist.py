class Node:
    def __init__(self, num=None):
        self.num = num
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            if self.tail is None:
                self.tail = self.head
        else:
            last = self.head
            while not(last.next is None):
                last = last.next
            last.next = new

    def insert_beginning(self, value):
        new = Node(value)
        if self.tail is None:
            self.tail = new
            if self.head is None:
                self.head = self.tail
            return
        first = self.tail
        self.tail = new
        self.tail.next = first

    def __str__(self):
        ans = ''
        ptr = self.tail
        while ptr is not None:
            ans += str(ptr.num)
            ans += ' -> '
            ptr = ptr.next
        ans += 'None'
        return ans

    def to_list(self):
        i = self.tail
        ans = []
        while not(i is None):
            ans.append(i.num)
            i = i.next
        return ans

    def get_data_by_id(self, value):
        thelist = self.to_list()
        for i in thelist:
            try:
                if i['id'] == value:
                    return i
            except TypeError as e:
                print('Данные не являются словарем или в словаре нет id.')

