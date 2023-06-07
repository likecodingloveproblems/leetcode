from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        MAX_AREA = (4 * 10**4) ** 2
        min_area = MAX_AREA
        points.sort()
        for i, point in enumerate(points):
            min_area = self.find_min_area(points[i + 1 :], point, min_area)
        if min_area == MAX_AREA:
            min_area = 0
        return min_area

    def find_min_area(self, points, point, min_area):
        top_left_corner = set()
        bottom_right_corner = set()
        for p in points:
            if p[0] == point[0]:
                top_left_corner.add(p[1])
            elif p[1] == point[1]:
                bottom_right_corner.add(p[0])
            elif p[0] in bottom_right_corner and p[1] in top_left_corner:
                area = abs((point[0] - p[0]) * (point[1] - p[1]))
                if min_area > area:
                    min_area = area
        return min_area


s = Solution()
area = s.minAreaRect([[3, 2], [0, 0], [3, 3], [3, 4], [4, 4], [2, 1], [4, 3], [1, 0], [4, 1], [0, 2]])
print(area)
