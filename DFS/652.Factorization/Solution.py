class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        self.results = []
        if not n or n <= 1:
            return self.results

        self._find_factors(n, 2, [])
        return self.results

    def _find_factors(self, n, start, factor):
        if factor:
            factor.append(n)
            self.results.append(factor[:])
            factor.pop()

        for i in range(start, int(math.sqrt(n) + 1)):
            if n % i != 0:
                continue

            factor.append(i)
            self._find_factors(n // i, i, factor)
            factor.pop()
