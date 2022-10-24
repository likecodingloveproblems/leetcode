from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = list()
        self._levelOrder([root])
        return self.result

    def _levelOrder(self, nodes):
        if len(nodes) == 0:
            return
        values = list()
        new_nodes = list()
        for node in nodes:
            values.append(node.val)
            if node.left:
                new_nodes.append(node.left)
            if node.right:
                new_nodes.append(node.right)

        if values:
            self.result.append(values)

        self._levelOrder(new_nodes)


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


nodes = [3, 9, 20, None, None, 15, 7]
head = GenerateTree().generate_tree(nodes)
s = Solution().levelOrder(head)
print(s)
