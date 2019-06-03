import heapq


class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.pq = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.pq, num)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return heapq.nlargest(self.k, self.pq)
