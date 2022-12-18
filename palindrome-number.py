from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = deque(str(x))
        while len(x) > 1:
            if x.pop() != x.popleft():
                return False
        return True


print(Solution().isPalindrome(1))
