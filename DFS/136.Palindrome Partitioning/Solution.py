class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        # write your code here
        results = []
        if not s or len(s) == 0:
            return results

        self._dfs(s, [], results)
        return results

    def _dfs(self, s, tmp, results):
        if len(s) == 0:
            results.append(tmp[:])
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                tmp.append(s[:i])
                self._dfs(s[i:], tmp, results)
                tmp.pop()

    def isPalindrome(self, s):
        return s == s[::-1]
