"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals or len(intervals) == 0:
            return 0

        new_intervals = []
        for interval in intervals:
            new_intervals.append([interval.start, 1])
            new_intervals.append([interval.end, -1])

        new_intervals.sort()
        min_rooms, curr_rooms = 0, 0
        for _, delta in new_intervals:
            curr_rooms += delta
            min_rooms = max(min_rooms, curr_rooms)

        return min_rooms
