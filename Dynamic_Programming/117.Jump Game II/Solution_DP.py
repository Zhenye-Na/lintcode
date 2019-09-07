class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        # write your code here
        # initialization: f[i] represents the min steps to reach i-th index
        f = [sys.maxsize for _ in range(len(A))]
        f[0] = 0

        # function f[i] = min(f[j] + 1) for j in [0, i), if constraints
        for i in range(1, len(A)):
            for j in range(0, i):
                if f[j] != sys.maxsize and j + A[j] >= i:
                    f[i] = min(f[i], f[j] + 1)

        # answer: f[-1] if we can jump to the last index else 0
        return f[-1] if f[-1] != sys.maxsize else 0
