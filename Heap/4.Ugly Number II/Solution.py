from heapq import heappush, heappop


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        pq = []
        history = set()
        history.add(1)
        heappush(pq, 1)

        count, res = 0, -1
        while count < n:
            res = heappop(pq)
            count += 1
            nums = [res * 2, res * 3, res * 5]
            for i in nums:
                if i not in history:
                    history.add(i)
                    heappush(pq, i)

        return res
