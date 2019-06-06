from heapq import heappush, heapreplace

class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        if not arrays or len(arrays) == 0:
            return None

        heap = []
        for array in arrays:
            if not array or len(array) == 0:
                continue

            for num in array:
                if len(heap) >= k:
                    if num > heap[0]:
                        heapreplace(heap, num)
                else:
                    heappush(heap, num)

        return heap[0]
