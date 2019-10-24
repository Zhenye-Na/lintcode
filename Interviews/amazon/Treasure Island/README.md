# Treasure Island

References: https://leetcode.com/discuss/interview-question/347457

**Description**

You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a *shortest route* to the treasure island.

Assume the map area is a two dimensional `grid`, represented by a matrix of characters. You must start from the <u>top-left</u> corner of the map and can move one block `up`, `down`, `left` or `right` at a time. The treasure island is marked as `X` in a block of the matrix. `X` will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as `D`. You must not enter dangerous blocks. You cannot leave the map area. Other areas `O` are safe to sail in. The top-left corner is always safe. Output the *minimum* number of steps to get to the treasure.


**Example**

```
Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
```

**Solution**

```python
from collections import deque

class Solution:

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def treasureIsland(self, island):
        # Output the *minimum* number of steps to get to the treasure
        if not island or len(island) == 0 or len(island[0]) == 0:
            return 0

        m, n = len(island), len(island[0])

        queue = deque([(0, 0)])
        history = set([(0, 0)])
        steps = 1
        while queue:
            steps += 1
            size = len(queue)
            for j in range(size):
                x, y = queue.popleft()
                for i in range(4):
                    new_x, new_y = x + self.dx[i], y + self.dy[i]
                    if self.isValid(new_x, new_y, m, n, island, history):
                        queue.append((new_x, new_y))
                        history.add((new_x, new_y))
                        if island[new_x][new_y] == "X":
                            return steps - 1

        return 0


    def isValid(self, x, y, m, n, island, history):
        return 0 <= x < m and  0 <= y < n and island[x][y] != "D" and (x, y) not in history


sol = Solution()
island = [
    ['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']
]
print(sol.treasureIsland(island))
```