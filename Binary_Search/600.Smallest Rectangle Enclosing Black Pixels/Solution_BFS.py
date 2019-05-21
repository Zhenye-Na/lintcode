from collections import deque
import sys


class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    WHITE = "0"
    BLACK = "1"

    dX = [1, -1, 0, 0]
    dY = [0, 0, 1, -1]

    def minArea(self, image, x, y):
        # write your code here
        if not image or len(image) == 0 or len(image[0]) == 0:
            return 0

        min_x, max_x = sys.maxsize, - sys.maxsize
        min_y, max_y = sys.maxsize, - sys.maxsize

        m, n = len(image), len(image[0])

        start = [(i, j) for i in range(m) for j in range(n) if image[i][j] == self.BLACK]
        start_x, start_y = start[0]

        queue = deque([(start_x, start_y)])
        history = set((start_x, start_y))

        while queue:
            x, y = queue.popleft()

            # update
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

            for i in range(4):
                new_x, new_y = x + self.dX[i], y + self.dY[i]

                if not self._isValid(new_x, new_y, m, n, image):
                    continue

                if (new_x, new_y) not in history:
                    history.add((new_x, new_y))
                    queue.append((new_x, new_y))

        return (max_x - min_x + 1) * (max_y - min_y + 1)


    def _isValid(self, x, y, m, n, image):
        return 0 <= x < m and 0 <= y < n and image[x][y] == self.BLACK
