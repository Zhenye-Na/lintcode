class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 1:
            return 1

        if n == 0:
            return 0

        dp = [sys.maxint] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in xrange(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
