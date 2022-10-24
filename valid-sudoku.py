from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        return not (
            self.RowsContainDuplication()
            or self.ColumnsContainDuplication()
            or self.SquaresContainDuplication()
        )

    def RowsContainDuplication(self):
        for row in self.board:
            row_set = set()
            for item in row:
                if item != ".":
                    if item in row_set:
                        return True
                    row_set.add(item)
        return False

    def ColumnsContainDuplication(self):
        columned_data = dict()
        for row in self.board:
            for index, item in enumerate(row):
                if item != ".":
                    column = columned_data.get(index)
                    if column:
                        if item in column:
                            return True
                        column.add(item)
                    else:
                        column = set(item)
                    columned_data[index] = column

    def SquaresContainDuplication(self):
        constants = [0, 3, 6]
        for row_plus in constants:
            for col_plus in constants:
                square = set()
                for row_num in range(row_plus, 3 + row_plus):
                    for col_num in range(col_plus, 3 + col_plus):
                        item = self.board[row_num][col_num]
                        if item != ".":
                            if item in square:
                                return True
                            square.add(item)
        return False


if __name__ == "__main__":
    board = [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
    print(Solution().isValidSudoku(board))
