from typing import List


# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         overlaps = dict()
#         for i1, interval1 in enumerate(intervals):
#             for i2, interval2 in enumerate(intervals[i1 + 1 :], i1 + 1):
#                 if self.has_overlap(interval1, interval2):
#                     if overlaps.get(i1):
#                         overlaps[i1].add(i2)
#                     else:
#                         overlaps[i1] = {
#                             i2,
#                         }
#                     if overlaps.get(i2):
#                         overlaps[i2].add(i1)
#                     else:
#                         overlaps[i2] = {
#                             i1,
#                         }
#         max_overlap = 0
#         removed_intervals = set()
#         while overlaps:
#             for i, overlap in enumerate(overlaps.values()):
#                 if overlap in removed_intervals:
#                     continue
#                 if len(overlap) >= max_overlap:
#                     removed_interval = i
#             removed_intervals.add(set(intervals[removed_interval]))
#             for i in overlaps[removed_interval]:
#                 overlaps[i].remove(removed_interval)
#                 if not overlaps[i]:
#                     overlaps.pop(i)
#             overlaps.pop(removed_interval)

#     def has_overlap(self, interval1, interval2):
#         return (interval1[0] < interval2[0] and interval1[1] > interval2[0]) or (
#             interval1[0] > interval2[0] and interval1[0] < interval2[1]
#         )


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlaps = dict()
        for i1, interval1 in enumerate(intervals):
            for i2, interval2 in enumerate(intervals[i1 + 1 :], i1 + 1):
                if self.has_overlap(interval1, interval2):
                    if overlaps.get(i1):
                        overlaps[i1].add(i2)
                    else:
                        overlaps[i1] = {
                            i2,
                        }
                    if overlaps.get(i2):
                        overlaps[i2].add(i1)
                    else:
                        overlaps[i2] = {
                            i1,
                        }
        max_overlap = 0
        removed_intervals = set()
        while overlaps:
            for i, overlap in enumerate(overlaps.values()):
                if overlap in removed_intervals:
                    continue
                if len(overlap) >= max_overlap:
                    removed_interval = i
            removed_intervals.add(set(intervals[removed_interval]))
            for i in overlaps[removed_interval]:
                overlaps[i].remove(removed_interval)
                if not overlaps[i]:
                    overlaps.pop(i)
            overlaps.pop(removed_interval)

    def has_overlap(self, interval1, interval2):
        return (interval1[0] < interval2[0] and interval1[1] > interval2[0]) or (
            interval1[0] > interval2[0] and interval1[0] < interval2[1]
        )


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
r = Solution().eraseOverlapIntervals(intervals)
print(r)
