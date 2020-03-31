"""
并查集
主要解决动态连通性的问题
"""
from abc import abstractmethod


class BaseUnionFind:
    @abstractmethod
    def find(self, target):
        pass

    @abstractmethod
    def connected(self, a, b):
        pass

    @abstractmethod
    def union(self, a, b):
        pass


class QuickFind(BaseUnionFind):
    """
    quick-find 算法
    在 relations 列表中, 索引是节点的数字表示， 值是节点所属组
    """

    def __init__(self, node_list):
        self.relations = [node_list.index(i) for i in node_list]

    def __repr__(self):
        return f'{self.relations}'

    @property
    def group_len(self):
        return len(set(self.relations))

    def find(self, target):
        return self.relations[target]

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        a_group = self.find(a)
        b_group = self.find(b)

        if a_group == b_group:
            return

        for value in range(len(self.relations)):
            if self.relations[value] == a_group:
                self.relations[value] = b_group


class QuickUnion(BaseUnionFind):
    """
    quick-union 算法
    在 relations 中, 索引是节点的数字表示,值是其父节点.
    根节点的父节点是其自身
    """

    def __init__(self, node_list):
        self.relations = [node_list.index(i) for i in node_list]

    def __repr__(self):
        return f'{self.relations}'

    def find(self, target):
        if self.relations[target] == target:
            return target
        else:
            return self.find(self.relations[target])  # 只指向父节点,容易形成一条长指向链

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)

        if a_parent == b_parent:
            return
        self.relations[a_parent] = b_parent


class QuickUnionCompressPath(BaseUnionFind):
    """
    quick-union 路径压缩
    在 relations 中, 索引是节点的数字表示,值是其 根节点.
    根节点的根节点是其自身
    """

    def __init__(self, node_list):
        self.relations = [node_list.index(i) for i in node_list]

    def __repr__(self):
        return f'{self.relations}'

    def find(self, target):
        if self.relations[target] == target:
            return target
        else:
            self.relations[target] = self.find(self.relations[target])  # 递归的指向根节点
            return self.relations[target]

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return
        self.relations[a_root] = b_root


if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd', 'e']
    q = QuickUnionCompressPath(a)
    q.union(0, 1)
    q.union(0, 2)
    q.union(0, 3)
    assert q.connected(0, 1) is True
    assert q.connected(0, 4) is False
