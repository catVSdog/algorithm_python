"""
前/后缀表达式转为表达式树
"""
from scan_binary_tree import Tree, Node


def trans_postfix_exprecession_tree(exprecession):
    """
    后缀表达式 => 表达式树
    1.遍历后缀表达式
    2.数字直接加入栈中
    3.非数字,将栈中的数字弹出作为子节点追击到非数字节点
    """
    exprecession = exprecession.replace(' ', '')
    node_stack = []
    node = None

    for i in exprecession:
        node = Node(i)
        if i.isdigit():
            node_stack.append(node)
        else:
            first_node = node_stack.pop()
            second_node = node_stack.pop()
            node.rchild = first_node  # 栈是先进后出,所以先出的应是右节点
            node.lchild = second_node
            node_stack.append(node)

    return node


def trans_prefix_exprecession_tree(exprecession):
    """
    前缀表达式 => 表达式树
    1.逆向遍历前缀表达式
    2.数字直接加入栈中
    3.非数字,将栈中的数字弹出作为子节点追击到非数字节点
    """
    exprecession = exprecession.replace(' ', '')
    node_stack = []
    node = None

    for i in range(len(exprecession) - 1, -1, -1):
        item = exprecession[i]
        node = Node(item)

        if item.isdigit():
            node_stack.append(node)
        else:
            first_node = node_stack.pop()
            second_node = node_stack.pop()

            node.lchild = first_node  # 遍历时已经是逆向了,而栈又是先进后出,负负得正,所以顺序就正确了
            node.rchild = second_node
            node_stack.append(node)

    return node


if __name__ == '__main__':
    # 遍历后缀表达式
    a = '2123*+*31-/'
    exprecession_tree = trans_postfix_exprecession_tree(a)
    print(Tree.post_scan_recursion(exprecession_tree))
    a = '21+3*42321+*-*+5+'
    exprecession_tree = trans_postfix_exprecession_tree(a)
    print(Tree.post_scan_recursion(exprecession_tree))
    print(Tree.post_scan_stack(exprecession_tree))

    # 遍历前缀表达式
    a = '/*2+1*23-31'
    exprecession_tree = trans_prefix_exprecession_tree(a)
    print(Tree.pre_scan_recursion(exprecession_tree))

    a = '++*+213*4-2*3+215'
    exprecession_tree = trans_prefix_exprecession_tree(a)
    print(Tree.pre_scan_recursion(exprecession_tree))
    print(Tree.pre_scan_stack(exprecession_tree))
