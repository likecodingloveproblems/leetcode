from typing import List
from unicodedata import numeric


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        d = dict()
        while i < len(numbers):
            if d.get(numbers[i]) is None:
                d[target - numbers[i]] = i + 1
            else:
                return d[numbers[i]], i + 1
            i += 1


numbers, target = [2, 7, 11, 15], 9
numbers, target = [-1, 0], -1
print(Solution().twoSum(numbers, target))
