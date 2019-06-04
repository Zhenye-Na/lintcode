import heapq


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        if not intervals or len(intervals) == 0:
            return intervals

        heap, merged = [], []
        for idx, interval in enumerate(intervals):
            if interval:
                heapq.heappush(heap, (interval[0].start, interval[0].end, idx, 0))

        while heap:
            start, end, idx1, idx2 = heap[0]
            heapq.heappop(heap)
            if len(merged) == 0 or merged[-1].end < start:
                merged.append(Interval(start, end))
            else:
                merged[-1].end = max(merged[-1].end, end)

            if idx2 + 1 < len(intervals[idx1]):
                heapq.heappush(heap, (intervals[idx1][idx2 + 1].start, intervals[idx1][idx2 + 1].end, idx1, idx2 + 1))

        return merged
