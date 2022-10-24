from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def generate_tree(nums, child_count):
    head = Node(nums[0])

    _generate_level([head], nums[1:], child_count)
    return head


def _generate_level(nodes: List, values: List, child_count: int):

    if len(values) == 0:
        return

    child_indexes = range(child_count)
    child_nodes = list()
    for index, node in enumerate(nodes):
        child_indexes = map(
            lambda child_index: child_index + index * child_count, child_indexes
        )
        for child_index in child_indexes:
            child_nodes.append(Node(values[child_index]))
            node.children.append(Node(values[child_index]))
    _generate_level(child_nodes, values[len(child_nodes) :], child_count)


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        pass


root = [1, None, 3, 2, 4, None, 5, 6]
