from collections import deque
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        end_items = deque()
        for _ in range(k):
            end_items.appendleft(nums.pop())
        result = list(end_items) + nums
        for i, v in enumerate(result):
            if i < len(nums):
                nums[i] = v
            else:
                nums.append(v)
        # length = len(nums)
        # k %= length
        # bound = length - k
        # if bound == 0:
        #     return
        # elif bound == k:
        #     for i in range(k):
        #         nums[i], nums[k + i] = nums[bound + i], nums[i]
        # else:
        #     for i in range(min(k, bound)):
        #         nums[i], nums[k + i], nums[bound + i] = (
        #             nums[bound + i],
        #             nums[i],
        #             nums[k + i],
        #         )


nums, k = [-1], 2
nums, k = [1, 2, 3], 2
nums, k = [-1, -100, 3, 99], 2
nums, k = [1, 2, 3, 4, 5, 6, 7, 8, 9], 3
Solution().rotate(nums, k)
print(nums)
