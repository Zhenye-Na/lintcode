class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        self.triplets = []
        if not numbers or len(numbers) < 3:
            return self.triplets

        numbers.sort()
        i = 0
        while i < len(numbers):
            self._twoSum(numbers[i + 1:], - numbers[i])
            i += 1
            while i < len(numbers) and numbers[i] == numbers[i - 1]:
                i += 1

        return self.triplets


    def _twoSum(self, nums, target):

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                self.triplets.append(sorted([-target, nums[left], nums[right]]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
