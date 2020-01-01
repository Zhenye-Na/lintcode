class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        if not A or len(A) == 0:
            return -1

        A.sort()

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid % 2 == 0:
                if A[mid] != A[mid + 1]:
                    right = mid
                else:
                    left = mid
            else:
                if mid >= 1 and A[mid] != A[mid - 1]:
                    right = mid
                else:
                    left = mid

        return A[left] if left % 2 == 0 else A[right]
