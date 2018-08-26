class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if len(nums) <= 1:
            return nums

        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i <= 0:
            nums.sort()
            return nums

        # Find successor to pivot
        j = len(nums) - 1
        while nums[j] <= nums[i - 1]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Reverse suffix
        nums[i : ] = nums[len(nums) - 1 : i - 1 : -1]

        return nums





class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if len(nums)<=1:
            return nums
        #从右向左扫过，寻找一个递增序列
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                for k in range(len(nums)-1,i,-1):
                    if nums[k]>nums[i]:
                        nums[i],nums[k]=nums[k],nums[i]
                        nums[i+1:]=sorted(nums[i+1:])
                        break
                break
            else:
                if i==0:
                    nums.sort()
        return nums





#
# Computes the next lexicographical permutation of the specified
# list in place, returning whether a next permutation existed.
# (Returns False when the argument is already the last possible
# permutation.)
#
def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True

# Example:
#   arr = [0, 1, 0]
#   next_permutation(arr)  (returns True)
#   arr has been modified to be [1, 0, 0]
