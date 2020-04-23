"""
树-孩子表示法
"""


class Node:
    def __init__(self, name):
        self._name = name  # e.g. '张三'
        self._children = set()  # e.g. [1, 2, 3, 4]

    def add_child_index(self, child_index):
        self._children.add(child_index)

    @property
    def name(self):
        return self._name

    @property
    def children(self):
        return self._children

    @property
    def has_children(self):
        return len(self._children) > 0


class Tree:
    def __init__(self):
        self.root = Node('root')
        self._nodes = [self.root]
        self.node_name_index_map = {'root': 0}  # e.g. {'root': 0, '女装': 1}

    def get_node_index_by_name(self, name):
        return self.node_name_index_map.get(name, -1)

    def append(self, node):
        self._nodes.append(node)
        node_index = self.length - 1
        self.node_name_index_map[node.name] = node_index
        return node_index

    @property
    def length(self):
        return len(self._nodes)

    def get_node_by_index(self, index):
        return self._nodes[index]


def convert_tree(data_list):
    tree = Tree()
    for data in data_list:
        if data['name'] in tree.node_name_index_map:  # 该节点已经存在在树中,但可能是子节点加进去的,需要根据自身进行配置父节点
            if 'parent_ind' not in data:
                tree.root.add_child_index(tree.node_name_index_map[data['name']])
            else:
                parent_index = tree.get_node_index_by_name(data['parent_ind'])
                parent_node = tree.get_node_by_index(parent_index)
                parent_node.add_child_index(tree.node_name_index_map[data['name']])

        elif 'parent_ind' not in data:  # 该节点没有父节点, 属于根节点的子节点
            node = Node(data['name'])
            node_index = tree.append(node)
            tree.root.add_child_index(node_index)

        elif 'parent_ind' in data:
            parent_name = data['parent_ind']
            parent_index = tree.get_node_index_by_name(parent_name)

            if parent_index < 0:  # 父节点还未加入树, 父节点加入树, 当前节点加入树, 将当前节点index放入父节点的子节点索引中
                parent_node = Node(parent_name)
                tree.append(parent_node)
                cur_node = Node(data['name'])
                cur_index = tree.append(cur_node)
                parent_node.add_child_index(cur_index)
            else:  # 父节点已在树中,提取出父节点, 将当前节点的index加入父节点的子节点索引中
                parent_node = tree.get_node_by_index(parent_index)
                cur_node = Node(data['name'])
                cur_index = tree.append(cur_node)
                parent_node.add_child_index(cur_index)
    return tree


def scan_tree(current_node, tree):
    children = current_node.children
    tmp_dict = {}
    for child_index in children:
        child_node = tree.get_node_by_index(child_index)
        tmp_dict[child_node.name] = scan_tree(child_node, tree)
    return tmp_dict


def convert_format_a(data):
    """创建树-遍历树"""
    tree = convert_tree(data)
    return scan_tree(tree.root, tree)


def convert_format_b(industry_list, expected):
    """循环遍历字典"""
    relation = {}  # 每个节点的父节点 {'连衣裙': '女装', '半身裙': '女装', '电脑配件': '数码', '内存': '电脑配件'}
    path = {}  # 每个节点的父节点的路径集合  e.g. {连衣裙:[女装], 华为牌内存: [内存, 电脑配件, 数码]}
    for entiry in industry_list:
        if 'parent_ind' not in entiry:
            if entiry['name'] not in expected:
                expected[entiry['name']] = {}
        else:
            relation[entiry['name']] = entiry['parent_ind']
            parent_name = entiry['parent_ind']
            path[entiry['name']] = [parent_name]
            while parent_name in relation:
                path[entiry['name']].append(relation[parent_name])
                parent_name = relation[parent_name]
            if parent_name not in expected:
                expected[parent_name] = {}
            tmp_inner = expected
            while len(path[entiry['name']]) > 0:
                parent = path[entiry['name']].pop()
                tmp_inner = tmp_inner[parent]
            tmp_inner[entiry['name']] = {}
    return expected


if __name__ == '__main__':
    industry_list = [
        {
            "parent_ind": "女装",
            "name": "连衣裙"
        },
        {
            "name": "女装"
        },
        {
            "parent_ind": "女装",
            "name": "半身裙"
        },
        {
            "parent_ind": "女装",
            "name": "A字裙"
        },
        {
            "name": "数码"
        },
        {
            "parent_ind": "数码",
            "name": "电脑配件"
        },
        {
            "parent_ind": "电脑配件",
            "name": "内存"
        },
    ]
    expected = convert_format(industry_list)
    print(expected)
    # {
    #     "女装": {
    #         "连衣裙": {},
    #         "半身裙": {},
    #         "A字裙": {}
    #     },
    #     "数码": {
    #         "电脑配件": {
    #             "内存": {}
    #         }
    #     }
    # }
