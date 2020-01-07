"""
双向循环链表
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


class DoubleCircularLinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def get_node(self, position, reverse=False):
        if position < 1 or position > self._len:
            raise NodeNotExists('out of list')
        if position == 1:
            return self._head

        if reverse:
            return self._get_node_toward_head(position)
        else:
            return self._get_node_toward_tail(position)

    def _get_node_toward_tail(self, position):
        cursor = self._head
        i = 1

        while i < position:
            cursor = cursor._next
            i += 1
        return cursor

    def _get_node_toward_head(self, position):
        cursor = self._head
        i = 0
        while -(position) < i:
            cursor = cursor._prior
            i -= 1
        return cursor

    def append(self, data):
        node = Node(data)

        if self._head is None:
            self._head = node
        else:
            tail = self.get_node(self._len)
            tail._next = node
            node._prior = tail  # 建立双向链接

        self._len += 1  # 这里也是在 self._head 指向了节点以后就+1了
        node._next = self._head
        self._head._prior = node

    def prepend(self, data):
        node = Node(data)

        if self._head is None:
            self._head = node
        else:
            node._next = self._head
            self._head._prior = node  # 建立双向链接
            self._head = node  # 移动self._head 指针

        self._len += 1  # 先 +1  这样才能 get_node(1) 否则在添加第一个节点的时候, 就变成了 get_node(0),明显是不对的
        tail = self.get_node(self._len)
        tail._next = self._head
        self._head._prior = tail

    def scan_list(self, reverse=False):
        if reverse:
            self._scan_list_toward_head()
        else:
            self._scan_list_toward_tail()

    def _scan_list_toward_head(self):
        cursor = self._head
        while cursor is not None:
            print(cursor)
            cursor = cursor._prior

    def _scan_list_toward_tail(self):
        cursor = self._head
        while cursor is not None:
            print(cursor)
            cursor = cursor._next

    def insert(self, position, data):
        if position > self._len or position < 0:
            raise NodeNotExists('out of list')

        node = Node(data)
        if position == 1:
            tail = self._head._prior
            tail._next = node
            node._prior = tail
            node._next = self._head
            self._head._prior = node
            self._head = node
        else:
            cursor = self.get_node(position - 1)
            cursor._next._prior = node
            node._next = cursor._next
            cursor._next = node
            node._prior = cursor
        self._len += 1


if __name__ == '__main__':
    ss = DoubleCircularLinkedList()
    ss.append(1)
    ss.append(2)
    ss.append(3)
    ss.append(4)
    # ss.prepend(1)
    # ss.prepend(2)
    # ss.prepend(3)
    # ss.prepend(4)
    ss.insert(4, 100)

    ss.scan_list(False)
