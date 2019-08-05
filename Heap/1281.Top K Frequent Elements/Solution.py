from heapq import heappush, heappop
from collections import Counter


class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """

    def topKFrequent(self, nums, k):
        # Write your code here
        if not nums or len(nums) == 0:
            return []

        counter = Counter(nums)
        candidates = []
        for ele in counter:
            if len(candidates) < k:
                heappush(candidates, (counter[ele], ele))
            else:
                heappush(candidates, (counter[ele], ele))
                heappop(candidates)

        res = []
        for count, ele in candidates:
            res.append(ele)

        return res
