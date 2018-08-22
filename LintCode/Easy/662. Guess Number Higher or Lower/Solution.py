"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        start, end = 1, n
        while start + 1 < end:
            mid = (end - start) / 2 + start

            if Guess.guess(mid) == 0:
                return mid
            elif Guess.guess(mid) > 0:
                start = mid
            else:
                end = mid

        if Guess.guess(start) == 0:
            return start
        if Guess.guess(end) == 0:
            return end
        return -1
