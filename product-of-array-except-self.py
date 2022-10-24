from typing import List
import numpy as np


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        global_product = 1
        zero_count = 0
        has_zero = False
        for num in nums:
            if num == 0:
                has_zero = True
                zero_count += 1
            else:
                global_product *= num

        result = list()

        for num in nums:
            if has_zero:
                if zero_count == 1:
                    if num == 0:
                        result.append(global_product)
                    else:
                        result.append(0)
                else:
                    result.append(0)
            else:
                result.append(int(global_product / num))
        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        global_product = 1
        zero_count = 0
        has_zero = False
        zero_index = 0
        for i, num in enumerate(nums):
            if num == 0:
                has_zero = True
                zero_count += 1
                zero_index = i
            else:
                global_product *= num

        result = np.zeros(len(nums), int)

        if has_zero:
            if zero_count == 1:
                result[zero_index] = global_product
            return result

        for i, num in enumerate(nums):
            result[i] = int(global_product / num)
        return result


nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]
r = Solution().productExceptSelf(nums)
print(r)
