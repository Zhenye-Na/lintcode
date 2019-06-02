class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 1

        for i in range(len(A)):
            # Make sure A[i] is in range(1, len(A) + 1),if A[i] is not supposed to be at index i, then move it to the correct index/ position
            while A[i] > 0 and A[i] <= len(A) and A[i] != A[A[i] - 1]:
                # Swap two numbers
                self.switch(A, i, A[i] - 1)

        # Find the first missing positive integer
        for idx, num in enumerate(A):
            if num != idx + 1:
                return idx + 1

        # All the integers are not missing in the array, return the next number
        return len(A) + 1

    def switch(self, A, start, end):
        tmp = A[start]
        A[start] = A[end]
        A[end] = tmp
