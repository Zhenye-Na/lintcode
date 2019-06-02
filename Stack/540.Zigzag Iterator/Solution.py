from collections import deque


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.v1 = deque(v1)
        self.v2 = deque(v2)

        self.flag = 0

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        if self.flag % 2 == 1:
            if self.v1:
                return self.v1.popleft()
            else:
                return self.v2.popleft()
        else:
            if self.v2:
                return self.v2.popleft()
            else:
                return self.v1.popleft()


    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        if len(self.v1) + len(self.v2) > 0:
            self.flag += 1
            return True
        else:
            return False


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result