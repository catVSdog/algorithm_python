"""
二叉树
                 10
               /   \
             7      20
            / \    /  \
          4    9  15   30
             二叉查找树
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
            finally_str += str(item.data)
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
                finally_str += str(node.data)
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

        # if left_node and right_node:
        #     return f'({left_node}{middle_data}{right_node})'  # 表达式树,构建中缀表达式
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
            finally_str += str(node.data)
            node = node.rchild
        return finally_str

    @classmethod
    def level_scan(cls, begin_node):
        """层级遍历"""
        if begin_node is None:
            return
        nodes = [begin_node]
        finally_str = ''
        while nodes:
            first_node = nodes.pop(0)
            finally_str += str(first_node.data)

            if first_node.lchild:
                left_node = first_node.lchild
                nodes.append(left_node)
            if first_node.rchild:
                right_node = first_node.rchild
                nodes.append(right_node)

        return finally_str

    def find(self, begin_node, data):
        if begin_node is None:
            return False
        if begin_node.data == data:
            return True
        result1 = self.find(begin_node.lchild, data)
        result2 = self.find(begin_node.rchild, data)
        return result1 or result2

    def find_min_recursion(self, begin_node):
        if begin_node is None:
            return
        if begin_node.lchild is None:
            return begin_node.data
        else:
            return self.find_min_recursion(begin_node.lchild)

    @staticmethod
    def find_min(begin_node):
        """最小值"""
        if begin_node is None:
            return
        node = begin_node
        while node.lchild:
            node = node.lchild
        return node.data

    def find_max_recursion(self, begin_node):
        if begin_node is None:
            return
        if begin_node.rchild is None:
            return begin_node.data
        else:
            return self.find_max_recursion(begin_node.rchild)

    @staticmethod
    def find_max(begin_node):
        """最大值"""
        if begin_node is None:
            return
        node = begin_node

        while node.rchild:
            node = node.rchild
        return node.data

    def insert(self, begin_node, data):
        """递归构建二叉查找树"""
        if begin_node.data is None:
            begin_node.data = data
            return True
        elif data < begin_node.data:
            if begin_node.lchild is None:
                begin_node.lchild = Node()
                return self.insert(begin_node.lchild, data)
            else:
                return self.insert(begin_node.lchild, data)
        elif data > begin_node.data:
            if begin_node.rchild is None:
                begin_node.rchild = Node()
                return self.insert(begin_node.rchild, data)
            else:
                return self.insert(begin_node.rchild, data)
        else:
            return False


if __name__ == '__main__':
    tree = Tree()
    tree.build_tree(10)
    tree.build_tree(7)
    tree.build_tree(20)
    tree.build_tree(4)
    tree.build_tree(9)
    tree.build_tree(15)
    tree.build_tree(30)
    assert tree.middle_scan_recursion(tree.root) == tree.middle_scan_stack(tree.root)
    assert tree.post_scan_recursion(tree.root) == tree.post_scan_stack(tree.root)
    assert tree.pre_scan_recursion(tree.root) == tree.pre_scan_stack(tree.root)
    assert tree.level_scan(tree.root) == '10720491530'
    assert tree.find(tree.root, 4) is True
    assert tree.find(tree.root, 100) is False
    assert tree.find_min(tree.root) == tree.find_min_recursion(tree.root) == 4
    assert tree.find_max(tree.root) == tree.find_max_recursion(tree.root) == 30

    tree_2 = Tree()
    assert tree_2.insert(tree_2.root, 10) == True
    assert tree_2.insert(tree_2.root, 5) == True
    assert tree_2.insert(tree_2.root, 15) == True
    assert tree_2.insert(tree_2.root, 5) == False
    assert tree_2.insert(tree_2.root, 1) == True
    assert tree_2.insert(tree_2.root, 7) == True
    assert tree_2.insert(tree_2.root, 20) == True
    assert tree_2.insert(tree_2.root, 13) == True

    assert tree_2.level_scan(tree_2.root) == '10515171320'
