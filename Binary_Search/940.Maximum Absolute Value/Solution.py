class Solution:
    """
    @param A: an array
    @param n: an integer
    @return: makes the smallest absolute value of the difference between any two elements to largest
    """
    def maximumAbsolutValue(self, A, n):
        # Write your code here
        if not A or len(A) == 0 or n <= 1 or n > len(A):
            return -1

        A.sort()
        lo, hi = 0, (A[-1] - A[0]) // (n - 1) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self._compute_N(A, mid) >= n:
                lo = mid
            else:
                hi = mid

        return lo

    def _compute_N(self, A, diff):

        count, val = 1, diff + A[0]
        for a in A[1:]:
            if a >= val:
                count += 1
                val = a + diff

        return count
