# 598. Zombie in Matrix

- **Description**
    - Given a 2D grid, each cell is either a wall `2`, a zombie `1` or people `0` (the number zero, one, two).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies?
    - Return `-1` if can not turn all people into zombies.
- **Example**
    - Given a matrix:

    ```
    0 1 2 0 0
    1 0 0 2 1
    0 1 0 0 0
    ```

    - return 2




## Solution

矩阵中的分层宽度优先搜索

`天数`就是`层数`，用模板即可。注意值的更新即可


### Code

```java
public class Solution {
    /**
     * @param grid: a 2D integer grid
     * @return: an integer
     */
    
    private int[] dx = {0,0,1,-1};
    private int[] dy = {1,-1,0,0};

    private static final int PEOPLE = 0;
    private static final int ZOMBIE = 1;
    private static final int WALL = 2;


    private class coordinate {
        public int X;
        public int Y;
        public coordinate(int x, int y) {
            X = x;
            Y = y;
        }
        
    }
    
    public int zombie(int[][] grid) {
        // write your code here
        if (grid == null || grid.length == 0 || grid[0].length == 0) return -1;
        
        int row = grid.length;
        int col = grid[0].length;
        int numPeople = 0;
        
        Queue<coordinate> queue = new LinkedList<>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == ZOMBIE) {
                    queue.offer(new coordinate(i, j));
                } else if (grid[i][j] == PEOPLE) {
                    numPeople++;
                }
            }
        }

        int day = 0;

        while (!queue.isEmpty()) {
            
            day++;
            
            int size = queue.size();
            for (int s = 0; s < size; s++) {

                coordinate zombie = queue.poll();

                for (int index = 0; index < 4; index++) {
                    if ( validate(zombie.X + dx[index], zombie.Y + dy[index], grid)) {
                        queue.offer(new coordinate(zombie.X + dx[index], zombie.Y + dy[index]));
                        grid[zombie.X + dx[index]][zombie.Y + dy[index]] = ZOMBIE;
                        numPeople--;
                        
                        if (numPeople == 0) {
                            return day;
                        }
                    }
                }

            }

        }

        return -1;

    }


    
    // Validate current coordinate is available && whether it is people
    private boolean validate(int x, int y, int[][]grid) {

        int row = grid.length;
        int col = grid[0].length;

        if (x < 0 || x > row - 1) {
            return false;
        }
        if (y < 0 || y > col - 1) {
            return false;
        }

        return (grid[x][y] == PEOPLE);
    }

}
```