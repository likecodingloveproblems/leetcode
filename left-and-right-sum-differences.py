from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = self.left_sum(nums)
        right_sum = self.right_sum(nums)
        diff = list()
        for left_num, right_num in zip(left_sum, right_sum):
            diff.append(abs(left_num - right_num))
        return diff

    def left_sum(self, nums):
        result = [0]
        sum = 0
        for num in nums[:-1]:
            sum += num
            result.append(sum)
        return result

    def right_sum(self, nums):
        return self.left_sum(nums[::-1])[::-1]


s = Solution()
nums = [10, 4, 8, 3]
print(s.left_sum(nums))
print(s.right_sum(nums))
print(s.leftRigthDifference(nums))
