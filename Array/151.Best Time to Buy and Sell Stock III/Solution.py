class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0

        forward_prices, backward_prices = [0 for _ in range(len(prices))], [0 for _ in range(len(prices))]
        
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            forward_prices[i] = max(forward_prices[i - 1], prices[i] - min_price)

        max_price = prices[-1]
        for j in range(len(prices) - 2, -1, -1):
            max_price = max(prices[j], max_price)
            backward_prices[j] = max(backward_prices[j + 1], max_price - prices[j])

        res = 0
        for i in range(len(prices)):
            res = max(res, forward_prices[i] + backward_prices[i])

        return res