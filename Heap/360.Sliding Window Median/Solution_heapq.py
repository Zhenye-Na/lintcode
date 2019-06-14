import heapq

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums or len(nums) == 0:
            return []

        if k > len(nums):
            return []

        if k == 1:
            return nums

        medians = []

        # elemements greater than median
        minHeap = []

        # elements smaller than median
        maxHeap = []

        # initialize
        heapq.heappush(maxHeap, - nums[0])
        for i in range(1, k - 1):
            if nums[i] > - maxHeap[0]:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(maxHeap, - nums[i])


        for i in range(k - 1, len(nums)):
            # add new element
            if nums[i] > - maxHeap[0]:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(maxHeap, - nums[i])
            self._balance(minHeap, maxHeap)

            # append result
            medians.append(- maxHeap[0])

            # remove left-wise element
            if nums[i + 1 - k] > - maxHeap[0]:
                minHeap.remove(nums[i + 1 - k])
                heapq.heapify(minHeap)
            else:
                maxHeap.remove(- nums[i + 1 - k])
                heapq.heapify(maxHeap)
            self._balance(minHeap, maxHeap)

        return medians

    def _balance(self, minHeap, maxHeap):
        while len(maxHeap) > len(minHeap) + 1:
            heapq.heappush(minHeap, - heapq.heappop(maxHeap))

        while len(maxHeap) < len(minHeap):
            heapq.heappush(maxHeap, - heapq.heappop(minHeap))
