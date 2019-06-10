class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        n = len(A)
        for i in range(n, -1, -1):
            self.helper(A, i)

    def helper(self, A, i):
        lowest = i             # root is the smallest element
        left   = i * 2 + 1     # left child
        right  = i * 2 + 2     # right child

        # Find smallest in left / right / root
        if left < len(A) and A[i] > A[left]:
            lowest = left

        if right < len(A) and A[lowest] > A[right]:
            lowest = right

        if lowest != i:

            # Swap with the smallest
            A[i], A[lowest] = A[lowest], A[i]

            # Re-heapify again
            self.helper(A, lowest)
