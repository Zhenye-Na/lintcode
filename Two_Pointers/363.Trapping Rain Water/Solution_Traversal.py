class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        # Forward-Backward-Traverse
        if not heights or len(heights) <= 1:
            return 0

        # find the highest bar on the left
        left_max, curr_max = [], -1
        for i in range(len(heights)):
            curr_max = max(curr_max, heights[i])
            left_max.append(curr_max)

        # find the highest bar on the right
        right_max, curr_max = [], -1
        for i in range(len(heights) - 1, -1, -1):
            curr_max = max(curr_max, heights[i])
            right_max.append(curr_max)

        # select the lower bar from left_max and right_max
        res, n = 0, len(heights)
        for i in range(len(heights)):
            res += min(left_max[i], right_max[n - 1 - i]) - heights[i]

        return res
