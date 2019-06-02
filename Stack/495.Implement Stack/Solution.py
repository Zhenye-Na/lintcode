class Stack:
    s = []

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.s.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.s.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.s[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.s) == 0
