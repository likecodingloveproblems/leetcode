from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for i, v in enumerate(nums):
            sum += v
            nums[i] = sum
        return nums


nums = [1, 2, 3, 4]
s = Solution().runningSum(nums)
print(s)
