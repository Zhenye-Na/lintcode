class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """

    def increasingTriplet(self, nums):
        # write your code
        if not nums or len(nums) < 3:
            return False

        smallest, second_smallest = sys.maxsize, sys.maxsize
        for num in nums:
            if num <= smallest:
                second_smallest = smallest
                smallest = num

            elif num <= second_smallest:
                second_smallest = num

            else:
                return True

        return False
