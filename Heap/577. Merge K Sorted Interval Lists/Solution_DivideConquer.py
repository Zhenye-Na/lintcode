from collections import deque


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

        return self._divideConquer(intervals, 0, len(intervals) - 1)

    def _divideConquer(self, intervals, start, end):
        if start == end:
            return intervals[start]

        mid = start + (end - start) // 2
        left = self._divideConquer(intervals, start, mid)
        right = self._divideConquer(intervals, mid + 1, end)

        return self._mergeIntervalLists(left, right)

    def _mergeIntervalLists(self, left, right):
        left, right = deque(left), deque(right)
        interval = None
        merged = []

        while left and right:
            if left[0].start < right[0].start:
                interval = left.popleft()
            else:
                interval = right.popleft()

            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        while left:
            interval = left.popleft()
            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        while right:
            interval = right.popleft()
            if len(merged) == 0 or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
