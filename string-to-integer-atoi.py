class Solution:
    MIN_INT_VALUE = -(2**31)
    MAX_INT_VALUE = 2**31 - 1

    def myAtoi(self, s: str) -> int:
        result = str()
        leading_whitespace = True
        for c in s:
            if c == " " and leading_whitespace:
                continue
            elif c in ["-", "+"] and len(result) == 0:
                result += c
                leading_whitespace = False
            elif c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                result += c
                leading_whitespace = False
            else:
                break
        try:
            result = int(result)
        except ValueError:
            return 0
        result = int(result)
        if result < self.MIN_INT_VALUE:
            return self.MIN_INT_VALUE
        elif result > self.MAX_INT_VALUE:
            return self.MAX_INT_VALUE
        else:
            return result


if __name__ == "__main__":
    result = Solution().myAtoi("   +0 123")
    print(result)
