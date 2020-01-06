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

        cursor = self._head
        i = 1

        if position == i:
            return cursor

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
            tail = self.get_node(self._len)
            tail._next = node
        self._len += 1

    def prepend(self, data):
        """头部插入节点"""
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            node._next = self._head
            self._head = node
        self._len += 1

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
        return self._len == 0  # or return self._head is None

    def init_list(self, length, reverse=False):
        """创建一个特定长度的链表"""
        if length < 1:
            return self

        if reverse:
            return self.init_list_insert_head(length)

        return self.init_list_append_tail(length)

    def init_list_append_tail(self, length):
        """创建整个链表：尾插法"""
        self._head = tail = Node(None)
        self._len += 1

        for i in range(length - 1):
            new_node = Node(None)  # 将此处None改为 i,然后打印整个链表,就会发现尾插法创建的链表时顺序的
            tail._next = new_node  # 尾部节点的 _next 指向新节点
            tail = new_node  # 移动tail游标,始终指向最后一个节点
            self._len += 1
        return self

    def init_list_insert_head(self, length):
        """创建整个链表：头插法"""
        self._head = Node(None)
        self._len += 1

        for i in range(length - 1):
            new_node = Node(None)  # 将此处None改为 i,然后打印整个链表,就会发现头插法创建的链表时逆序的
            new_node._next = self._head  # 新节点的_next 指向第一个节点
            self._head = new_node  # 移动 self._head 指针, 使其指向新节点,即：把新节点作为第一个节点
            self._len += 1
        return self

    def get_head(self):
        return self._head

    def get_tail(self):
        return self.get_node(self._len)

    def scan_list(self):
        """遍历链表,遍历完所有元素就结束了"""
        cursor = self._head
        while cursor is not None:
            print(cursor)
            cursor = cursor._next


if __name__ == '__main__':
    s = SinglyLinkList()

    # ss = s.init_list(5)

    # print(f"length: {ss.length}")
    # print(s.get_node(1))
    # print(s.get_node(2))
    # print(s.get_node(3))
    # print(s.get_node(4))
    # print(s.get_node(5))
    # s.scan_list()

    # print("++ 插入一个元素 ++ ")
    # new_node = Node(100)
    # ss.insert_node(2, new_node)
    # print(s.get_node(1))
    # print(s.get_node(2))
    # print(s.get_node(3))
    # print(s.get_node(4))
    # print(s.get_node(5))
    # print(s.get_node(6))
    #
    # print("+++ 删除一个元素 +++")
    # ss.delete_node(1)
    # print(s.get_node(1))
    # print(s.get_node(2))
    # print(s.get_node(3))
    # print(s.get_node(4))
    # print(s.get_node(5))
    #
    # blank_list = SinglyLinkList()
    # blank_list.init_list(0)
    # print(blank_list)
    # print(blank_list.length)
    #
    #
    # print("获取不属于链表的节点")
    # print(ss.get_node(100))
    #

    # print("尾部追加节点")
    # list_a = SinglyLinkList()
    # list_a.append(1)
    # list_a.append(2)
    # list_a.append(3)
    # list_a.append(4)
    # print(list_a.length)
    # list_a.scan_list()

    print("头部部插入节点")
    list_b = SinglyLinkList()
    list_b.prepend(1)
    list_b.prepend(2)
    list_b.prepend(3)
    list_b.prepend(4)
    print(list_b.get_head())
    print(list_b.get_tail())
