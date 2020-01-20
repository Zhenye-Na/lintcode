from collections import deque


class Solution:
    """
    @param board: the given board
    @return:  the least number of moves required so that the state of the board is solved
    """

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    target = [["1", "2", "3"], ["4", "5", "0"]]

    def slidingPuzzle(self, board):
        # write your code here
        if not board or len(board) == 0 or len(board[0]) == 0:
            return -1

        initial_state = self.board_to_state(board)
        target_state = self.board_to_state(self.target)

        queue = deque([initial_state])
        history = set([initial_state])

        m, n = len(board), len(board[0])

        steps = 0
        while queue:
            size = len(queue)

            for _ in range(size):
                state = queue.popleft()

                if state == target_state:
                    return steps

                idx = state.find("0")
                x, y = idx // n, idx % n

                for i in range(4):
                    new_x, new_y = x + self.dx[i], y + self.dy[i]

                    if self.isValid(new_x, new_y, m, n):
                        newIdx = new_x * n + new_y
                        new_state = self.swap(state, idx, newIdx)

                        if new_state in history:
                            continue

                        history.add(new_state)
                        queue.append(new_state)


            steps += 1

        return -1

    def swap(self, state, idx, newIdx):
        lst = list(state)
        lst[idx], lst[newIdx] = lst[newIdx], lst[idx]
        return ''.join(lst)

    def board_to_state(self, board):
        state = ""
        for row in board:
            for col in row:
                state += str(col)

        return state

    def isValid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
