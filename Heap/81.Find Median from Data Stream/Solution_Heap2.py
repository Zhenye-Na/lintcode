from heapq import heappush, heappop, heappushpop

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        # medians -> return lists
        # min_heap -> elements that are greater than median
        # max_heap -> elements that are less than median
        min_heap, max_heap, medians = [], [], []

        medians.append(nums[0])
        heappush(max_heap, - nums[0])

        for i in range(1, len(nums)):

            if nums[i] <= - max_heap[0]:
                heappush(max_heap, - nums[i])
            else:
                heappush(min_heap, nums[i])

            if len(max_heap) > len(min_heap) + 1:
                heappush(min_heap, - heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heappush(max_heap, - heappop(min_heap))

            medians.append(- max_heap[0])

        return medians
