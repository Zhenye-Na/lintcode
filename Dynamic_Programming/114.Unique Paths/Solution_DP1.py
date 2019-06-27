class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        # state: dp[x][y] represents how many possible unique paths which can reach point (x, y)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initialization: first row and first col have only one path
        dp[0][0] = 1
        for row in range(1, m):
            dp[row][0] = 1
        for col in range(1, n):
            dp[0][col] = 1

        # function: dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

        # answer: dp[-1][-1] stores how may paths reach to bottom-right point
        return dp[-1][-1]
