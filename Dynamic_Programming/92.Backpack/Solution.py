class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # state: f[i][j] 从前 i 个取出若干个, 拼成总和为 j
        f = [[False for _ in range(m + 1)] for _ in range(len(A) + 1)]

        # initialization
        f[0][0] = True

        # function: f[i][j]: f[i- 1][j] or f[i][j - A[i]]
        # 取第 i 个数, 那么前 i - 1 个数就要能够拼成 j - A[i]
        # 不取第 i 个数, 那么前 i 个数 已经能够拼成 j

        for i in range(1, len(A) + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j - A[i - 1] >= 0:
                    f[i][j] = f[i - 1][j - A[i - 1]] or f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]

        for idx in range(m, -1, -1):
            if f[-1][idx]:
                return idx
        return 0
