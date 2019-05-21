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