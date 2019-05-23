class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        if abs(A[start] - target) < abs(A[end] - target):
            return start
        else:
            return end