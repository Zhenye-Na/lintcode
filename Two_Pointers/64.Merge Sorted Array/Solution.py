class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        ap, bp = m - 1, n - 1
        idx = m + n - 1

        while ap >= 0 and bp >= 0 and idx >= 0:
            if A[ap] > B[bp]:
                A[idx] = A[ap]
                ap -= 1
            else:
                A[idx] = B[bp]
                bp -= 1
            idx -= 1

        while ap >= 0:
            A[idx] = A[ap]
            ap -= 1
            idx -= 1

        while bp >= 0:
            A[idx] = B[bp]
            bp -= 1
            idx -= 1