class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def string_to_map(s: str) -> dict:
            d = dict()
            for char in s:
                d[char] = d[char] + 1 if d.get(char) else 1
            return d

        magazine_map = string_to_map(magazine)
        ransomNote_map = string_to_map(ransomNote)
        for char, count in ransomNote_map.items():
            mag_count = magazine_map.get(char) if magazine_map.get(char) else 0
            if mag_count < count:
                return False
        return True


print(Solution().canConstruct("aa", "baa"))
print(Solution().canConstruct("aa", "ab"))
print(Solution().canConstruct("aab", "baa"))
