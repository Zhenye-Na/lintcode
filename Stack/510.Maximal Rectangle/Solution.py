class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        area = 0
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return area

        height = [0 for _ in range(len(matrix[0]))]
        for row in matrix:
            for idx, elem in enumerate(row):
                height[idx] = height[idx] + 1 if elem else 0
            area = max(area, self._findMaxArea(height))

        return area

    def _findMaxArea(self, height):
        max_area = 0
        stack = []

        for i in range(len(height) + 1):
            cur = -1 if i == len(height) else height[i]

            while stack and height[stack[-1]] >= cur:
                h = height[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max(max_area, w * h)

            stack.append(i)

        return max_area
