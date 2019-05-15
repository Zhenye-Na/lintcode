class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """

    def pathSum(self, nums):
        n, siz = len(nums), 1
        self.ans, self.mx = 0, nums[n - 1] // 100
        for i in range(self.mx - 1):
            siz *= 2
        g = [[-1 for j in range(siz)]for i in range(self.mx)]
        for i in range(n):
            dep, pos = nums[i] // 100, nums[i] // 10 % 10
            g[dep - 1][pos - 1] = nums[i] % 10
        self.dfs(g, 0, 0, 0)
        return self.ans

    def dfs(self, g, d, p, sum):
        if(g[d][p] == -1):
            return
        sum += g[d][p]
        if(d == self.mx - 1 or (g[d + 1][2 * p] == -1 and g[d + 1][2 * p + 1] == -1)):
            self.ans += sum
            return
        self.dfs(g, d + 1, 2 * p, sum)
        self.dfs(g, d + 1, 2 * p + 1, sum)
