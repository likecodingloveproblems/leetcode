import math
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        duplicates = self.get_duplicates(nums)
        result = 0
        for count in duplicates.values():
            result += self.count_to_combinator(count)
        return int(result)


    def get_duplicates(self, nums):
        result = dict()
        for num in nums:
            if result.get(num):
                result[num] += 1
            else:
                result[num] = 1
        must_removed = list()
        for k, v in result.items():
            if v == 1:
                must_removed.append(k)
        for k in must_removed:
            result.pop(k)
        return result

    def count_to_combinator(self, count):
        return math.factorial(count) / (2 * math.factorial(count - 2))

s = Solution().numIdenticalPairs([1,2,3,1,1,3])