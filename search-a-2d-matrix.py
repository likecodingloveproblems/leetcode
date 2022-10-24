from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for row_num in range(row_count):
            if target <= matrix[row_num][-1]:
                row = matrix[row_num]
                break
        for item in row:
            if item == target:
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(Solution().searchMatrix(matrix, target))
