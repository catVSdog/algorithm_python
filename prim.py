"""
最小生成树 - 普里姆算法
构造连通网最小代价生成树

            B ———5———  C
        1/   \7        \ 8
        A     G  ——6——  D
        2\      \4    /3
          F ——9——— E

普里姆算法, 以点找边, 构造生成树
"""
INFINITY = 65535
VERTEXES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 邻接矩阵
EDGES = [  # 为了简化读取操作, 故 将 X 轴， Y轴 颠倒,即先读Y轴再度X轴  e.g.  a-c  EDGES[0][2] = INFINITY

  #        a(0)      b(1)       c(2)       d(3)       e(4)       f(5)       g(6)
    [       0,         1,  INFINITY,  INFINITY,  INFINITY,         2,  INFINITY],  # a(0)
    [       1,         0,         5,  INFINITY,  INFINITY,  INFINITY,         7],  # b(1)
    [INFINITY,         5,         0,         8,  INFINITY,  INFINITY,  INFINITY],  # c(2)
    [INFINITY,  INFINITY,         8,         0,         3,  INFINITY,         6],  # d(3)
    [INFINITY,  INFINITY,  INFINITY,         3,         0,         9,         4],  # e(4)
    [       2,  INFINITY,  INFINITY,  INFINITY,         9,         0,  INFINITY],  # f(5)
    [INFINITY,         7,  INFINITY,         6,         4,  INFINITY,         0],  # g(6)
]


class Graph:
    """邻接矩阵方式"""
    visited_vertexes_cls = set()

    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def prim(self, begin_vertex):
        vertex_index = self.vertex_list.index(begin_vertex)
        tree_to_other_vertex_weight = self.edge_list[vertex_index]  # 此列表存的是 最小生成树所有节点距离图中其余各顶点的距离
        tree_to_other_vertex_begin_vertex = [vertex_index for i in range(len(self.vertex_list))]  # 此列表中存的是 出发点的索引

        for i in range(len(self.vertex_list) - 1):
            min = INFINITY
            j = 0
            k = vertex_index  # 出发点索引
            while j < len(tree_to_other_vertex_weight):
                if tree_to_other_vertex_weight[j] != 0 and tree_to_other_vertex_weight[j] < min:
                    min = tree_to_other_vertex_weight[j]
                    k = j
                j += 1
            print(
                f'EDGE: begin:{tree_to_other_vertex_begin_vertex[k]+1}({self.vertex_list[tree_to_other_vertex_begin_vertex[k]]})'
                f' to: {k+1}({self.vertex_list[k]})')
            tree_to_other_vertex_weight[k] = 0  # 将相应坐标置为0,表示这是树中节点.

            tem_row = self.edge_list[k]  # 根据新的出发点,更新树到图中各节点的距离
            for m in range(len(tem_row)):
                if tem_row[m] != 0 and tem_row[m] < tree_to_other_vertex_weight[m]:
                    tree_to_other_vertex_weight[m] = tem_row[m]
                    tree_to_other_vertex_begin_vertex[m] = k

        print(tree_to_other_vertex_weight)
        print(tree_to_other_vertex_begin_vertex)


if __name__ == '__main__':
    graph = Graph(VERTEXES, EDGES)
    graph.prim('g')











