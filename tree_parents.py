"""
树-双亲表示法
"""
from django.forms import models


class Strategy(models.Model):
    pass


class Tree:
    def __init__(self):
        self.nodes = []

    def append(self, node):
        self.nodes.append(node)

    def get_node_index(self, node):
        return self.nodes.index(node)

    @property
    def nodes_count(self):
        return len(self.nodes)

    def pop(self):
        self.nodes.pop()

    @property
    def range(self):
        return self.nodes


class Node:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent


def run():
    node_temp_list = []
    strategy_code = 'STRATEGY_202003040001'
    try:
        strategy = Strategy.objects.get(strategy_code=strategy_code)
    except Strategy.DoesNotExist:
        return

    tree = Tree()

    node_strategy = Node(strategy)
    tree.append(node_strategy)

    node_temp_list.append(node_strategy)

    while node_temp_list:
        node = node_temp_list.pop(0)
        node_index = tree.get_node_index(node)

        if isinstance(node.data, Strategy):
            # 增加app信息
            app = node.data.application
            node_app = Node(app, node_index)
            tree.append(node_app)

            # 增加规则集信息
            rule_sets = node.data.rule_set.all()
            for rule_set in rule_sets:
                node_rule_set = Node(rule_set, node_index)
                tree.append(node_rule_set)
                node_temp_list.append(node_rule_set)
