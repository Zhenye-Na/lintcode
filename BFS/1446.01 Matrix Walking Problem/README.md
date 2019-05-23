# 1446. 01 Matrix Walking Problem

**Description**

Given an `0 1` matrix gird of size `n * m`, `1` is a wall, `0` is a road, now you can turn **a** `1` in the grid into `0`, Is there a way to go from the upper left corner to the lower right corner? If there is a way to go, how many steps to take at least?


```​​
1 <= n <= 10^3
1 <= m <= 10^3
```


**Example**

Example 1:

```
Input: a = [[0,1,0,0,0],[0,0,0,1,0],[1,1,0,1,0],[1,1,1,1,0]] 
Output: 7 
Explanation: Change `1` at (0,1) to `0`, the shortest path is as follows:
(0,0)->(0,1)->(0,2)->(0,3)->(0,4)->(1,4)->(2,4)->(3,4) There are many other options of length `7`, not listed here.
```

Example 2:

```
Input: a = [[0,1,1],[1,1,0],[1,1,0]] 
Output: -1 
Explanation: Regardless of which `1` is changed to `0`, there is no viable path.
```

**BFS 1**

```
朴素做法：对于每个是1的点修改成0， 做BFS，然后回溯；
时间复杂度N^4, 数据给到1000，N^3都会超时（OJ可能会让你过， 面试肯定不行）， 所以我们要思考N^2的做法。

解法如下:
两次BFS:

1. 从0，0（左上）开始BFS，记录0,0到达所有可拓展点的距离。（碰到1还是要记录， 但是1不能继续向外拓展）；
2. 从M - 1, N - 1（右下） 开始BFS， 。。。。。同上

因为1不能往外拓展，所以很多被包在中间的1的距离矩阵是不会被更新的， 所以有些点的距离矩阵还是 Integer.MAX_VALUE, 表示不可到达。

然后得到两个记录距离的矩阵，

srcToDes矩阵：从左上出发到达每个点的距离（初始Integer.MAX_VALUE表示不可到达）
DesToSrc矩阵：从右下出发到达每个点的距离（初始Integer.MAX_VALUE表示不可到达）

做完两次BFS得到初始点，终点到达每个点的距离

之后枚举每个点， 如果左上和右下都可以到达这个点（一开始设置为Integer.MAX_VALUE) 如果可以拓展到这个点，
值会被修改。 如果两个矩阵都可以到达该点， 那么更新最短距离。

if m 接近于 n
时间复杂度： N^2
空间复杂度： N^2
```

```java
/**
* 本参考程序来自九章算法，由 @Iris 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/ 

public class Solution {
    /**
     * @param grid: The gird
     * @return: Return the steps you need at least
     */
    public int getBestRoad(int[][] grid) {
        // Write your code here
        int[] dirs = {0, 1, 0, -1, 0};
        int m = grid.length, n = grid[0].length;
        int[][] srcToDes = new int[m][n];
        int[][] DesToSrc = new int[m][n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                srcToDes[i][j] = Integer.MAX_VALUE;       
                DesToSrc[i][j] = Integer.MAX_VALUE;
            }
        }

        bfs(0, 0, grid, dirs, srcToDes);
        bfs(m - 1, n - 1, grid, dirs, DesToSrc);

        int minDist = Integer.MAX_VALUE;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (srcToDes[i][j] != Integer.MAX_VALUE && DesToSrc[i][j] != Integer.MAX_VALUE) {
                    minDist = Math.min(minDist, srcToDes[i][j] + DesToSrc[i][j]);
                }       
            }
        }

        return minDist == Integer.MAX_VALUE ? -1: minDist;
    }

    private void bfs(int startX, int startY, int[][] grid, int[] dirs, int[][] distMatrix) {

        int m = grid.length, n = grid[0].length;
        Queue<Integer> q = new LinkedList<>();
        q.offer(startX * n + startY);

        boolean[][] visited = new boolean[m][n];
        visited[startX][startY] = true;
        distMatrix[startX][startY] = 0;

        int dist = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            dist++;
            while (size-- != 0) {
                int cur = q.poll();
                int x = cur / n;
                int y = cur % n;
                
                for (int i = 0; i < 4; ++i) {
                    int nx = x + dirs[i];
                    int ny = y + dirs[i + 1];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        distMatrix[nx][ny] = dist;
                        
                        if (grid[nx][ny] != 1) {
                            q.offer(nx * n + ny);
                        }
                    }
                }
            }
        }
    }
}
```

**BFS 2**

從起點跟終點都BFS一遍，紀錄距離。

假設起點走不到終點，起點範圍裡面的值也會因為終點BFS的距離紀錄矩陣是sys.maxsize而被忽略。


```python
from collections import deque
import sys

class Solution:
    """
    @param grid: The gird
    @return: Return the steps you need at least
    """
    def getBestRoad(self, grid):
        # Write your code here
        m, n = len(grid), len(grid[0])
        src = [ [sys.maxsize] * n for _ in range(m)] 
        dst = [ [sys.maxsize] * n for _ in range(m)] 

        self.bfs(grid, src, m, n, True)
        self.bfs(grid, dst, m, n, False)

        minDis = sys.maxsize
        for i in range(m):
            for j in range(n):
                if src[i][j] != sys.maxsize and dst[i][j] != sys.maxsize:
                    minDis = min(minDis, src[i][j] + dst[i][j])

        if minDis == sys.maxsize:
            return -1
        else:
            return minDis


    def bfs(self, grid, dis, m, n, isSrc):
        q = deque()

        if isSrc:
            q.append((0, 0))
            dis[0][0] = 0
        else:
            q.append((m - 1, n - 1))
            dis[m - 1][n - 1] = 0

        step = 0
        while q:
            step += 1
            qsize = len(q)
            for _ in range(qsize):
                i, j = q.popleft()
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni = i + di
                    nj = j + dj
                    if self._isValid(ni, nj, m, n, dis):
                        if grid[ni][nj] == 1:
                            dis[ni][nj] = step
                        else:
                            dis[ni][nj] = step
                            q.append((ni, nj))

    def _isValid(self, ni, nj, m, n, dis):
        return 0 <= ni < m and 0 <= nj < n and dis[ni][nj] == sys.maxsize
```