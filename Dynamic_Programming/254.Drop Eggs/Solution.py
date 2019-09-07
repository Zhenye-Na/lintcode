class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def dropEggs(self, n):
        # write your code here
        return math.ceil((math.sqrt(8 * n) - 1) / 2)
