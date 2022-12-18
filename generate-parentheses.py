from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = list()
        pattern = list(range(n))

        while True:
            string = self.generate_string(pattern, n)
            if self.is_valid(string):
                parenthesis.append(string)
            pattern, is_end = self.update_pattern(pattern, n)
            if is_end:
                break

        return parenthesis

    def generate_string(self, pattern, n):
        chars = list()
        for i in range(2 * n):
            if i in pattern:
                chars.append("(")
            else:
                chars.append(")")
        return "".join(chars)

    def is_valid(self, string):
        stack = list()
        for c in string:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != "(":
                    return False
        if len(stack) > 0:
            return False
        return True

    def update_pattern(self, pattern, n):
        index = 1
        while True:
            pattern[-index] += 1
            if pattern[-index] > 2 * n - index:
                while True:
                    index += 1
                    if index == 2 * n:
                        return pattern, True
                    if index + pattern[-index] > 2 * n:
                        break
                    else:
                        break
            else:
                break
        if index > 1:
            while index > 1:
                index -= 1
                pattern[-index] = pattern[-index - 1] + 1
        return pattern, False


n = 3
print(Solution().generateParenthesis(n))
