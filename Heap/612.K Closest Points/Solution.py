import heapq


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        pq = []
        for point in points:
            triplet = [-self._computeDistance(point, origin), -point.x, -point.y]
            heapq.heappush(pq, triplet)
            if len(pq) > k:
                heapq.heappop(pq)

        res = []
        while len(pq) > 0:
            _, x, y = heapq.heappop(pq)
            res.append(Point(-x, -y))

        return res[::-1]


    def _computeDistance(self, point, origin):
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
