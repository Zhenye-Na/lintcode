class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code hereclass Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        n = len(triangle)

        # state: dp[i][j] 代表从 i,j 走到最底层的最短路径值
        dp = [[0] * (i + 1) for i in range(n)]

        # initialize: 初始化终点（最后一层）
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]

        # function: 从下往上倒过来推导，计算每个坐标到哪儿去
        # dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        # answer: 起点就是答案
        return dp[0][0]
