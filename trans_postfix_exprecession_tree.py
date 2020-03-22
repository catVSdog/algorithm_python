"""
后缀表达式转为表达式树
"""
from scan_binary_tree import Tree, Node


def trans_postfix_exprecession_tree(exprecession):
    exprecession = exprecession.replace(' ', '')
    node_stack = []
    parent_node = None

    for i in exprecession:
        if i.isdigit():
            node = Node(i)
            node_stack.append(node)
        else:
            parent_node = Node(i)
            first_node = node_stack.pop()
            second_node = node_stack.pop()
            parent_node.rchild = first_node  # 栈是先进后出,所以先出的应是右节点
            parent_node.lchild = second_node
            node_stack.append(parent_node)

    return parent_node


if __name__ == '__main__':
    a = '2123*+*31-/'

    exprecession_tree = trans_postfix_exprecession_tree(a)

    print(Tree.post_scan_recursion(exprecession_tree))

    a = '21+3*42321+*-*+5+'

    exprecession_tree = trans_postfix_exprecession_tree(a)

    print(Tree.post_scan_recursion(exprecession_tree))
