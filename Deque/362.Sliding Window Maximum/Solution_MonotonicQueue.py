from collections import deque


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums or len(nums) == 0:
            return []

        max_queue, res = deque([]), []
        for i in range(len(nums)):

            while max_queue and nums[i] >= nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(i)

            if i + 1 >= k:
                res.append(nums[max_queue[0]])

            if i + 1 - k == max_queue[0]:
                max_queue.popleft()

        return res
