class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: how many problem can you accept
    """

    def canAccept(self, n, k):
        # Write your code here
        # range of number of problems can be solved
        self.k = k
        start, end = 0, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._computeSum(mid) <= n:
                start = mid
            else:
                end = mid

        if self._computeSum(end) <= n:
            return end
        if self._computeSum(start) <= n:
            return start

        return -1

    def _computeSum(self, endIndex):
        return endIndex * (endIndex + 1) / 2 * self.k
