# 433. Number of Islands

**Description**

Given a boolean 2D matrix, `0` is represented as the sea, `1` is represented as the island. If two `1` is adjacent, we consider them in the same island. We only consider `up/down/left/right` adjacent.

Find the number of islands.

**Example**

Example 1:

```
Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
```

Example 2:

```
Input:
[
  [1,1]
]
Output:
1
```


**BFS**

```python
from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self._bfs(grid, i, j)
                    islands += 1

        return islands                    
    
    def _bfs(self, grid, x, y):
        queue = deque([(x, y)])
        grid[x][y] = False

        while queue:
            x, y = queue.popleft()

            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y

                if not self.is_valid(grid, next_x, next_y):
                    continue

                queue.append((next_x, next_y))
                grid[next_x][next_y] = False
                
    def is_valid(self, grid, x, y):
        n, m = len(grid), len(grid[0])
        return 0 <= x < n and 0 <= y < m and grid[x][y]
```


**Union Find**

使用老師介紹的Union Find 去解決這個題目，首先要先建立Union Find 這個Class(請依照模版）

然後，假設每個島都是獨立，計算出數量，然後遍歷整個矩陣來連接每個島嶼。

```python
class UnionFind:
    def __init__(self, size):
        self.father = [i for i in range(size)]
        self.num_of_connected_components = 0

    def find(self, x):
        if self.father[x] == x:
            return x

        self.father[x] = self.find(self.father[x])

        return self.father[x]

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a != root_b:
            self.father[root_a] = root_b
            self.num_of_connected_components -= 1

    def query(self):
        return self.num_of_connected_components

    def set_num(self, num):
        self.num_of_connected_components = num
        
    
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        num_of_islands = 0
        # assume each island is isolated and get the number of islands first
        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    num_of_islands += 1

    	union_find = UnionFind(m * n)
        union_find.set_num(num_of_islands)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(m):
            for y in range(n):
                if grid[x][y]:
                    for dx, dy in directions:
                        new_x = x + dx
                        new_y = y + dy

                        if self._is_bound(new_x, new_y, m ,n) and grid[new_x][new_y]:
                            # remember to covert each point in 2D matrix to 1D array
                            # because in union find, we use 1D array to track each component and its root
                            union_find.connect(x * n + y, new_x * n + new_y)

        return union_find.query()
                        
    def _is_bound(self, x, y, m ,n):
        return 0 <= x <= m - 1 and 0 <= y <= n - 1
```

区别是不需要建立一个 set 来区分是否访问过, 因为他必须要访问, 不然怎么 connect 呢?

```python
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def __init__(self):

        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        self.father = {}

    def numIslands(self, grid):
        # write your code here
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        self.father = {i:i for i in range(m * n)}
        self.size = sum([sum(l) for l in grid])

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for k in range(4):
                        x, y = i + self.dx[k], j + self.dy[k]
                        if self._inBound(x, y, m, n, grid):
                            self.union(i * n + j, x * n + y)

        return self.query()

    def _inBound(self, x, y, m, n, grid):
        return 0 <= x < m and 0 <= y < n and grid[x][y]

    def find(self, position):
        path = []
        while position != self.father[position]:
            path.append(position)
            position = self.father[position]

        for p in path:
            self.father[p] = position

        return position

    def union(self, p1, p2):
        root_p1, root_p2 = self.find(p1), self.find(p2)
        if root_p2 != root_p1:
            self.father[root_p1] = root_p2
            self.size -= 1

    def query(self):
        return self.size
```

**DFS**

使用 DFS 的方法进行搜索。
DFS 分为两类：

- 找所有路径的
- 找所有节点的

第一类一般需要回溯，也就是把一个东西标记为使用过以后要把他标记回来。这样才能找到所有的路径。

第二类不需要回溯，因为只需要把所有连通的节点都标记一下即可。

```python
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        self.n, self.m = len(grid), len(grid[0])
        self.visited = [[False] * self.m for _ in range(self.n)]
        
        islands = 0
        for row in range(self.n):
            for col in range(self.m):
                if self.is_island(grid, row, col):
                    self.visited[row][col] = True
                    self.dfs(grid, row, col)
                    islands += 1
                    
        return islands
        
    def is_island(self, grid, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and grid[x][y] and not self.visited[x][y]

    def dfs(self, grid, x, y):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for direction in range(4):
            newx = x + dx[direction]
            newy = y + dy[direction]
            
            if self.is_island(grid, newx, newy):
                self.visited[newx][newy] = True
                self.dfs(grid, newx, newy)
                # no backtracking
```
