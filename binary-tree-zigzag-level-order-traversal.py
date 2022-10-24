from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class GenerateTree:
    def generate_tree(self, values):
        return self._generate_depth_nodes(values, 0)

    def _generate_depth_nodes(self, values, current_index, nodes=None):
        if current_index >= len(values):
            return
        if nodes is None:
            head = TreeNode(values[current_index])
            new_nodes = [head]
            current_index += 1
        else:
            new_nodes = list()
            for node in nodes:
                if values[current_index]:
                    node.left = TreeNode(values[current_index])
                    new_nodes.append(node.left)
                current_index += 1
                if values[current_index]:
                    node.right = TreeNode(values[current_index])
                    new_nodes.append(node.right)
                current_index += 1

        self._generate_depth_nodes(values, current_index, new_nodes)
        if current_index == 1:
            return head


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = list()
        self._extract_depth([root])
        return self.result

    def _extract_depth(self, nodes, right_to_left=False):
        if not nodes:
            return

        depth_values = list()
        new_nodes = list()
        while nodes:
            node = nodes.pop()
            depth_values.append(node.val)
            if right_to_left:
                if node.right:
                    new_nodes.append(node.right)
                if node.left:
                    new_nodes.append(node.left)
            else:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
        self.result.append(depth_values)
        self._extract_depth(new_nodes, not right_to_left)


nodes = [3, 9, 20, None, None, 15, 7]
head = GenerateTree().generate_tree(nodes)
s = Solution().zigzagLevelOrder(head)
print(s)
