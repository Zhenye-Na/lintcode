# 150. Best Time to Buy and Sell Stock II

**Description**

Given an array `prices`, which represents the price of a stock in each day.

You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, if you already have the stock, you must sell it before you buy again).

Design an algorithm to find the maximum profit.

**Example**

Example 1:

```
Input: [2, 1, 2, 0, 1]
Output: 2
Explanation: 
1. Buy the stock on the second day at 1, and sell the stock on the third day at 2. Profit is 1.
2. Buy the stock on the 4th day at 0, and sell the stock on the 5th day at 1. Profit is 1.
Total profit is 2.
```

Example 2:

```
Input: [4, 3, 2, 1]
Output: 0
Explanation: No transaction, profit is 0.
```

**Greedy**

https://www.youtube.com/watch?v=tofVYSGUUXY

针对数组每一个值, 看它紧挨着的前一个元素是不是比他小, 如果是的话, 那就可以算在收益里面, 最后累加

```python
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
```