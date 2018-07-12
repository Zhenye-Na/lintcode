# 433. Number of Islands

- **Description**
    - Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
    - Find the number of islands.
- **Example**
    - Given graph:

    ```java
    [
      [1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1]
    ]
    ```

    - return `3`.


## Solution

采用 BFS in Matrix，遍历所有矩阵中的值，如果 `grid[i][j] == true`，那么判定 这是一个 island，那么对这个点进行 BFS （原因是对这个点BFS相当于找到它临街的所有点中，同样也是 island 的点）同步更新之前 BFS 过得 点的值 `true -> false`，数据结构用 `queue`。


### Code

```java
public class Solution {
    /**
     * @param grid: a boolean 2D matrix
     * @return: an integer
     */

    private class coordinate {
        public int X;
        public int Y;
        public coordinate(int x, int y) {
            X = x;
            Y = y;
        }
        
    }

    // coordinates
    public int[] dx = {1, -1, 0, 0};
    public int[] dy = {0, 0, 1, -1};
    
    public int numIslands(boolean[][] grid) {
        // write your code here
        int num = 0;
        if (grid == null || grid.length == 0) return num;

        int row = grid.length;
        int col = grid[0].length;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == true) {
                    BFS(grid, i, j);
                    num += 1;
                }
            }
        }

        return num;
    }

    
    // BFS in matrix
    private void BFS(boolean[][]grid, int x, int y) {

        int row = grid.length;
        int col = grid[0].length;

        Queue<coordinate> queue = new LinkedList<coordinate>();
        grid[x][y] = false;   // reset to false, in case of duplicating

        // Get neighbors of current position
        for (int index = 0; index < 4; index++) {
            if (validate(x + dx[index], y + dy[index], row, col)) {
                coordinate co = new coordinate(x + dx[index], y + dy[index]);
                queue.add(co);
            }
        }
        
        
        // BFS templates
        while (!queue.isEmpty()) {
            coordinate val = queue.poll();            
            if (grid[val.X][val.Y] == true) {
                BFS(grid, val.X, val.Y);
            }
        }

    }


    // Validate current coordinate is available
    private boolean validate(int x, int y, int row, int col) {
        if (x < 0 || x > row - 1) {
            return false;
        }
        
        if (y < 0 || y > col - 1) {
            return false;
        }
        
        return true;
    }

}
```