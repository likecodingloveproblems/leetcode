from collections import deque
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        summation = 0
        left_index, right_index = 0, 0
        while True:
            if summation == k:
                count += 1
                summation -= nums[left_index]
                left_index += 1
            elif summation > k:
                summation -= nums[left_index]
                left_index += 1
            elif summation < k and right_index < len(nums):
                summation += nums[right_index]
                right_index += 1
            if right_index == len(nums) and summation < k:
                break
        return count


nums, k = [1, 1, 1], 2
nums, k = [1, 2, 3], 3
nums, k = [1], 0
nums, k = [-1, -1, 1], 0
r = Solution().subarraySum(nums, k)
print(r)
