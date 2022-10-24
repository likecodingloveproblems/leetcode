from collections import deque
from itertools import zip_longest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = deque()
        baghimandeh = 0
        for n1, n2 in zip_longest(num1[::-1], num2[::-1], fillvalue="0"):
            sum_result = int(n1) + int(n2) + baghimandeh
            baghimandeh = sum_result // 10
            result.appendleft(str(sum_result % 10))
        if baghimandeh:
            result.appendleft(str(baghimandeh))

        return "".join(result)


num1, num2 = "11", "123"
num1, num2 = "456", "77"
num1, num2 = "0", "0"
num1, num2 = "1", "9"
r = Solution().addStrings(num1, num2)
print(r)
