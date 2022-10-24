from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        sub = deque()
        i = 0
        while i < len(s):
            if s[i] in sub:
                max_length = len(sub) if len(sub) > max_length else max_length
                sub.popleft()
                continue
            else:
                sub.append(s[i])
                i += 1

        max_length = len(sub) if len(sub) > max_length else max_length
        return max_length
