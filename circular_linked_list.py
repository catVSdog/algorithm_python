"""
循环链表
关键之最后一个节点的 next 指针指向第一个节点
连接两个循环链表,也是通过修改两个链表的头尾节点的指针实现
"""
from copy import deepcopy


class Node:
    def __init__(self, data):
        self.data = data
        self._next = None

    def __repr__(self):
        return f"{self.data}"


class NodeNotExists(Exception):
    pass


class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def get_node(self, position):
        if position < 1 or position > self._len:
            raise NodeNotExists("out of list")

        i = 1
        p = self._head

        if position == i:
            return p

        while i < position:
            p = p._next
            i += 1
        return p

    @property
    def length(self):
        return self._len

    def init_list(self, length, reverse=False):
        if length < 1:
            return self
        if reverse:
            return self.init_list_insert_head(length)

        return self.init_list_append_tail(length)

    def init_list_append_tail(self, length):
        """尾插法"""
        self._head = tail = Node(None)
        self._len += 1

        for i in range(length - 1):
            new_node = Node(i)  # 创建一个新节点
            tail._next = new_node  # 尾部节点的 _next 指向新节点
            tail = new_node  # 移动游标,使游标指向新节点
            self._len += 1
        tail._next = self._head  # 循环链表的关键,最后一个节点的 _next 指向 第一个节点
        return self

    def init_list_insert_head(self, length):
        """头插法"""
        self._head = tail = Node(None)
        self._len += 1

        for i in range(length - 1):
            new_node = Node(i)  # 创建一个新节点
            new_node._next = self._head  # 新节点的　_next 指向第一个节点
            self._head = new_node  # 移动 self._head 指针, 使其指向新节点,即：把新节点作为第一个节点
            self._len += 1
        tail._next = self._head  # 循环链表的关键,最后一个节点的 _next 指向 第一个节点
        return self

    def scan_list(self):
        """遍历链表,因为是循环链表,故永不会停止"""
        cursor = self._head
        while cursor is not None:
            print(cursor)
            cursor = cursor._next

    def get_head(self):
        return self._head

    def get_tail(self):
        return self.get_node(self._len)

    def concact(self, another_list):  # 连接两个循环链表
        list_b = deepcopy(another_list)
        first_list_head = self.get_head()
        first_list_tail = self.get_tail()
        last_list_head = list_b.get_head()
        last_list_tail = list_b.get_tail()
        first_list_tail._next = last_list_head  # 前一个链表的最后一个节点的指针指向后一个链表的第一个节点
        last_list_tail._next = first_list_head  # 后一个链表的最后一个节点指向前一个链表的第一个节点
        return self

    def append(self, data):
        """尾部追加节点"""
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            tail = self.get_node(self._len)
            tail._next = node
        self._len += 1
        node._next = self._head  # 每次添加一个节点,都要将新节点指向第一个节点

    def prepend(self, data):
        """头部插入节点"""
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            node._next = self._head
            self._head = node

        self._len += 1
        last_node = self.get_node(self._len)
        last_node._next = self._head  # 每次添加一个节点,都要将最后节点指向新的第一个节点


if __name__ == '__main__':
    s = CircularLinkedList()
    ss = s.init_list(5, True)

    # ss.scan_list()

    # c_a = CircularLinkedList()
    # init_a = c_a.init_list(0)
    # init_a.append(1)
    # init_a.append(2)
    # init_a.append(3)
    #
    # c_b = CircularLinkedList()
    # init_b = c_b.init_list(0)
    # init_b.append(4)
    # init_b.append(5)
    # init_b.append(6)

    # print("尾部追加节点")
    # list_a = CircularLinkedList()
    # list_a.append(1)
    # list_a.append(2)
    # list_a.append(3)
    # list_a.append(4)
    # list_a.scan_list()

    print("头部部插入节点")
    list_b = CircularLinkedList()
    list_b.prepend(1)
    list_b.prepend(2)
    list_b.prepend(3)
    list_b.prepend(4)
    print(list_b.get_head())
    print(list_b.get_tail())
