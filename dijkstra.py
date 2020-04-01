"""
最短路径算法

迪杰斯特拉算法

            B ———5———  C
        1/   \7        \ 8
        A     G  ——6——  D
        2\      \4    /3
          F ——9——— E

"""

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


class Dijkstra:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def process(self, begin, end):
        begin_index = self.vertex_list.index(begin)
        visited = [False for i in self.vertex_list]  # 记录访问过的节点,初始均为False,表示没有访问过
        vertex_from = [begin_index for i in self.vertex_list]  # 记录每段路径的起始点, 起始值为begin所在的节点索引
        vertex_weight = self.edge_list[begin_index]  # 记录起始节点到每一个节点的最短路径,初始为begin节点到图中各个顶点的距离

        visited[begin_index] = True  # 初始化,从begin节点开始, 表示已经访问过
        vertex_weight[begin_index] = 0  # 初始化,从节点到节点的距离是 0

        for i in range(len(self.vertex_list)):
            # 寻找距离 begin 最近的节点
            cost_min = INFINITY

            for vertex_index in range(len(self.vertex_list)):
                if not visited[vertex_index] and vertex_weight[vertex_index] < cost_min:
                    nearest_index = vertex_index
                    cost_min = vertex_weight[vertex_index]

            visited[nearest_index] = True

            for vertex_index in range(len(self.vertex_list)):
                direct_connection_cost = vertex_weight[vertex_index]  # 例如 Ro 直接到 R2的距离
                detour_connection_cost = self.edge_list[nearest_index][vertex_index] + cost_min  # R0 - R1 - R2 的距离
                if not visited[vertex_index] and direct_connection_cost > detour_connection_cost:
                    vertex_weight[vertex_index] = detour_connection_cost
                    vertex_from[vertex_index] = nearest_index

        print(f'vertex_from: {vertex_from}')
        print(f'vertex_weight: {vertex_weight}')

        end_index = self.vertex_list.index(end)
        begin_end_cost = vertex_weight[end_index]

        def find(x):
            path = ' '
            if vertex_from[x] == begin_index:
                path += str(begin_index)
                return path
            else:
                path += str(vertex_from[x])
                path += find(vertex_from[x])
                return path

        path_rev = find(end_index)
        flow_path = path_rev[::-1] + f'{end_index}'

        return flow_path, begin_end_cost


if __name__ == '__main__':
    dj = Dijkstra(VERTEXES, EDGES)
    path, cost = dj.process('d', 'a')
    print(f'path:{path}')
    print(f'cost: {cost}')
