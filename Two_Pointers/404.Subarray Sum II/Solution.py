class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        if not A or len(A) == 0:
            return 0

        n = len(A)
        l, r = 0, 0
        l_sum, r_sum = 0, 0
        res = 0

        for i in range(len(A)):

            l = max(l, i)
            r = max(r, i)

            while l < n and l_sum + A[l] < start:
                l_sum += A[l]
                l += 1

            while r < n and r_sum + A[r] <= end:
                r_sum += A[r]
                r += 1

            if r - l > 0:
                res += r - l

            if l > i:
                l_sum = l_sum - A[i]

            if r > i:
                r_sum = r_sum - A[i]

        return res
