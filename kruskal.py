"""
最小生成树 - 克鲁斯卡尔算法
构造连通网最小代价生成树

            B ———5———  C
        1/   \7        \ 8
        A     G  ——6——  D
        2\      \4    /3
          F ——9——— E

克鲁斯卡尔算法  直接找边, 构造树
"""
from union_find import QuickFind

INFINITY = 65535
VERTEXES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 邻接矩阵
EDGES = [  # 为了简化读取操作, 故 将 X 轴， Y轴 颠倒,即先读Y轴再度X轴  e.g.  a-c  EDGES[0][2] = INFINITY

    #      a(0)      b(1)       c(2)       d(3)       e(4)       f(5)       g(6)
    [       0,         1,  INFINITY,  INFINITY,  INFINITY,         2,  INFINITY],  # a(0)
    [       1,         0,         5,  INFINITY,  INFINITY,  INFINITY,         7],  # b(1)
    [INFINITY,         5,         0,         8,  INFINITY,  INFINITY,  INFINITY],  # c(2)
    [INFINITY,  INFINITY,         8,         0,         3,  INFINITY,         6],  # d(3)
    [INFINITY,  INFINITY,  INFINITY,         3,         0,         9,         4],  # e(4)
    [       2,  INFINITY,  INFINITY,  INFINITY,         9,         0,  INFINITY],  # f(5)
    [INFINITY,         7,  INFINITY,         6,         4,  INFINITY,         0],  # g(6)
]


class Edge:
    def __init__(self, begin, end, weight):
        self.begin = begin
        self.end = end
        self.weight = weight

    def __repr__(self):
        return f'edge: begin:{self.begin}-end:{self.end}-weight:{self.weight}'

    def __eq__(self, other):
        return other.begin == self.end and other.end == self.begin


def get_edges(edge_array):
    EDGE_LIST = []

    for x in range(len(edge_array)):
        row_x = edge_array[x]
        for y in range(len(row_x)):
            if edge_array[x][y] not in (0, INFINITY):
                edge = Edge(x, y, edge_array[x][y])
                if edge not in EDGE_LIST:
                    EDGE_LIST.append(edge)

    return sorted(EDGE_LIST, key=lambda x: x.weight)


class Graph:
    """邻接矩阵方式"""

    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def kruscal(self):
        tree = []
        sorted_edges = get_edges(self.edge_list)  # 根据边的权,从小到大排序
        uq = QuickFind(self.vertex_list)   # 转换节点,根据边来判断各个节点是否是同一组

        for edge in sorted_edges:
            begin = edge.begin
            end = edge.end
            if not uq.connected(begin, end):  # 判断边的两端是否在同一个连通图中
                uq.union(begin, end)
                tree.append(edge)

        for edge in tree:
            print(
                f'EDGE: begin:{edge.begin}({self.vertex_list[edge.begin]}) to {edge.end}({self.vertex_list[edge.end]})')

        return tree


if __name__ == '__main__':
    graph = Graph(VERTEXES, EDGES)
    graph.kruscal()
