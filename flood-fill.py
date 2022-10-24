from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.image = image
        self.color = color
        self.val = image[sr][sc]
        self._floodFill(sr, sc)
        return self.image

    def _floodFill(self, sr, sc):
        if self.image[sr][sc] == self.val:
            self.image[sr][sc] = self.color
        else:
            return
        if sr < 0 or sc < 0 or sr > len(self.image) - 1 or sc > len(self.image[0]) - 1:
            return
        for row_num in [sr - 1, sr + 1]:
            self._floodFill(row_num, sc)
        for col_num in [sc - 1, sc + 1]:
            self._floodFill(sr, col_num)


image, sr, sc, color = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2
image, sr, sc, color = [[0, 0, 0], [0, 0, 0]], 0, 0, 0
r = Solution().floodFill(image, sr, sc, color)
print(r)
