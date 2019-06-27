class Solution:

    def uniquePaths(self, m, n) -> int:

        steps = [1 for _ in range(n)]

        for _ in range(1, m):
            for i in range(1, n):
                steps[i] = steps[i-1] + steps[i]

        return steps[-1]
