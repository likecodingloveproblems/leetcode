class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = 0
        for i1, n1 in enumerate(num1[::-1]):
            for i2, n2 in enumerate(num2[::-1]):
                num += int(n1) * int(n2) * 10 ** (i1 + i2)
        return str(num)


num1, num2 = "2", "3"
num1, num2 = "123", "456"
r = Solution().multiply(num1, num2)
print(r)
