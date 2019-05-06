class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or not k or len(L) == 0:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._compute_k(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self._compute_k(L, end) >= k:
            return end
        if self._compute_k(L, start) >= k:
            return start
        return 0


    def _compute_k(self, L, length):
        return sum([l // length for l in L])
