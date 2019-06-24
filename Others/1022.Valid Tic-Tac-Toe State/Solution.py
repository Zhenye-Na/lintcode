class Solution:
    """
    @param board: the given board
    @return: True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game
    """
    def validTicTacToe(self, board):
        # Write your code
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False

        # check players order
        count_X, count_O = 0, 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    count_X += 1
                elif board[i][j] == "O":
                    count_O += 1

        if not (count_X == count_O or count_X == count_O + 1):
            return False

        # check rows if there is a winner
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == 'X':
                    return count_X == count_O + 1
                if board[i][0] == 'O':
                    return count_X == count_O

        # check cols if there is a winner
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == 'X':
                    return count_X == count_O + 1
                if board[0][j] == 'O':
                    return count_X == count_O

        # check one diagnal if there is a winner
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 'X':
                return count_X == count_O + 1
            if board[0][0] == 'O':
                return count_X == count_O

        # check another diagnal if there is a winner
        if board[0][2] == board[1][1] == board[2][0]:
            if board[2][0] == 'X':
                return count_X == count_O + 1
            if board[2][0] == 'O':
                return count_X == count_O

        return True
