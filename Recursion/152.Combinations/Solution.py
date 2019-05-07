class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if not n or n == 0 or not k or k == 0:
            return [[]]

        self.n = n
        self.k = k
        combinations = []
        self._find_combinations(combinations, [], 1)
        return combinations

    def _find_combinations(self, combinations, tmp, start):
        if len(tmp) == self.k:
            combinations.append(tmp[:])
            return

        for i in range(start, self.n + 1):
            tmp.append(i)
            self._find_combinations(combinations, tmp, i + 1)
            tmp.pop()
