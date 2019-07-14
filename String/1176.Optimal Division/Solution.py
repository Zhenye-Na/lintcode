class Solution:
    """
    @param nums: an array
    @return: the corresponding expression in string format
    """

    def optimalDivision(self, nums):
        # Write your code here
        if not nums or len(nums) == 0:
            return ""

        if len(nums) == 1:
            return str(nums[0])

        if len(nums) == 2:
            return "/".join([str(num) for num in nums])

        ans = None
        while len(nums) > 1:
            num = nums.pop()
            if not ans:
                ans = str(num)
            else:
                ans = str(num) + "/" + ans

        return str(nums[-1]) + "/(" + ans + ")"
