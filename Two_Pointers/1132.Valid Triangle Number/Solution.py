class Solution:
    """
    @param nums: the given array
    @return:  the number of triplets chosen from the array that can make triangles
    """

    def triangleNumber(self, nums):
        # Write your code here
        if not nums or len(nums) == 0:
            return 0

        nums.sort()
        ans = 0

        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1

        return ans
