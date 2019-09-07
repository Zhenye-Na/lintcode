class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def numWays(self, n, k):
        # write your code here
        if n == 1:
            return k

        if n == 2:
            return k * k

        if k == 1:
            return 0

        # initialization
        # f[i] represents the number of ways to paint first i posts
        f = [0 for _ in range(n + 1)]
        f[0] = 0
        f[1] = k
        f[2] = k * k

        # function: (k - 1) * f[i - 1] + (k - 1) * f[i - 2]
        for i in range(3, n + 1):
            f[i] = (k - 1) * f[i - 1] + (k - 1) * f[i - 2]

        return f[-1]
