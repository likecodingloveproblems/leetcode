from typing import Optional

from executing import Source


def generate_bst(nodes):
    pass


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return

    def _searchBST(self, root):
        return


nodes, val = [4, 2, 7, 1, 3], 2
root = generate_bst(nodes)

r = Solution().searchBST(root, val)
