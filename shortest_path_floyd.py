"""
最短路径算法

弗洛伊德算法

            B ———5———  C
        1/   \7        \ 8
        A     G  ——6——  D
        2\      \4    /3
          F ——9——— E

"""
from copy import deepcopy

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


class Floyd:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def transformation(self):
        weight_array = deepcopy(self.edge_list)
        from_vertex_array = deepcopy(self.edge_list)

        for row in range(len(self.edge_list)):
            for col in range(len(self.edge_list[row])):
                from_vertex_array[row][col] = col
        return weight_array, from_vertex_array

    def calculate(self):
        weight_array, from_vertex = self.transformation()
        for middle in range(len(self.vertex_list)):
            for row in range(len(self.vertex_list)):
                for col in range(len(self.vertex_list)):
                    direct_connection_cost = weight_array[row][col]  # 例如 Ro - R2的距离
                    detour_connection_cost = weight_array[row][middle] + weight_array[middle][col]  # R0 - R1 - R2 的距离
                    if direct_connection_cost > detour_connection_cost:
                        weight_array[row][col] = weight_array[row][middle] + weight_array[middle][col]
                        from_vertex[row][col] = from_vertex[row][middle]

        return weight_array, from_vertex

    def process(self, begin, end):
        begin_index = self.vertex_list.index(begin)
        end_index = self.vertex_list.index(end)
        weight_array, from_vertex = self.calculate()

        begin_end_weight = weight_array[begin_index][end_index]

        path = str(begin_index) + self.find(begin_index, end_index, from_vertex, '')
        return begin_end_weight, path

    def find(self, begin, end, from_vertex, path):
        latest_vertex = from_vertex[begin][end]
        if latest_vertex == end:
            path += str(latest_vertex)
            return path
        else:
            path += str(latest_vertex)
            return self.find(latest_vertex, end, from_vertex, path)


if __name__ == '__main__':
    fy = Floyd(VERTEXES, EDGES)
    weight, path = fy.process('d', 'a')

    print(weight)
    print(f'path: {path}')
    """weight
    
           a0     b1    c2    d3   e4     f5    g6
       
    a0   [  0,    1,    6,   14,   11,    2,    8]
    b1   [  1,    0,    5,   13,   11,    3,    7]
    c2   [  6,    5,    0,    8,   11,    8,   12]
    d3   [ 14,   13,    8,    0,    3,   12,    6]
    e4   [ 11,   11,   11,    3,    0,    9,    4]
    f5   [  2,    3,    8,   12,    9,    0,   10]
    g6   [  8,    7,   12,    6,    4,   10,    0]
    
    """

    """  from_vertex
    
        a0     b1    c2    d3   e4     f5    g6
      
   a0  [ 0,    1,    1,    1,    5,    5,    1]    
   b1  [ 0,    1,    2,    2,    6,    0,    6]    
   c2  [ 1,    1,    2,    3,    3,    1,    1]    
   d3  [ 2,    2,    2,    3,    4,    4,    6]    
   e4  [ 5,    6,    3,    3,    4,    5,    6]    
   f5  [ 0,    0,    0,    4,    4,    5,    0]    
   g6  [ 1,    1,    1,    3,    4,    1,    6] 
      
    """
    """
    求a-d
    from_vertex[0][3] = 1
    from_vertex[1][3] = 2
    from_vertex[2][3] = 3
    所以路径是： 0,1,2,3
    
    """