class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        # initialization:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        # state: dp[i] represents how many ways to reach step i
        # function: dp[i] = dp[i - 1] + dp[i - 2]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # answer: dp[n] represents the number of ways to reach n
        return dp[n]
