class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        start, end = 0, n
        while start + 1 < end:
            mid = (end - start) / 2 + start

            if n - self.summation(1, mid) == mid or n - self.summation(1, mid) == mid - 1:
                return mid
            elif n - self.summation(1, mid) > mid:
                start = mid
            else:
                end = mid

        if n - self.summation(1, start) == start or n - self.summation(1, start) == start - 1:
            return start
        else:
            return end


    def summation(self, start, end):
        return (start + end) * (end - start + 1) / 2;
