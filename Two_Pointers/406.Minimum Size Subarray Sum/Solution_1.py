class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        length = sys.maxsize
        total, right = 0, 0

        for left in range(len(nums)):
            while right < len(nums) and total < s:
                total += nums[right]
                right += 1

            if total >= s:
                length = min(length, right - left)

            total -= nums[left]

        return -1 if length == sys.maxsize else length