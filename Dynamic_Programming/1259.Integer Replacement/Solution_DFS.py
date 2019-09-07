class Solution:
    """
    @param n: a positive integer 
    @return: the minimum number of replacements
    """

    def integerReplacement(self, n):
        # Write your code here
        ans = {}
        return self.dfs(ans, n)

    def dfs(self, ans, n):
        if n == 1:
            return 0

        if n in ans:
            return ans[n]

        if n % 2 == 0:
            ans[n] = self.dfs(ans, n // 2) + 1
        else:
            ans[n] = min(self.dfs(ans, n + 1), self.dfs(ans, n - 1)) + 1

        return ans[n]
