class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """
    def optimalUtilization(self, A, B, K):
        # write your code here
        if not A or not B:
            return []

        if A[0] + B[0] > K:
            return []

        bestSum = -sys.maxsize
        result = []

        for idx1 in range(len(A)):
            idx2 = self.binarySearch(B, A[idx1], K)

            if idx2 != -1 and A[idx1] + B[idx2] > bestSum:
                result = [idx1, idx2]
                bestSum = A[idx1] + B[idx2]

        return result


    def binarySearch(self, arr, ele, target):
        lo, hi = 0, len(arr) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if arr[mid] + ele == target:
                hi = mid
            elif arr[mid] + ele < target:
                lo = mid
            else:
                hi = mid

        if arr[hi] + ele <= target:
            return hi
        if arr[lo] + ele <= target:
            return lo
        return -1
