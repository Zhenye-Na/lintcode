class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """

    def getFactors(self, n):
        # write your code here
        self.combinations = []
        if not n or n < 0:
            return []

        self.dfs(2, [], n)
        return self.combinations

    def dfs(self, start, current, target):
        if current:
            current.append(target)
            self.combinations.append(sorted(current[:]))
            current.pop()

        for factor in range(start, int(math.sqrt(target) + 1)):

            if target % factor != 0:
                continue

            current.append(factor)
            self.dfs(factor, current, target // factor)
            current.pop()
