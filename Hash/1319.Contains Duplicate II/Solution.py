class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return: whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """

    def containsNearbyDuplicate(self, nums, k):
        # Write your code here
        if not nums or len(nums) == 0 or k <= 0:
            return False

        # map from value to index
        mapping = {}
        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping[nums[i]] = i
            else:
                if abs(i - mapping[nums[i]]) <= k:
                    return True
                else:
                    mapping[nums[i]] = i

        return False
