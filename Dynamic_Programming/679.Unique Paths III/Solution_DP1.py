class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        # write your codes here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[set([]) for _ in range(n)] for _ in range(m)]

        dp[0][0].add(grid[0][0])
        for row in range(1, m):
            for path_sum in dp[row - 1][0]:
                dp[row][0].add(path_sum + grid[row][0])
        for col in range(1, n):
            for path_sum in dp[0][col - 1]:
                dp[0][col].add(path_sum + grid[0][col])

        for x in range(1, m):
            for y in range(1, n):
                if x == m - 1 and n == n - 1:
                    continue
                for path_sum in dp[x][y - 1]:
                    dp[x][y].add(path_sum + grid[x][y])
                for path_sum in dp[x - 1][y]:
                    dp[x][y].add(path_sum + grid[x][y])

        return sum(dp[-1][-1])
