# 114. Unique Paths

**Description**

A robot is located at the top-left corner of a `m x n` grid.

The robot can only move either `down` or `right` at any point in time. The robot is trying to reach the `bottom-right` corner of the grid.

How many possible unique paths are there?

`m` and `n` will be at most 100.

**Example**

Example 1:

```
Input: n = 1, m = 3
Output: 1	
Explanation: Only one path to target position.
```

Example 2:

```
Input:  n = 3, m = 3
Output: 6	
Explanation:
	D : Down
	R : Right
	1) DDRR
	2) DRDR
	3) DRRD
	4) RRDD
	5) RDRD
	6) RDDR
```

**DP 1**

```python
class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        # state: dp[x][y] represents how many possible unique paths which can reach point (x, y)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initialization: first row and first col have only one path
        dp[0][0] = 1
        for row in range(1, m):
            dp[row][0] = 1
        for col in range(1, n):
            dp[0][col] = 1

        # function: dp[x][y] = dp[x - 1][y] + dp[x][y - 1]
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x - 1][y] + dp[x][y - 1]

        # answer: dp[-1][-1] stores how may paths reach to bottom-right point
        return dp[-1][-1]
```

**DP 2**

滚动数组优化

```python
class Solution:
    
    def uniquePaths(self, m, n) -> int:
        
        steps = [1 for _ in range(n)]
        
        for _ in range(1, m):
            for i in range(1, n):
                steps[i] = steps[i-1] + steps[i]
                
        return steps[-1]
```