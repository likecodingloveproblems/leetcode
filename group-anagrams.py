from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = dict()
        for s in strs:
            s_set = frozenset([(c, s.count(c)) for c in set(s)])

            if s_set in s_map:
                s_map[s_set].append(s)
            else:
                s_map[s_set] = [s]
            grouped_strs = s_map.values()
        return sorted(grouped_strs, key=lambda l: len(l))


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["ddddddddddg", "dgggggggggg"]
r = Solution().groupAnagrams(strs)
print(r)
