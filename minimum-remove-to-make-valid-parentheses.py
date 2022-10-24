class Solution:
    OPEN_PARENTHESES = "("
    CLOSE_PARENTHESES = ")"

    def minRemoveToMakeValid(self, s: str) -> str:
        parentheses_stack = list()
        parentheses_index_stack = list()
        chars_list = list()
        for i, c in enumerate(s):
            if c == self.OPEN_PARENTHESES:
                chars_list.append(c)
                parentheses_stack.append(c)
                parentheses_index_stack.append(i)
            elif c == self.CLOSE_PARENTHESES:
                chars_list.append(c)
                if parentheses_stack and parentheses_stack[-1] == self.OPEN_PARENTHESES:
                    parentheses_stack.pop()
                    parentheses_index_stack.pop()
                else:
                    parentheses_index_stack.append(i)
            else:
                chars_list.append(c)

        for i in parentheses_index_stack[::-1]:
            chars_list.pop(i)

        return "".join(chars_list)


s = "))(("
s = "a)b(c)d"
s = "lee(t(c)o)de)"
r = Solution().minRemoveToMakeValid(s)
print(r)
