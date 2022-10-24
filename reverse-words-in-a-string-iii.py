class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split()
        for i, si in enumerate(sl):
            sl[i] = si[::-1]
        return " ".join(sl)


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))
