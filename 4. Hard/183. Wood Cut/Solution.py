class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if L is None or len(L) == 0:
            return 0

        start, end = 1, max(L)
        while (start + 1 < end):
            mid = (start + end) / 2

            count = self.counter(L, mid)
            if count >= k:
                start = mid
            else:
                end = mid

        count1, count2 = self.counter(L, start), self.counter(L, end)

        if count2 >= k:
            return end
        elif count1 >= k:
            return start
        else:
            return 0


    def counter(self, L, d):
        counter = 0
        for dist in L:
            counter += dist / d
        return counter
