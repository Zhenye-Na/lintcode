class Solution:
    """
    @param n: An integer
    @return: An Integer
    """

    def climbStairs2(self, n):
        # write your code here
        # initialization:
        if n == 0 or n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        # state: dp[i] represents how many steps can reach step i
        # function: dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
