from collections import deque


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = [deque(vector) for vector in vecs]

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        for i in range(len(self.queue)):
            if self.queue[i]:
                ele = self.queue[i].popleft()
                self.queue.append(self.queue.pop(i))
                break
        return ele

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        for q in self.queue:
            if q:
                return True
        return False

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result