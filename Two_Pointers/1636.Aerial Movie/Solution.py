import sys


class Solution:
    """
    @param t: the length of the flight
    @param dur: the length of movies 
    @return: output the lengths of two movies
    """

    def aerial_Movie(self, t, dur):
        # Write your code here
        dur.sort()
        t = t - 30
        left, right = 0, len(dur) - 1
        ans = [0, 0]
        delta = sys.maxsize

        while left < right:
            if dur[left] + dur[right] > t:
                right -= 1
            elif dur[left] + dur[right] < t:
                d = t - (dur[left] + dur[right])
                if d < delta:
                    ans = [dur[left], dur[right]]
                    delta = d
                left += 1
            elif dur[left] + dur[right] == t:
                return [dur[left], dur[right]]

        return ans
