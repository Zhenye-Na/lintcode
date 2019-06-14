"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes or len(airplanes) == 0:
            return 0

        interval = []
        for airplane in airplanes:
            interval.append([airplane.start, 1])
            interval.append([airplane.end, -1])

        max_num_of_airplane, curr_num = -1, 0
        for timestamp, delta in sorted(interval):
            curr_num += delta
            max_num_of_airplane = max(max_num_of_airplane, curr_num)

        return max_num_of_airplane
