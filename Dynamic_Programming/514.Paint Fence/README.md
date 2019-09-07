# 514. Paint Fence

**Description**

There is a fence with `n` posts, each post can be painted with one of the `k` colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

> `n` and `k` are non-negative integers.

**Example**

Example 1:

```
Input: n=3, k=2  
Output: 6
Explanation:
          post 1,   post 2, post 3
    way1    0         0       1 
    way2    0         1       0
    way3    0         1       1
    way4    1         0       0
    way5    1         0       1
    way6    1         1       0
```

Example 2:

```
Input: n=2, k=2  
Output: 4
Explanation:
          post 1,   post 2
    way1    0         0       
    way2    0         1            
    way3    1         0          
    way4    1         1       
```

**Dynamic Programming**

采用动态规划的思想。

- `dp[i] = (k-1) × (dp[i-1]+dp[i-2])`
- `dp[i-1] × (k-1)` 代表当前格子的颜色和前一个不同的方案
- `dp[i-2] × (k-1)` 代表当前格子的颜色和前一个相同的方案

```python
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def numWays(self, n, k):
        # write your code here
        if n == 1:
            return k

        if n == 2:
            return k * k

        if k == 1:
            return 0

        # initialization
        # f[i] represents the number of ways to paint first i posts
        f = [0 for _ in range(n + 1)]
        f[0] = 0
        f[1] = k
        f[2] = k * k

        # function: (k - 1) * f[i - 1] + (k - 1) * f[i - 2]
        for i in range(3, n + 1):
            f[i] = (k - 1) * f[i - 1] + (k - 1) * f[i - 2]

        return f[-1]
```