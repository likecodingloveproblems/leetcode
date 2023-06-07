class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        return self.get_max(num) - self.get_min(num)

    def get_max(self, num: str) -> int:
        for char in num:
            if char != "9":
                return int(num.replace(char, "9"))
        return int(num)

    def get_min(self, num: str) -> int:
        if num[0] != "1":
            return int(num.replace(num[0], "1"))
        for char in num[1:]:
            if char != "0":
                num = num.replace(char, "0")
                if int(num) == 0:
                    num = num.replace("0", "1")
        return int(num)


s = Solution()
print(s.maxDiff(111))
