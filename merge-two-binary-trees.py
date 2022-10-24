from typing import Optional


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
                if current_index < len(values) and values[current_index]:
                    node.left = TreeNode(values[current_index])
                    new_nodes.append(node.left)
                current_index += 1
                if current_index < len(values) and values[current_index]:
                    node.right = TreeNode(values[current_index])
                    new_nodes.append(node.right)
                current_index += 1

        self._generate_depth_nodes(values, current_index, new_nodes)
        if current_index == 1:
            return head


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
        elif root1 is None and root2 is None:
            return
        elif root1 is None:
            node = TreeNode(root2.val)
            node.left = self.mergeTrees(None, root2.left)
            node.right = self.mergeTrees(None, root2.right)
        elif root2 is None:
            node = TreeNode(root1.val)
            node.left = self.mergeTrees(root1.left, None)
            node.right = self.mergeTrees(root1.right, None)
        return node


r1, r2 = [1, 3, 2, 5], [2, 1, 3, None, 4, None, 7]
t1 = GenerateTree().generate_tree(r1)
t2 = GenerateTree().generate_tree(r2)
r = Solution().mergeTrees(t1, t2)
print(r)
