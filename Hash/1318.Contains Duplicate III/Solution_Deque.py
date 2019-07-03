from collections import deque


class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @param t: the given t
    @return: whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
    """

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Write your code here
        if not nums or len(nums) == 0 or k <= 0:
            return False

        record = deque([])
        for i in range(k + 1):

            for target in range(nums[i] - t, nums[i] + t + 1):
                if target in record:
                    return True

            record.append(nums[i])

        for j in range(k + 1, len(nums)):
            record.popleft()
            for target in range(nums[j] - t, nums[j] + t + 1):
                if target in record:
                    return True

            record.append(nums[j])

        return False
