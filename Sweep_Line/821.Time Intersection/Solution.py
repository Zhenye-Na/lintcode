"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        # Write your code here
        if not seqA or not seqB or len(seqA) == 0 or len(seqB) == 0:
            return []

        timelines = []
        for a in seqA:
            timelines.append((a.start, 1))
            timelines.append((a.end, -1))

        for b in seqB:
            timelines.append((b.start, 1))
            timelines.append((b.end, -1))

        timelines.sort()

        results = []
        start_time, end_time = -1, -1
        running_count, max_count = 0, 0
        for time, delta in timelines:
            running_count += delta
            if running_count == 2 and max_count < 2:
                start_time = time
                max_count = running_count

            elif running_count < 2 and max_count == 2:
                end_time = time
                max_count = running_count

            if start_time != -1 and end_time != -1:
                results.append(Interval(start_time, end_time))
                start_time, end_time = -1, -1

        return results
