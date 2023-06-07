# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original.val == target.val:
            return cloned
        if original.left is not None:
            value = self.getTargetCopy(original.left, cloned.left, target)
            if value is not None:
                return value
        if original.right is not None:
            value = self.getTargetCopy(original.right, cloned.right, target)
            if value is not None:
                return value


original = TreeNode(7)
original.left = TreeNode(4)
original.right = TreeNode(3)
cloned = TreeNode(7)
cloned.left = TreeNode(4)
cloned.right = TreeNode(3)
s = Solution()
cloned_target = s.getTargetCopy(original, cloned, original.right)
print(cloned_target)
