from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = list()
        queue = deque()
        result = list()
        for v in nums:
            vs = v**2
            if v <= 0:
                stack.append(vs)
            else:
                queue.append(vs)

        while len(stack) or len(queue):
            if len(stack) == 0:
                result.append(queue.popleft())
            elif len(queue) == 0:
                result.append(stack.pop())
            elif stack[-1] > queue[0]:
                result.append(queue.popleft())
            else:
                result.append(stack.pop())
        return result


nums = [-4, -1, 0, 3, 10]
nums = [-10000, -9999, -7, -5, 0, 0, 10000]
nums = [-4, -3, -3, -2, 2]
print(Solution().sortedSquares(nums))
