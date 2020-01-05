"""
单向链表
链表整体不需要连续的地址空间,每个数据元素存储其下一个数据元素的位置
"""


class Node:  # 数据元素又称之为节点
    def __init__(self, data):
        self.data = data  # 每个节点含数据域，用于存储数据元素信息
        self._next = None  # 也包含一个指针域,指向直接后继位置的元素

    def __repr__(self):
        return f"{self.data}"


class NodeNotExists(Exception):
    pass


class SinglyLinkList:
    """单项链表类"""

    def __init__(self):
        self._head = None
        self._len = 0

    @property
    def length(self):
        return self._len

    def get_node(self, position):
        """查找节点"""
        if position < 1 or position > self._len:
            raise NodeNotExists("out of list")

        temp = self._head
        i = 1

        if position == i:
            return temp

        while i < position:
            temp = temp._next
            i += 1
        return temp

    def insert_node(self, position, data):
        """插入节点"""
        node = Node(data)
        if position == 1:
            node._next = self._head
            self._head = node
        else:
            target_node = self.get_node(position - 1)
            node._next = target_node._next
            target_node._next = node

        self._len += 1
        return self._len

    def delete_node(self, position):
        """删除节点"""
        if position == 1:
            self._head = self._head._next
        else:
            target_node = self.get_node(position - 1)
            target_node._next = target_node._next._next
        self._len -= 1
        return self._len

    def is_empty(self):
        """链表是否为空"""
        return self._len == 0

    def init_list(self, length, reverse=False):
        if reverse:
            return self.init_list_insert_head(length)

        else:
            return self.init_list_append_tail(length)

    def init_list_append_tail(self, length):
        """创建整个链表：尾插法"""
        first_init_node = Node(None)
        self._head = tail = first_init_node
        self._len += 1

        for i in range(length - 1):
            temp = Node(None)  # 将此处None改为 i,然后打印整个链表,就会发现尾插法创建的链表时顺序的
            tail._next = temp
            tail = temp  # 移动tail游标,始终指向最后一个节点
            self._len += 1
        return self

    def init_list_insert_head(self, length):
        """创建整个链表：头插法"""
        first_init_node = Node(None)
        self._head = first_init_node
        self._len += 1

        for i in range(length - 1):
            temp = Node(None)  # 将此处None改为 i,然后打印整个链表,就会发现头插法创建的链表时逆序的
            temp._next = self._head
            self._head = temp  # head始终指向第一个节点
            self._len += 1
        return self


if __name__ == '__main__':
    s = SinglyLinkList()
    ss = s.init_list(5, True)

    print(f"length: {ss.length}")
    print(s.get_node(1))
    print(s.get_node(2))
    print(s.get_node(3))
    print(s.get_node(4))
    print(s.get_node(5))

    print("++ 插入一个元素 ++ ")
    new_node = Node(100)
    ss.insert_node(2, new_node)
    print(s.get_node(1))
    print(s.get_node(2))
    print(s.get_node(3))
    print(s.get_node(4))
    print(s.get_node(5))
    print(s.get_node(6))

    print("+++ 删除一个元素 +++")
    ss.delete_node(1)
    print(s.get_node(1))
    print(s.get_node(2))
    print(s.get_node(3))
    print(s.get_node(4))
    print(s.get_node(5))

    print("获取不属于链表的节点")
    print(ss.get_node(100))
