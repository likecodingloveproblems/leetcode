class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ss = str()
        step = (numRows - 1) * 2
        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                ss += s[row : len(s) : step]
            else:
                i1 = iter(range(row, len(s), step))
                i2 = iter(range(step - row, len(s), step))
                while True:
                    index1 = next(i1, None)
                    index2 = next(i2, None)
                    if index1:
                        ss += s[index1]
                    if index2:
                        ss += s[index2]
                    if not (index1 or index2):
                        break
        return ss


if __name__ == "__main__":
    import time

    s = "PAYPALISHIRING"
    num = 4
    s = "A"
    num = 1
    t1 = time.time()
    result = Solution().convert(s, num)
    t2 = time.time()
    print(result)
    print(t2 - t1)
