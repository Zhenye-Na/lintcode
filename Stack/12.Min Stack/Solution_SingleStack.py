class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, num):

        min_val = min(num, self.stack[-1][1] if self.stack else num)
        self.stack.append((num, min_val))

    def pop(self) -> int:

        val, _ = self.stack.pop()
        return val

    def min(self) -> int:

        _, min_val = self.stack[-1]
        return min_val
