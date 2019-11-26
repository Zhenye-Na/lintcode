class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.value_stack = []
        self.min_stack = []

    def push(self, number):
        """
        @param: number: An integer
        @return: nothing
        """
        # write your code here
        self.value_stack.append(number)
        if len(self.min_stack) == 0 or number <= self.min_stack[-1]:
            self.min_stack.append(number)

    def pop(self):
        """
        @return: An integer
        """
        # write your code here
        element = self.value_stack.pop()
        if element == self.min_stack[-1]:
            self.min_stack.pop()
        return element

    def min(self):
        """
        @return: An integer
        """
        # write your code here
        return self.min_stack[-1]
