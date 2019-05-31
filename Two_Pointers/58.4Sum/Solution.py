from collections import defaultdict

class Solution:
    """
    @param nums: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        # write your code here
        quadruplets = []
        nums.sort()
        quadruplets = []
        length = len(nums)

        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                total = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > total:
                        right -= 1
                    else:
                        left += 1

        return quadruplets
