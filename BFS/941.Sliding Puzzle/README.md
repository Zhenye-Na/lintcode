# 941. Sliding Puzzle

**Description**

On a `2x3` board, there are `5` tiles represented by the integers `1` through `5`, and an empty square represented by `0`.

A move consists of choosing `0` and a `4-directionally` adjacent number and swapping it.

The state of the board is solved if and only if the board is `[[1,2,3],[4,5,0]]`.

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return `-1`.

```
board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
```

Example

Example 1:

```
Given board = `[[1,2,3],[4,0,5]]`, return `1`.

Explanation:
Swap the 0 and the 5 in one move.
```

Example 2:

```
Given board = `[[1,2,3],[5,4,0]]`, return `-1`.

Explanation:
No number of moves will make the board solved.
```

Example 3:

```
Given board = `[[4,1,2],[5,0,3]]`, return `5`.

Explanation:
5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
```

Example 4:

```
Given board = `[[3,2,4],[1,5,0]]`, return `14`.
```

**解析**

> **简单无向图已知起点和终点求最短路径问题**

分层 BFS, 问题是"多少步", 这就基本上是 分层BFS, 模板牢记

- 如何交换字符串中两个字符?
    - 把字符串变成 list 然后交换, 再转会成字符串即可
- 使用 set 用来除重


```python
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
```
