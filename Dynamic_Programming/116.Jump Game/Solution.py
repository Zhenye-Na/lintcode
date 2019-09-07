class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        # initialization: we can jump to the first position
        # dp[i] represents whether we can jump to the i-th position
        dp = [False for _ in range(len(A))]
        dp[0] = True

        # Sequence DP
        # function: f[i] <- f[j] j < i, dp[j] == True, j + A[j] >= i
        for i in range(1, len(A)):
            for j in range(0, i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break  # no longer need to change value of dp[i], break

        # answer: dp[-1]
        return dp[-1]
