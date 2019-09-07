# 111. Climbing Stairs

**Description**

You are climbing a stair case. It takes `n` steps to reach to the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example**

```
Example 1:
	Input:  n = 3
	Output: 3
	
	Explanation:
	1) 1, 1, 1
	2) 1, 2
	3) 2, 1
	total 3.


Example 2:
	Input:  n = 1
	Output: 1
	
	Explanation:  
	only 1 way.
```

```
思路: 基于题目要求，每次只能一次性走一个台阶，或者两个台阶，所以能到第n个台阶的情况只有两种：
1. 从第 n-1 的台阶跨一步到第 n 台阶
2. 从第 n-2 的台阶一次性跨两步到第 n 台阶

定义动态规划函数: f[i] 代表了走到第i个台阶的总共不同的方式个数, 因而有了转移方程 f[i] = f[i - 1] + f[i - 2]

初始值设定: f[0] 代表走到第0个台阶的方式: 1 -> 代表原地不动, f[1] 代表走到第1个台阶的方式：1 -> 代表跨一步
```

```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        # initialization:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        # state: dp[i] represents how many ways to reach step i
        # function: dp[i] = dp[i - 1] + dp[i - 2]
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # answer: dp[n] represents the number of ways to reach n
        return dp[n]
```