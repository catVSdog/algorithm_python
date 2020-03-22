"""
遍历二叉树
"""


class Node:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

    def __repr__(self):
        return f'{self.data}'


class Tree:
    def __init__(self):
        self.root = Node()
        self.string = ''

    def build_tree(self, data):
        node = Node(data)

        if self.root.data is None:
            self.root = node
        else:
            nodes = [self.root]
            while nodes:
                top_node = nodes.pop(0)
                if top_node.lchild is None:
                    top_node.lchild = node
                    return
                elif top_node.rchild is None:
                    top_node.rchild = node
                    return
                else:
                    nodes.append(top_node.lchild)
                    nodes.append(top_node.rchild)

    @classmethod
    def post_scan_recursion(cls, begin_node):
        if begin_node is None:
            return ''
        else:
            left_node = cls.post_scan_recursion(begin_node.lchild)
            right_node = cls.post_scan_recursion(begin_node.rchild)
            middle_node = begin_node.data
        return eval(f'{left_node}{middle_node}{right_node}')  # 计算表达式的值
        # return f'{left_node}{right_node}{middle_node}'  # 返回后序遍历字符串
