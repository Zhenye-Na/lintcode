class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 0:
            return 0

        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res = res + (prices[i] - prices[i - 1])

        return res