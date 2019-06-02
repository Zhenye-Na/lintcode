class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        n = len(A)

        for i in xrange(n, -1, -1):
            self.heapify(A, n, i)

        for i in xrange(n - 1, 0, -1):

            # Swap
            A[i], A[0] = A[0], A[i]

            # Re-Heapify
            self.heapify(A, i, 0)


    def heapify(self, A, n, i):
        # Ascending order -> Max Heap
        largest = i
        left    = 2 * i + 1
        right   = 2 * i + 2


        if left < n and A[largest] < A[left]:
            largest = left

        if right < n and A[largest] < A[right]:
            largest = right

        # Swap root with left or right if needed
        if largest != i:

            # Swap
            A[i], A[largest] = A[largest], A[i]

            # Re-Heapify
            self.heapify(A, n, largest)
