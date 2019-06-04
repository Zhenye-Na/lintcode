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
        # max_heap -> elements that are less than or equal to median
        max_heap, min_heap, medians = [], [], []

        for num in nums:

            if len(min_heap) == len(max_heap):
                if max_heap and num > - max_heap[0]:
                    num = heappushpop(min_heap, num)
                heappush(max_heap, -num)

            else:
                if num < - max_heap[0]:
                    num = - heappushpop(max_heap, -num)
                heappush(min_heap, num)

            medians.append(- max_heap[0])

        return medians
