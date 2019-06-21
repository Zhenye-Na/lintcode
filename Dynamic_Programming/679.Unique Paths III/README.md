# 679. Unique Paths III

**Description**

Follow up for "Unique Paths II": http://lintcode.com/en/problem/unique-paths-ii/

Now each grid contains a `value`, so each path also has a `value`. Find the `sum` of all the *unique* values paths.

**Example**

Example 1

```
Input:
[
  [1,1,2],
  [1,2,3],
  [3,2,4]
]
Output:
21
Explanation:
There are 2 unique value path:
[1,1,2,3,4] = 11
[1,1,2,2,4] = 10
```

Example 2

```
Input:
[
    [1,5],
    [4,6]
]
Output: 23
Explanation:
There are 2 unique value path:
[1,5,6] = 12
[1,4,6] = 11
```

**DP Solution 1**

二维 DP 数组, 每个位置是一个 `set()`, 用来存储到 (x, y) 不同的路径和

```python
class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        # write your codes here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[set([]) for _ in range(n)] for _ in range(m)]

        dp[0][0].add(grid[0][0])
        for row in range(1, m):
            for path_sum in dp[row - 1][0]:
                dp[row][0].add(path_sum + grid[row][0])
        for col in range(1, n):
            for path_sum in dp[0][col - 1]:
                dp[0][col].add(path_sum + grid[0][col])

        for x in range(1, m):
            for y in range(1, n):
                if x == m - 1 and n == n - 1:
                    continue
                for path_sum in dp[x][y - 1]:
                    dp[x][y].add(path_sum + grid[x][y])
                for path_sum in dp[x - 1][y]:
                    dp[x][y].add(path_sum + grid[x][y])

        return sum(dp[-1][-1])
```

**DP Solution 2**

每一步存放和的 `set`, 比较容易理解的写法。加*滚动数组*优化。

```python
class Solution:
    def uniqueWeightedPaths(self, grid):
        if not grid or not grid[0]:
            return 0
        
        n, m = len(grid), len(grid[0])
        tmp, sumset = 0, []
        for v in grid[0]:
            tmp += v
            sumset.append({tmp})
        
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    v = sumset[j].pop() + grid[i][j]
                    sumset[j] = {v}
                else:
                    sumset[j] = {grid[i][j] + v for v in sumset[j].union(sumset[j-1])}

        return sum(sumset[m - 1])
```
