class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        if not A or len(A) == 0:
            return B
        if not B or len(B) == 0:
            return A

        if len(A) < len(B):
            temp = A
            A = B
            B = temp

        # binary search and insert
        for ele in B:
            left = 0
            right = len(A) - 1
            while left + 1 < right:
                mid = int(left + (right - left) / 2)
                if ele < A[mid]:
                    right = mid
                else:
                    left = mid

            if ele < A[left]:
                A.insert(left, ele)
            elif ele > A[right]:
                A.insert(right + 1, ele)
            else:
                A.insert(right, ele)

        return A
