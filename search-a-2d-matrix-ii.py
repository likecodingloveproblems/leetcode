from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target and target <= row[-1]:
                if self.find(row, target):
                    return True
        return False

    def find(self, row, target):
        first_index, last_index = 0, len(row) - 1
        current_index = lambda: int((first_index + last_index) / 2)
        while True:
            if row[current_index()] > target:
                last_index = current_index() - 1
            elif row[current_index()] < target:
                first_index = current_index() + 1
            else:
                return True
            if row[current_index()] == target:
                return True
            if first_index > last_index:
                break


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 5
matrix, target = [[-5]], -5
r = Solution().searchMatrix(matrix, target)
print(r)
