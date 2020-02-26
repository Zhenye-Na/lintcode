class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 0:
            return 0

        min_price, res = sys.maxsize, 0
        for price in prices:
            min_price = min(min_price, price)
            res = max(res, price - min_price)

        return res
