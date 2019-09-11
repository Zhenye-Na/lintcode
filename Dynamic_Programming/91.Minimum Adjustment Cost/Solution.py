import sys

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if not A or len(A) == 0:
            return 0

        n, l = len(A), 100

        # state: f[i][k] 表示 A[i] 调整到 k 时的最小调整代价
        f = [[sys.maxsize for _ in range(l + 1)] for _ in range(n + 1)]

        # initialization
        for col in range(l + 1):
            f[0][col] = 0

        # function
        for i in range(1, n + 1):
            for k in range(1, l + 1):
                if f[i - 1][k] != sys.maxsize:
                    for t in range(l + 1):
                        if abs(k - t) <= target:
                            f[i][t] = min(f[i][t], f[i - 1][k] + abs(A[i - 1] - k))

        # find results
        ans = f[n][l]
        for i in range(l + 1):
            if f[n][i] < ans:
                ans = f[n][i]       

        return ans
