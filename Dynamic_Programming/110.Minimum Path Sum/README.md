# 110. Minimum Path Sum

**Description**

Given a `m x n` grid filled with non-negative numbers, find a path from `top-left` to `bottom-right` which minimizes the sum of all numbers along its path.

You can only go `right` or `down` in the path..

Example

```
Example 1:
	Input:  [[1,3,1],[1,5,1],[4,2,1]]
	Output: 7
	
	Explanation:
	Path is: 1 -> 3 -> 1 -> 1 -> 1


Example 2:
	Input:  [[1,3,2]]
	Output: 6
	
	Explanation:  
	Path is: 1 -> 3 -> 2
```

```python
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])

        # state: 从起点走到 (x, y) 路径最小和
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # initialization
        dp[0][0] = grid[0][0]
        for col in range(1, n):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        # function: dp[x][y] = min(dp[x][y - 1], dp[x - 1][y]) + grid[x][y]
        # 从两个方向来的路径取最小值
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = min(dp[x][y - 1], dp[x - 1][y]) + grid[x][y]

        return dp[-1][-1]
```