class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)

        # state: f[i][j] 表示前 i 个数, 取出一些, 能够拼成体积为 j 的最大价值
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # function: f[i][j] = max(f[i - 1][j - A[i - 1]] + V[i - 1], f[i - 1][j])
        # 决策就是第 i 个物品装不装入背包
        for i in range(1, n + 1):
            f[i][0] = 0
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = max(f[i - 1][j - A[i - 1]] + V[i - 1], f[i - 1][j])
                else:
                    f[i][j] = f[i - 1][j]

        return max(f[-1])
