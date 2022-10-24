from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        margin = 0
        count = 0
        length = len(matrix)
        while length - 2 * margin > 1:
            (
                matrix[margin][margin + count],
                matrix[margin + count][length - margin - 1],
                matrix[length - margin - count - 1][margin],
                matrix[length - margin - 1][length - margin - 1 - count],
            ) = (
                matrix[length - margin - count - 1][margin],
                matrix[margin][margin + count],
                matrix[length - margin - 1][length - margin - 1 - count],
                matrix[margin + count][length - margin - 1],
            )
            count += 1
            if length - 2 * margin - 1 == count:
                margin += 1
                count = 0


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
Solution().rotate(matrix)
print(matrix)
