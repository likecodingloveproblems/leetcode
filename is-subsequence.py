from collections import deque


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = deque(t)
        for c in s:
            while True:
                if len(t) == 0:
                    return False
                if c == t.popleft():
                    break

        return True


s, t = "abc", "ahbgdc"
s, t = "acb", "ahbgdc"
s = Solution().isSubsequence(s, t)
print(s)
