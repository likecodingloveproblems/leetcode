from typing import List

from sympy import intersection


class MyDict(dict):
    def __init__(self, items):
        for item in items:
            self[item] = self[item] + 1 if self.get(item) else 1

    def remove(self, key):
        if self[key] == 1:
            self.pop(key)
        else:
            self[key] -= 1

    def add(self, key):
        if self.get(key, False):
            self[key] += 1
        else:
            self[key] = 1


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = 0
        counts = list()
        string_map = MyDict(s)
        sub_set = set()
        for c in s:
            sub_set.add(c)
            string_map.remove(c)
            count += 1
            if not sub_set.intersection(string_map):
                counts.append(count)
                sub_set = set()
                count = 0
        return counts


s = "ababcbacadefegdehijhklij"
r = Solution().partitionLabels(s)
print(r)
