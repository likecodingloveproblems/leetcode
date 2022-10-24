import time
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result_set = set()
        result = list()
        for i1, _ in enumerate(nums):
            i2, i3 = i1 + 1, len(nums) - 1
            while i2 < i3:
                if i1 == i2:
                    i2 += 1
                    continue
                elif i1 == i3:
                    i3 -= 1
                    continue
                s = nums[i1] + nums[i2] + nums[i3]
                if s == 0:
                    r = (nums[i1], nums[i2], nums[i3])
                    if r not in result_set:
                        result.append(r)
                        result_set.add(r)
                    i2 += 1
                elif s < 0:
                    i2 += 1
                else:
                    i3 -= 1
        return result


nums = [-1, 0, 1, 2, -1, -4]
t0 = time.time()
r = Solution().threeSum(nums)
t1 = time.time()
print(r)
print(t1 - t0)
