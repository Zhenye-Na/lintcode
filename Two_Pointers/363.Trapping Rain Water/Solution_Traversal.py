class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights or len(heights) == 0:
            return 0

        left_max, left_max_height = [], -1
        for height in heights:
            left_max_height = max(left_max_height, height)
            left_max.append(left_max_height)

        right_max, right_max_height = [], -1
        for height in reversed(heights):
            right_max_height = max(right_max_height, height)
            right_max.append(right_max_height)

        water, n = 0, len(heights)
        for i in range(n):
            water += min(left_max[i], right_max[n - i - 1]) - heights[i]

        return water
