class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        leftMax, rightMax = 0, 0
        result = 0

        while left < right:
            if heights[left] < heights[right]:
                leftMax = max(heights[left], leftMax)
                result += leftMax - heights[left]
                left += 1
            else:
                rightMax = max(heights[right], rightMax)
                result += rightMax - heights[right]
                right -= 1

        return result