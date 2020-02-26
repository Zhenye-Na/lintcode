# 151. Best Time to Buy and Sell Stock III

**Description**

Say you have an array for which the `ith` element is the price of a given stock on day `i`.

Design an algorithm to find the maximum profit. You may complete *at most two* transactions.

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

**Example**

Example 1

```
Input : [4,4,6,1,1,4,2,5]
Output : 6
```

**Forward and Backward Traverse**

> 从前到后扫一次, 从后向前扫一次

因为两次交易不可以"相交", 所以我们可以用分割线的思想:

遍历分割线, 分别对左右两边进行 `Best Time to Buy and Sell Stock I` 的做法, 然后求出每一个分割线对应的最大值

但是时间复杂度这样计算的话是 `O(n^2)`

所以我们:

1. 从左到右, 计算分割线左侧的 max profit
2. 从右到左, 计算分割线右侧的 max profit
3. 计算总和, 求出最大的


```python
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
```

***

@Tin 大佬的答案

```
什么五个状态，三维数组的，不是很好理解而且面试时能重现的几率低，除非你前一天晚上又背了一遍。

把状态设置成每个阶段的获利很不利于思考。而转换一下思考方位，只关注你的股票账户的现金数会更自然。

这题可以这么理解：你账户里的现金最多有四种状态：1. 第一次满仓，2. 第一次清仓，3。第二次满仓，4.第二次清仓。分别用 h1，s1，h2，s2 代表。 h是hold，s是sold。

这里我们用空手套白狼的手法，即借钱买股票，因为反正知道股票的未来价格，稳定赚钱。

第一次满仓时，是借钱买股票，那天买，就欠那天价格数的钱，目标是用最低价格买进，所以要孜孜以求的把它置为最小，求反就是max
这个式子是 h1 = max(h1, -price)
满仓的初始值设为股票最高价的负数，也就是你最多需要借那么多钱，苹果股票最高1000块，你最多借1000块，长虹股票最高5块，你最多负债5块，多了也用不了。
有人习惯上来就是-inf，或 -sys.maxsize，太糙。

其它同理，第一次清仓，你账户里的现金应该是当天卖掉股票的成交价格冲抵你的余额(欠的钱)，当然，这要和以前的最优的(余额最高)的额度比，没以前高，就别清仓了。

这个式子是 s1 = max(s1, price + h1)

以此类推，可以把2扩展到k。

注: 你要是拷贝去 lintcode，要加上这行: if not prices: return 0
lintcode 纯脆是胡搞，输入为空有什么意义？面试时是绝不用写的，更面试官说一声，你假设输入有意义就好。面试官更在意你抓紧时间展示你的思维和分析。
```

```python
# 本参考程序来自九章算法，由 @Tin 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:

    def maxProfit(self, prices) -> int:

        h1 = h2 = - max(prices) 
        s1 = s2 = 0 
        for price in prices:
            s2,                 h2,                 s1,                 h1 = \
            max(s2, price+h2),  max(h2, -price+s1), max(s1, price+h1),  max(h1, -price) 

        return s2
```
