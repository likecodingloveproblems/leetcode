from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min_index = 0
        max_index = len(nums) - 1
        while max_index >= min_index:
            mid_index = int((min_index + max_index) / 2)
            if nums[mid_index] == target:
                return mid_index
            if nums[mid_index] < target:
                min_index = mid_index + 1
            else:
                max_index = mid_index - 1
        return min_index


nums = [1, 3, 5, 6]
target = 2

print(Solution().searchInsert(nums, target))
