class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, height):
        # write your code here
        if not height or len(height) == 0:
            return 0

        area = 0
        stack = []
        for i in range(len(height) + 1):
            cur = -1 if i == len(height) else height[i]
            while stack and height[stack[-1]] >= cur:
                h = height[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                area = max(area, h * w)

            stack.append(i)

        return area
