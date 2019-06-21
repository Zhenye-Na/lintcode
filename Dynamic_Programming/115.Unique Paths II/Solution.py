class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    OBSTACLE = 1
    EMPTY = 0

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # state: dp[x][y] represents how may unique paths which can reach point (x, y)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initialization: start position
        dp[0][0] = 1 if obstacleGrid[0][0] == self.EMPTY else -1

        # function: dp[x][y] = dp[x - 1][y] + dp[x][y - 1] if not obstacle
        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
                    if dp[x][y] == -1:
                        return 0
                    else:
                        continue

                if obstacleGrid[x][y] == self.OBSTACLE:
                    dp[x][y] = 0
                else:
                    dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

        # answer: dp[-1][-1] stores how may paths reach to bottom-right point
        return dp[-1][-1]
