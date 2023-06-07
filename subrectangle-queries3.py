from collections import deque
from typing import List


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.updates = deque()

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.updates.appendleft(((row1, row2), (col1, col2), newValue))

    def getValue(self, row: int, col: int) -> int:
        for update in self.updates:
            if update[0][0] <= row <= update[0][1] and update[1][0] <= col <= update[1][1]:
                return update[2]
        return self.rectangle[row][col]


rectangle = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
obj = SubrectangleQueries(rectangle)
obj.updateSubrectangle(0, 0, 3, 2, 5)
obj.updateSubrectangle(3, 0, 3, 2, 10)
print(obj.getValue(3, 1))
print(obj.getValue(0, 2))
