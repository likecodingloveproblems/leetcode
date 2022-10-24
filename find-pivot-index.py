from collections import deque
from typing import List


class Solution:
    def list_summation(self, nums: List, right=False) -> list:
        result = deque()
        summation = 0
        if right:
            for i in range(len(nums) - 1, -1, -1):
                summation += nums[i]
                result.appendleft(summation)
        else:
            for num in nums:
                summation += num
                result.append(summation)
        return result

    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = self.list_summation(nums)
        right_sum = self.list_summation(nums, right=True)
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1

    def pivotIndex1(self, nums: List[int]) -> int:
        next_left_index = 0
        next_right_index = len(nums) - 1
        left_sum, right_sum = 0, 0
        while next_left_index != next_right_index:
            next_left_sum = left_sum + nums[next_left_index]
            next_right_sum = right_sum + nums[next_right_index]
            if abs(next_left_sum - right_sum) < abs(next_right_sum - left_sum):
                left_sum = next_left_sum
                next_left_index += 1
            else:
                right_sum = next_right_sum
                next_right_index -= 1
        if right_sum == left_sum:
            return next_left_index
        else:
            return -1


nums = [1, 2, 3]
nums = [-1, -1, -1, -1, -1, 0]
nums = [-1, -1, 0, 1, 1, 0]
nums = [1, 7, 3, 6, 5, 6]
nums = [-1, -1, 0, 1, 0, -1]
nums = [2, 1, -1]
nums = [-1, -1, 1, 1, 0, 0]
s = Solution().pivotIndex(nums)
print(s)
