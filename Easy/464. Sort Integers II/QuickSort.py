import random

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return A
        self.quickSort(A, 0, len(A) - 1)


    def quickSort(self, A, start, end):
        if start >= end:
            return

        pivotIndex = random.randint(start, end)
        pivot = A[pivotIndex]

        left, right = start, end

        while left <= right:

            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]

                left  += 1
                right -= 1

        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
