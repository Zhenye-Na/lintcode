import sys

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        n = len(A) + len(B)
        if n % 2 == 1:
            return self._find_kth_element(A, 0, B, 0, (n - 1) // 2 + 1)
        else:
            m1 = self._find_kth_element(A, 0, B, 0, n // 2)
            m2 = self._find_kth_element(A, 0, B, 0, n // 2 + 1)
            return (m1 + m2) / 2

    def _find_kth_element(self, A, a_index, B, b_index, k):
        if a_index == len(A):
            return B[b_index + k - 1]
        if b_index == len(B):
            return A[a_index + k - 1]
        if k == 1:
            return min(A[a_index], B[b_index])

        a_val = A[a_index + k // 2 - 1] if a_index + \
            k // 2 <= len(A) else sys.maxsize
        b_val = B[b_index + k // 2 - 1] if b_index + \
            k // 2 <= len(B) else sys.maxsize

        if a_val > b_val:
            return self._find_kth_element(A, a_index, B, b_index + k // 2, k - k // 2)
        return self._find_kth_element(A, a_index + k // 2, B, b_index, k - k // 2)
