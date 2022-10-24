from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        right_tree = self.rotate(root.right)
        return self.trees_are_equal(root.left, right_tree)

    def rotate(self, root):
        return self._rotate(root)

    def _rotate(self, root):
        if root is None:
            return

        root.left, root.right = self._rotate(root.right), self._rotate(root.left)
        return root

    def trees_are_equal(self, root1, root2):
        return self._trees_are_equal(root1, root2)

    def _trees_are_equal(self, root1, root2):
        if root1 is None or root2 is None:
            return root1 == root2
        return (
            root1.val == root2.val
            and self._trees_are_equal(root1.right, root2.right)
            and self._trees_are_equal(root1.left, root2.left)
        )


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
                node.left = TreeNode(values[current_index])
                current_index += 1
                node.right = TreeNode(values[current_index])
                current_index += 1
                new_nodes.append(node.left)
                new_nodes.append(node.right)

        self._generate_depth_nodes(values, current_index, new_nodes)
        if current_index == 1:
            return head


nodes = [1, 2, 2, 3, 4, 4, 3]
head = GenerateTree().generate_tree(nodes)
print(Solution().isSymmetric(head))
print(head)
