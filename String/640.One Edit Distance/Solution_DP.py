class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        if s == t:
            return False

        if abs(len(s) - len(t)) > 1:
            return False

        n, m = len(s), len(t)
        f = [[0] * (m + 1) for _ in range(2)]

        for j in range(m + 1):
            f[0][j] = j

        for i in range(1, n + 1):
            f[i % 2][0] = i
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    f[i % 2][j] = min(f[(i - 1) % 2][j - 1],
                                      f[(i - 1) % 2][j] + 1, f[i % 2][j - 1] + 1)
                else:
                    f[i % 2][j] = min(f[(i - 1) % 2][j - 1] + 1,
                                      f[(i - 1) % 2][j] + 1, f[i % 2][j - 1] + 1)

        return f[n % 2][m] == 1
