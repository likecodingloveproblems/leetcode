from typing import List
from typing_extensions import Self


# class Node:
#     def __init__(self, val: int, right: Self=None, left: Self=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Tree:
#     def __init__(self, root: Node=None):
#         self.root = root

#     def create_from_list(nums: List[int]) -> Tree:


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = 0
        max_index = len(nums)
        prev_middle_index = -1
        while True:
            middle_index = int((max_index + min_index) / 2)
            if middle_index == prev_middle_index:
                break
            if target == nums[middle_index]:
                return middle_index
            if target < nums[middle_index]:
                max_index = middle_index
            else:
                min_index = middle_index
            prev_middle_index = middle_index
        return -1


print(Solution().search([-1, 0, 3, 5, 9, 12, 13], 9))
s = Solution().search([5], 5)
print(s)
