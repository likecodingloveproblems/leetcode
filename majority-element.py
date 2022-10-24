from typing import List


class MyDict(dict):
    def add(self, key):
        if self.get(key, False):
            self[key] += 1
        else:
            self[key] = 1


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = MyDict()
        majority_count = len(nums) / 2
        for num in nums:
            nums_dict.add(num)

        for num, count in nums_dict.items():
            if count > majority_count:
                return num

        return -1


nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]
r = Solution().majorityElement(nums)
print(r)
