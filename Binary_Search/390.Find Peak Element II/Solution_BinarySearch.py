class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        if not A or len(A) == 0 or len(A[0]) == 0:
            return [-1, -1]

        # 二分列
        n, m = len(A), len(A[0])
        lo, hi = 0, len(A[0]) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            max_idx, max_num = -1, -1
            for row in range(n):
                if A[row][mid] > max_num:
                    max_num, max_idx = A[row][mid], row

            if A[max_idx][mid - 1] < A[max_idx][mid] and A[max_idx][mid] > A[max_idx][mid + 1]:
                return [max_idx, mid]
            elif A[max_idx][mid - 1] < A[max_idx][mid] < A[max_idx][mid + 1]:
                lo = mid
            elif A[max_idx][mid - 1] > A[max_idx][mid] > A[max_idx][mid + 1]:
                hi = mid
            else:
                hi = mid

        return [-1, -1]
