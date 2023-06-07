"""
0, 0 -> 0
1, 1 -> 0
0, 1 -> 1
1, 0 -> 1
"""

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        pass


def xor(a, b):
    return (not a and b) or (not b and a)


print(xor(bin(1), bin(2)))
