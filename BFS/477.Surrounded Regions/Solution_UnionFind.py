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

