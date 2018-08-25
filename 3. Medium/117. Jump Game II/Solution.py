class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        jumps = [len(A)] * len(A)
        jumps[0] = 0

        for i in range(1, len(A)):
            for j in range(i):
                if A[j] + j >= i:
                    jumps[i] = min(jumps[i], jumps[j] + 1)

        return jumps[-1]
