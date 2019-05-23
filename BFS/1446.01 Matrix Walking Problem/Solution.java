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