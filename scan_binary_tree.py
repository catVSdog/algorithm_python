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
        """后序遍历-递归"""
        if begin_node is None:
            return ''
        else:
            left_node = cls.post_scan_recursion(begin_node.lchild)
            right_node = cls.post_scan_recursion(begin_node.rchild)
            middle_node = begin_node.data
        # return eval(f'{left_node}{middle_node}{right_node}')  # 计算表达式的值
        return f'{left_node}{right_node}{middle_node}'  # 返回后序遍历字符串

    @classmethod
    def post_scan_stack(cls, begin_node):
        """后序遍历-栈"""
        stack_1 = []
        stack_2 = []

        stack_1.append(begin_node)

        while stack_1:
            left_node = stack_1.pop()  # 弹出时, 先弹出右孩子,再弹出左孩子
            stack_2.append(left_node)  # 压入时,先压入右孩子,再压入左孩子

            if left_node.lchild:
                stack_1.append(left_node.lchild)
            if left_node.rchild:
                stack_1.append(left_node.rchild)  # stack_1 现价左孩子,再加右孩子,

        finally_str = ''
        while stack_2:  # [ root, right_node, left_node, right_node, left_node ... ]
            item = stack_2.pop()  # 依次弹出左孩子, 右孩子, 根
            finally_str += item.data
        return finally_str

    @classmethod
    def pre_scan_recursion(cls, begin_node):
        """前序遍历-递归"""
        if begin_node is None:
            return ''
        else:
            middle_data = begin_node.data
            left_node = cls.pre_scan_recursion(begin_node.lchild)
            right_node = cls.pre_scan_recursion(begin_node.rchild)

        return f'{middle_data}{left_node}{right_node}'

    @classmethod
    def pre_scan_stack(cls, begin_node):
        """前序遍历-栈"""
        if begin_node is None:
            return ''
        stack = []
        node = begin_node
        finally_str = ''
        while node or stack:
            while node:
                finally_str += node.data
                stack.append(node)
                node = node.lchild

            next_begin = stack.pop()
            node = next_begin.rchild

        return finally_str

    @classmethod
    def middle_scan_recursion(cls, begin_node):
        if begin_node is None:
            return ''
        else:
            left_node = cls.middle_scan_recursion(begin_node.lchild)
            middle_data = begin_node.data
            right_node = cls.middle_scan_recursion(begin_node.rchild)
        return f'{left_node}{middle_data}{right_node}'

    @classmethod
    def middle_scan_stack(cls, begin_node):
        if begin_node is None:
            return ''

        stack = []
        finally_str = ''
        node = begin_node

        while node or stack:
            while node:
                stack.append(node)
                node = node.lchild

            node = stack.pop()
            finally_str += node.data
            node = node.rchild
        return finally_str


if __name__ == '__main__':
    tree = Tree()
    tree.build_tree('1')
    tree.build_tree('2')
    tree.build_tree('3')
    tree.build_tree('4')
    tree.build_tree('5')
    tree.build_tree('6')
    tree.build_tree('7')
    tree.build_tree('8')
    tree.build_tree('9')
    assert tree.middle_scan_recursion(tree.root) == tree.middle_scan_stack(tree.root) == '849251637'
    assert tree.post_scan_recursion(tree.root) == tree.post_scan_stack(tree.root) == '894526731'
    assert tree.pre_scan_recursion(tree.root) == tree.pre_scan_stack(tree.root) == '124895367'
