from asyncore import write
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read_index = 0
        write_index = 0
        zero_count = 0
        while write_index < len(nums):
            if write_index + zero_count >= len(nums):
                nums[write_index] = 0
                write_index += 1
            elif nums[read_index] != 0:
                nums[write_index] = nums[read_index]
                write_index += 1
            else:
                zero_count += 1
            read_index += 1


nums = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums)
print(nums)
