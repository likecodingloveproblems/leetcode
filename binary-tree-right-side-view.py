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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.right_side_view = list()
        self._right_side_view(root)
        return self.right_side_view

    def _right_side_view(self, root):
        if root is None:
            return
        self.right_side_view.append(root.val)
        if root.right:
            self._right_side_view(root.right)
        elif root.left:
            self._right_side_view(root.left)


nodes = [1, 2, 3, None, 5, None, 4]
head = GenerateTree().generate_tree(nodes)
s = Solution().rightSideView(head)
print(s)
