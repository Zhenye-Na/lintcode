class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        j, counter = 0, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                counter = 1
            else:
                # nums[i] == nums[j]
                if counter < 2:
                    j += 1
                    nums[j] = nums[i]
                    counter += 1
        return j + 1

    def removeDuplicatesSolution2(self, nums):
        # write your code here
        left, right = 2, 2
        
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left - 2]:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                
        return left