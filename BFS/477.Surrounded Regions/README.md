# 477. Surrounded Regions

**Description**

Given a 2D board containing `'X'` and `'O'` (the letter `"O"`), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`'s into `'X'`'s in that surrounded region.

**Example**

Example 1:

```
Input:
  X X X X
  X O O X
  X X O X
  X O X X
Output:
  X X X X
  X X X X
  X X X X
  X O X X
Example 2:

Input:
  X X X X
  X O O X
  X O O X
  X O X X
Output:
  X X X X
  X O O X
  X O O X
  X O X X
```

**Union Find**

如果不是被 `"X"` 全部包住就不能变成 `"O"`

所以先从整个矩形最外层的2行2列开始, 找到 `O` 就标注成一个临时的变量, 最后遍历, O 变成 X, 临时变量变回 O


```python
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if not board or len(board) == 0 or len(board[0]) == 0:
            return

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        m, n = len(board), len(board[0])
        self.father = {i : i for i in range(m * n + 1)}

        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    continue
                
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    self._connect(i * n + j, m * n)
                else:
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if board[x][y] == "O":
                            self._connect(i * n + j, x * n + y)

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O" and self._find(x * n + y) != m * n :
                    board[x][y] = "X"


    def _find(self, loc):
        path = []
        while loc != self.father[loc]:
            path.append(loc)
            loc = self.father[loc]

        for l in path:
            self.father[l] = loc

        return loc

    def _connect(self, loc1, loc2):
        cluster1 = self._find(loc1)
        cluster2 = self._find(loc2)
        if cluster2 != cluster1:
            self.father[min(cluster2, cluster1)] = max(cluster2, cluster1)
```


**BFS**


```python
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        queue = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
                board[r][c] = "D"
                queue.append((r - 1, c)); queue.append((r + 1, c))
                queue.append((r, c - 1)); queue.append((r, c + 1))
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "D":
                    board[r][c] = "O"
```