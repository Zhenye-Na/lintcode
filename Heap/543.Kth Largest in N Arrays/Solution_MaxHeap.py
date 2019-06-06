import heapq

class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        if not arrays:
            return None

        # in order to avoid directly changing the original arrays
        # and remove the empty arrays, we need a new sortedArrays
        sortedArrays = []
        for arr in arrays:
            if not arr:
                continue
            sortedArrays.append(sorted(arr, reverse=True))

        maxheap = [
            (-arr[0], index, 0)
            for index, arr in enumerate(sortedArrays)
        ]
        heapq.heapify(maxheap)

        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(maxheap)
            num = - num
            if y + 1 < len(sortedArrays[x]):
                heapq.heappush(maxheap, (-sortedArrays[x][y + 1], x, y + 1))

        return num