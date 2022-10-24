from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target_sum = targetSum
        return self._pathSum(root)

    def _pathSum(self, root, sum=0):
        if root is None:
            return []
        sum += root.val
        if root.left is None and root.right is None:
            if sum == self.target_sum:
                "save this path"
                return [deque([root.val])]
            else:
                return []
        paths = self._pathSum(root.left, sum)
        paths += self._pathSum(root.right, sum)
        for path in paths:
            path.appendleft(root.val)
        return paths


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


nodes, target_sum = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22
head = GenerateTree().generate_tree(nodes)
s = Solution().pathSum(head, target_sum)
print(s)
