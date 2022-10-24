class Solution:
    MAX_INT_32 = 2**31
    MIN_INT_32 = -(2**31)

    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)
            x = "-" + x[:0:-1]
        else:
            x = str(x)[::-1]
        x = int(x)
        if x > self.MAX_INT_32 or x < self.MIN_INT_32:
            return 0
        return x


if __name__ == "__main__":
    x = 120
    s = Solution().reverse(x)
    print(s)
