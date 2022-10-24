from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                nums_set.remove(num)
            else:
                nums_set.add(num)  
        return nums_set.pop()

nums = [2,2,1]
r = Solution().singleNumber(nums)
print(r)