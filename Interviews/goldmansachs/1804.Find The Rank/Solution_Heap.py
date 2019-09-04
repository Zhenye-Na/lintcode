from heapq import heappush, heappop


class Solution:
    """
    @param scores: two dimensional array
    @param K: a integer
    @return: return a integer
    """

    def FindTheRank(self, scores, K):
        # write your code here
        heap = []
        for idx, score in enumerate(scores):
            # keep a min-heap with size K
            total = sum(score)
            if len(heap) < K:
                heappush(heap, (total, idx))
            else:
                # len(heap) >= K
                if total >= heap[0][0]:
                    heappop(heap)
                    heappush(heap, (total, idx))

        return heap[0][1]
