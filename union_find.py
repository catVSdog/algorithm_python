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
    """quick-find 算法
        在 relation列表中, 索引是节点的数字表示， 值是节点所属组
    """

    def __init__(self, node_list):
        self.relations = [node_list.index(i) for i in node_list]

    def __repr__(self):
        return self.relations

    @property
    def group_len(self):
        return len(set(self.relations))

    def find(self, target):
        return self.relations[target]

    def connected(self, a, b):
        a_group = self.find(a)
        b_group = self.find(b)

        if a_group != b_group:
            return False
        return True

    def union(self, a, b):
        a_group = self.find(a)
        b_group = self.find(b)

        if a_group == b_group:
            return

        for value in range(len(self.relations)):
            if self.relations[value] == a_group:
                self.relations[value] = b_group
