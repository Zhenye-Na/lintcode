from collections import deque

DIRECTIONS = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]


class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        # # write your code here

        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)

        queue = deque()
        distance = {}

        queue.append(source)
        distance[source] = 0

        while queue:
            size = len(queue)

            for _ in range(size):

                node = queue.popleft()
                if node == target:
                    return distance[node]

                for neighbor in self.get_neighbors(node):
                    if neighbor in distance:
                        continue

                    queue.append(neighbor)
                    distance[neighbor] = distance[node] + 1

        return -1

    def matrix_to_string(self, matrix):
        seq = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                c = str(matrix[i][j])
                seq.append(c)

        return "".join(seq)

    def get_neighbors(self, seq):
        neighbors = []
        zeroIndex = seq.find("0")

        x = zeroIndex // 3
        y = zeroIndex % 3

        for dx, dy in DIRECTIONS:
            seq_list = list(seq)
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue

            seq_list[zeroIndex], seq_list[nx * 3 +
                                          ny] = seq_list[nx * 3 + ny], seq_list[zeroIndex]
            neighbor = "".join(seq_list)
            neighbors.append(neighbor)

        return neighbors
