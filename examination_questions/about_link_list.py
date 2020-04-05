class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.data}'


def function(node):
    stack = []

    while node:
        stack.append(node)
        node = node.next

    while stack:
        print(stack.pop())


def function_b(node):
    if node is None:
        return
    else:
        function_b(node.next)
        print(node)


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    a.next = b
    b.next = c
    function_b(a)
