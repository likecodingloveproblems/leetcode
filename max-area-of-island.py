from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        self.grid = grid
        # initialize array
        self.visited = list()
        init_row = [0] * len(self.grid[0])
        for _ in self.grid:
            self.visited.append(init_row[:])

        for row_num, row in enumerate(self.grid):
            for col_num, _ in enumerate(row):
                if not self.visited[row_num][col_num]:
                    area = self._cal_area(row_num, col_num)
                    if max_area < area:
                        max_area = area
        return max_area

    def _cal_area(self, row_num, col_num):
        if (
            row_num < 0
            or col_num < 0
            or row_num > len(self.grid) - 1
            or col_num > len(self.grid[0]) - 1
            or self.visited[row_num][col_num]
        ):
            return 0
        self.visited[row_num][col_num] = 1
        if self.grid[row_num][col_num] == 0:
            return 0

        summation = 1

        for r in [row_num - 1, row_num + 1]:
            summation += self._cal_area(r, col_num)

        for c in [col_num - 1, col_num + 1]:
            summation += self._cal_area(row_num, c)
        return summation


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
r = Solution().maxAreaOfIsland(grid)
print(r)
