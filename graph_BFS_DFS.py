"""
图遍历

            b ——  c
          /  \  /  \
        a ——  g ——  d
        \    /  \  /
          f ———— e
"""
VERTEXES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
EDGES = [   # 由于pythn二维数组的限制,故 将 X 轴， Y轴 颠倒,即先读Y轴再度X轴
        # 故 a-c  EDGES[0][2] = -1
     #  a(0)    b(1)   c(2)   d(3)   e(4)   f(5)   g(6)
        [ 0,     1,    -1,     -1,    -1,      1,     1],   # a(0)
        [ 1,     0,     1,     -1,    -1,     -1,     1],   # b(1)
        [-1,     1,     0,      1,    -1,     -1,     1],   # c(2)
        [-1,    -1,     1,      0,     1,     -1,     1],   # d(3)
        [-1,    -1,    -1,      1,     0,      1,     1],   # e(4)
        [ 1,    -1,    -1,     -1,     1,      0,     1],   # f(5)
        [ 1,     1,     1,      1,     1,      1,     0],   # g(6)
]


class Graph:
    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def BFS(self, begin_vertex):
        """广度优先"""
        next_vertex_list = []
        visited_vertexes = set()
        finally_string = ''

        next_vertex_list.append(begin_vertex)

        while next_vertex_list:
            vertex = next_vertex_list.pop(0)

            if vertex in visited_vertexes:  # 如果该元素已经访问过, 略过
                continue
            finally_string += vertex

            visited_vertexes.add(vertex)
            vertex_index = self.vertex_list.index(vertex)
            row = self.edge_list[vertex_index]
            for v_index, v_value in enumerate(row):
                if v_value > 0:
                    adjacent_vertex = self.vertex_list[v_index]
                    if adjacent_vertex not in visited_vertexes:
                        next_vertex_list.append(adjacent_vertex)  # 此处会重复添加已经访问过得元素


        return finally_string

    def DFS(self, begin_vertex):
        """深度优先"""
        next_vertex_list = []
        visited_vertexes = set()
        finally_string = ''

        next_vertex_list.append(begin_vertex)

        while next_vertex_list:
            vertex = next_vertex_list.pop()

            if vertex in visited_vertexes:
                continue
            finally_string += vertex
            visited_vertexes.add(vertex)

            vertex_index = self.vertex_list.index(vertex)
            row = self.edge_list[vertex_index]

            for v_index, v_value in enumerate(row):
                adjacent_vertex = self.vertex_list[v_index]

                if v_value > 0 and adjacent_vertex not in visited_vertexes:
                    next_vertex_list.append(adjacent_vertex)
                    break  # 深度优先,只要找到一个相邻的顶点,那么就退出本循环,以相邻顶点开始继续查找下一个相邻顶点

        return finally_string





if __name__ == '__main__':
    graph = Graph(VERTEXES, EDGES)
    assert graph.BFS('a') == 'abfgced'
    assert graph.DFS('a') == 'abcdefg'