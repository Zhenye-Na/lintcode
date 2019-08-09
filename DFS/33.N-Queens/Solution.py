class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        self.solutions = []
        if not n or n < 0:
            return self.solutions.append([])

        self._dfs(0, n, [])
        results = self._draw_chessboard(n)
        return results

    def _dfs(self, startIndex, n, solution):
        if len(solution) == n:
            self.solutions.append(solution[:])

        for i in range(startIndex, n):
            if self._isValid(solution, i, len(solution)):
                solution.append(i)
                self._dfs(0, n, solution)
                solution.pop()

    def _isValid(self, solution, colIndex, rowIndex):
        for row, col in enumerate(solution):
            if row == rowIndex or col == colIndex:
                return False
            if row + col == rowIndex + colIndex:
                return False
            if row - col == rowIndex - colIndex:
                return False
        return True

    def _draw_chessboard(self, n):
        results = []
        for solution in self.solutions:
            chessboard = []
            for i in range(n):
                row = ['Q' if j == solution[i] else '.' for j in range(n)]
                chessboard.append("".join(row))
            results.append(chessboard)
        return results
