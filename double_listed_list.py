"""
双向链表
每个节点除了数据域,都还各有两个指针域,分别指向前一个节点和后一个节点
"""


class Node:
    def __init__(self, data):
        self._prior = None
        self.data = data
        self._next = None

    def __repr__(self):
        return f"{self.data}"


class NodeNotExists(Exception):
    pass


class DoubleLinkedList:

    def __init__(self):
        self._head = None
        self._len = 0

    @property
    def length(self):
        return self._len

    def get_node(self, position):
        cursor = self._head
        i = 1
        if position == i:
            return cursor
        else:
            while i < position:
                cursor = cursor._next
                i += 1
            return cursor

    def append(self, data):
        """尾部追加节点"""
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            last_node = self.get_node(self._len)
            last_node._next = node
            node._prior = last_node
        self._len += 1

    def prepend(self, data):
        """头部插入节点"""
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            node._next = self._head
            self._head._prior = node
            self._head = node
        self._len += 1

    def scan_list(self, reverse=False):
        if reverse:
            self._scan_list_toward_head()
        else:
            self._scan_list_toward_tail()

    def _scan_list_toward_tail(self):
        """朝尾部遍历节点"""
        cursor = self._head
        while cursor is not None:
            print(cursor)
            cursor = cursor._next

    def _scan_list_toward_head(self):
        cursor = self.get_node(self._len)
        while cursor is not None:
            print(cursor)
            cursor = cursor._prior


if __name__ == '__main__':
    s_a = DoubleLinkedList()
    # s_a.prepend(1)
    # s_a.prepend(2)
    # s_a.prepend(3)
    # s_a.prepend(4)
    # print(s_a.length)
    # s_a.scan_list(True)

    s_a.append(100)
    s_a.append(101)
    s_a.append(102)
    s_a.append(103)
    s_a.scan_list()
