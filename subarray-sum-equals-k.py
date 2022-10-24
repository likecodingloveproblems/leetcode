from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # zero is special
        count = 0
        nums.sort()
        for i in range(len(nums)):
            nums_sum = 0
            for num in nums[i:]:
                nums_sum += num
                if k == nums_sum:
                    count += 1
                    break
                if k < nums_sum:
                    break
        return count


nums, k = [1, 1, 1], 2
r = Solution().subarraySum(nums, k)
print(r)
