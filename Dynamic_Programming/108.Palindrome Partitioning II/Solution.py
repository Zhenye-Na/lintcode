class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        n = len(s)
        isPalindrome = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            isPalindrome[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                isPalindrome[i][i + 1] = True

        for i in range(n - 2, 0, -1):
            for j in range(i, n - 1):
                if isPalindrome[i][j] and s[i - 1] == s[j + 1]:
                    isPalindrome[i - 1][j + 1] = True

        return self.dfs(s, n, 0, isPalindrome, {})

    def dfs(self, s, n, start, isPalindrome, records):
        if start >= len(s):
            return -1

        if start in records:
            return records[start]

        minCut = sys.maxsize
        for end in range(start, n):
            if isPalindrome[start][end]:
                cutsOfRest = self.dfs(s, n, end + 1, isPalindrome, records)
                minCut = min(minCut, cutsOfRest + 1)

        records[start] = minCut

        return minCut
