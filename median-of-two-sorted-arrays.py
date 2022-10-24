from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        return self.simple_median(nums)

    def simple_median(self, nums):
        if len(nums) % 2:
            return nums[len(nums) // 2]
        else:
            i, j = len(nums) // 2, len(nums) // 2 - 1
            return (nums[i] + nums[j]) / 2


if __name__ == "__main__":
    l1 = [1, 2]
    l2 = [3, 4]
    s = Solution().findMedianSortedArrays(l1, l2)
    print(s)
