"""
先序遍历： 根 -> 左 -> 右
中序遍历:  左 -> 中 -> 右
后序遍历:  左 -> 右 -> 中
层级遍历

由中序遍历和任意一种上面的遍历方式可以确定一颗二叉树
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 层级 + 先序  -> 二叉树

def rebuild_tree_from_mid_pre(pre, mid):
    """
    前序遍历： [1 2 3 4 5 6 7]
    中序遍历： [2 3 1 5 4 7 6]

    解析：

    前序遍历都是根在前，所以 1 为根
    中序遍历：左右字数分布在根左右，所以以 1 为根, [2 3] 为左子树 [5 4 7 6] 为右子树

    接着看前序，2 为根
    中序遍历  左子树为空， 3为右子树

    前序 3 为根
    中序：左右皆为空

    前序： 4 为根
    中序： [5] 为左子树 [7 6] 为右子树

    前序: 5 为根
    中序: 左右皆为空

    前序: 6 为根
    中序: [7]为左子树 右子树为空
    """
    if not pre:
        return
    if not mid:
        return

    tree = TreeNode()
    root_val = pre.pop(0)
    tree.val = root_val
    root_index = mid.index(root_val)
    left = rebuild_tree_from_mid_pre(pre, mid[:root_index])  # 先生成左子树
    tree.left = left

    right = rebuild_tree_from_mid_pre(pre, mid[root_index + 1:])  # 再生成右子树
    tree.right = right
    return tree


pre = [1, 2, 3, 4, 5, 6, 7]
mid = [2, 3, 1, 5, 4, 7, 6]
suf = [3, 2, 5, 7, 6, 4, 1]
level = [1, 2, 4, 3, 5, 6, 7]

root_1 = rebuild_tree_from_mid_pre(pre, mid)


def rebuild_tree_from_mid_suf(suf, mid):
    """
    后序： [3, 2, 5, 7, 6, 4, 1]
    中序: [2, 3, 1, 5, 4, 7, 6]
    解析:

    后序遍历，根为最后节点
    中序遍历，左右子树分布在根节点左右

    后序 1 为根
    中序 [2, 3] 和 [5, 4, 7, 6]

    后序 4 根
    中序 [5] 和 [7, 6]

    后序 6 根
    中序 [7] 和 空

    后序 7 根
    中序 左右皆空

    后序 5 根
    中序 左右皆空

    后序 2 根
    中序 [] 和 [3]

    后序 3 根
    中序 左右皆为空
    """
    if not suf:
        return
    if not mid:
        return

    tree = TreeNode()
    root_val = suf.pop()
    tree.val = root_val
    root_index = mid.index(root_val)
    right = rebuild_tree_from_mid_suf(suf, mid[root_index + 1:])  # 先生成右子树
    tree.right = right
    left = rebuild_tree_from_mid_suf(suf, mid[:root_index])  # 再生成左子树
    tree.left = left

    return tree


root_2 = rebuild_tree_from_mid_suf(suf, mid)


def rebuild_tree_from_mid_level(level, mid):
    """
    层级：[1, 2, 4, 3, 5, 6, 7]
    中序: [2, 3, 1, 5, 4, 7, 6]

    层级 1 根
    中序 [2, 3] 和 [5, 4, 7, 6]
    层级 [2, 3]  [4, 5, 6, 7]

    层级 2 根
    中序 [] 和 [3]
    层级 [] 和 [3]


    层级 4 根
    中序 [5] 和 [7, 6]
    层加 [5] 和 [6, 7]


    层级 3 根
    中序 [] 和 []
    层级 [] 和 「」

    层级 5 根
    中序 [] []

    层级 6 根
    中序 [7] []

    层加 7 根
    中序 [] []
    """

    if not level:
        return
    if not mid:
        return

    tree = TreeNode()
    root_val = level.pop(0)

    tree.val = root_val
    root_index = mid.index(root_val)
    mid_left = mid[:root_index]
    mid_right = mid[root_index + 1:]

    level_left = []
    level_right = []
    for i in level:
        if i in mid_left:
            level_left.append(i)
        if i in mid_right:
            level_right.append(i)

    left = rebuild_tree_from_mid_level(level_left, mid_left)
    tree.left = left
    righ = rebuild_tree_from_mid_level(level_right, mid_right)
    tree.right = righ
    return tree


root_3 = rebuild_tree_from_mid_level(level, mid)


def pre_scan(root):
    """
    先序
    """
    slice = []

    def inner(root):
        if root is None:
            return
        slice.append(root.val)
        inner(root.left)
        inner(root.right)
        return slice

    inner(root)
    return slice


def mid_scan(root):
    """
    中序
    """
    slice = []

    def inner(root):
        if root is None:
            return
        inner(root.left)
        slice.append(root.val)
        inner(root.right)

    inner(root)
    return slice


def suf_scan(root):
    """
    后序
    """
    slice = []

    def inner(root):
        if root is None:
            return
        inner(root.left)
        inner(root.right)
        slice.append(root.val)

    inner(root)
    return slice


def level_scan(root):
    """
    层级
    """

    slice = []

    tmp = [root]

    while tmp:
        length = len(tmp)
        for i in range(length):
            node = tmp.pop(0)
            slice.append(node.val)
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)
    return slice


print('前序遍历')
print('树一：', pre_scan(root_1))
print('树二：', pre_scan(root_2))
print('树三：', pre_scan(root_3))

print('中序遍历')
print('树一：', mid_scan(root_1))
print('树二：', mid_scan(root_2))
print('树三：', mid_scan(root_3))

print('后序遍历')
print('树一：', suf_scan(root_1))
print('树二：', suf_scan(root_2))
print('树三：', suf_scan(root_3))

print('层级遍历')
print('树一：', level_scan(root_1))
print('树二：', level_scan(root_2))
print('树三：', level_scan(root_3))
