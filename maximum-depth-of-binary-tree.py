from typing import Optional


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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._max_depth(root, 0)

    def _max_depth(self, root, index):
        if root == None:
            return index
        index += 1
        return max(
            self._max_depth(root.left, index), self._max_depth(root.right, index)
        )


nodes = [3, 9, 20, None, None, 15, 7]
head = GenerateTree().generate_tree(nodes)
s = Solution().maxDepth(head)
print(s)
