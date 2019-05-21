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