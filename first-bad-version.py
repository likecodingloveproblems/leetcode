def isBadVersion(index):
    i = 1702766719
    if index >= i:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        def isFirstBadVersion(index):
            if isBadVersion(index) and not isBadVersion(index - 1):
                return True
            return False

        min_index = 0
        max_index = n + 1

        while True:
            mid_index = int((max_index + min_index) / 2)
            if isFirstBadVersion(mid_index):
                return mid_index
            elif isFirstBadVersion(max_index):
                return max_index
            elif isFirstBadVersion(min_index):
                return min_index

            if isBadVersion(mid_index):
                max_index = mid_index
            else:
                min_index = mid_index


print(Solution().firstBadVersion(2126753390))
