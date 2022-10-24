from typing import Optional, List


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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None or root.val is None:
            return False
        return self._hasPathSum(root, targetSum)

    def _hasPathSum(self, root, target):
        if self.isLeaf(root):
            return target == root.val
        target -= root.val
        if root.left is None:
            return self._hasPathSum(root.right, target)
        elif root.right is None:
            return self._hasPathSum(root.left, target)
        else:
            return self._hasPathSum(root.left, target) or self._hasPathSum(
                root.right, target
            )

    def isLeaf(self, root):
        return root.left is None and root.right is None


root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22

head = GenerateTree().generate_tree(root)
s = Solution().hasPathSum(head, targetSum)
print(s)
