from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1 :], i + 1):
                if num2 > num1:
                    for num3 in nums[j + 1 :]:
                        if num3 > num2:
                            return True
        return False


from sortedcontainers import SortedDict


class CounterMap(SortedDict):
    """A map that store each number as key in an ascending order
    and their occurrence as key"""

    def __init__(self, items=None):
        super().__init__()
        if isinstance(items, list):
            for item in items:
                self.add(item)

    def add(self, item: int) -> None:
        """if item exists only increase occurrence by one
        other wise add number in the  1"""
        if isinstance(self.get(item), int):
            self[item] += 1
        else:
            self[item] = 1

    def remove(self, item):
        if self[item] == 1:
            self.pop(item)
        else:
            self[item] -= 1


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_nums = nums[0]
        max_nums = nums[0]
        left_part = CounterMap()
        left_part.add(nums[0])
        right_part = CounterMap()
        for num in nums[1:]:
            right_part.add(num)
            if num > max_nums:
                max_nums = num
            if num < min_nums:
                min_nums = num

        for num in nums[1:-1]:
            if num > left_part.keys()[0] and num < right_part.keys()[-1]:
                return True
            left_part.add(num)
            right_part.remove(num)
        return False


nums = [1, 5, 0, 4, 1, 3]
nums = [0, 4, 2, 1, 0, -1, -3]
nums = [5, 4, 3, 2, 1]
nums = [1, 2, 3, 4, 5]
r = Solution().increasingTriplet(nums)
print(r)
