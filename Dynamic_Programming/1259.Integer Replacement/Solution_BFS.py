from collections import deque


class Solution:
    """
    @param n: a positive integer 
    @return: the minimum number of replacements
    """

    def integerReplacement(self, n):
        # Write your code here
        steps = 0
        if n == 1:
            return steps

        queue = deque([n])
        while queue:
            size = len(queue)
            print(queue, steps)
            for _ in range(size):
                num = queue.popleft()
                if num == 1:
                    return steps
                if num % 2 == 0:
                    queue.append(num // 2)
                else:
                    queue.append(num + 1)
                    queue.append(num - 1)
            steps += 1

        return 0
