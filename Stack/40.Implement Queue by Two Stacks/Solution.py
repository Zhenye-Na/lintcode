class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.s1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        while self.s1:
            self.s2.append(self.s1.pop())
        ele =  self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())

        return ele
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.s1:
            self.s2.append(self.s1.pop())
        ele = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return ele
