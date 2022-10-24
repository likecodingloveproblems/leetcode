from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def __init__(self) -> None:
        self.items = list()

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self._postorderTraversal(root)
        return self.items

    def _postorderTraversal(self, root):
        if root == None:
            return
        self._postorderTraversal(root.left)
        self._postorderTraversal(root.right)
        self.items.append(root.val)


node3 = TreeNode(val=3)
node2 = TreeNode(val=2, left=node3)
root = TreeNode(val=1, right=node2)
s = Solution().preorderTraversal(root)
print(s)
