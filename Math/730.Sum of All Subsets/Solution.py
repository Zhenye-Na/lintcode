class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        # write your code here
        if not n or n == 0:
            return 0

        self.total = 0
        self._find_all_subsets(n, [], 1)
        return self.total

    def _find_all_subsets(self, n, tmp, start):
        self.total += sum(tmp)

        for i in range(start, n + 1):
            tmp.append(i)
            self._find_all_subsets(n, tmp, i + 1)
            tmp.pop()
