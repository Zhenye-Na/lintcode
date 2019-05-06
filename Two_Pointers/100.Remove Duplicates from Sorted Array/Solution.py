class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        length = len(nums)

        p1, p2 = 0, 1
        while p2 < length:
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
            else:
                while p2 < length and nums[p2] == nums[p1]:
                    p2 += 1
                if p2 < length:
                    p1 += 1
                    nums[p1] = nums[p2]
                    p2 += 1

        return p1 + 1
