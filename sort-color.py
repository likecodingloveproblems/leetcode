from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        index = 0
        for num in nums:
            counts[num] += 1

        for i, count in enumerate(counts):
            for _ in range(count):
                nums[index] = i
                index += 1


nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)
