from typing import List
from math import factorial


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self._get_row(rowIndex)

    def _get_value(self, row_index, col_index):
        if col_index < 0 or col_index > row_index:
            return 0
        if row_index == 0:
            return 1

        return self._get_value(row_index - 1, col_index - 1) + self._get_value(
            row_index - 1, col_index
        )

    def _get_row(self, row_index):
        row = list()
        for col_index in range(row_index + 1):
            row.append(self._get_value(row_index, col_index))
        return row


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = list()
        for col_index in range(rowIndex + 1):
            row.append(int(self.combination(rowIndex, col_index)))
        return row

    def combination(self, n, r):
        return factorial(n) / (factorial(n - r) * factorial(r))


rowIndex = 33
r = Solution().getRow(rowIndex)
print(r)
