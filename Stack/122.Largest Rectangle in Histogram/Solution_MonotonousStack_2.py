class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, heights):
        indices_stack = []
        area = 0

        for index, height in enumerate(heights + [0]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                # 如果列表尾部高度大于当前高度
                popped_index = indices_stack.pop()
                left_index = indices_stack[-1] if indices_stack else -1

                # 如果列表为空，则宽度为index，否则为 index- indices_stack[-1] - 1
                width = index - left_index - 1
                area = max(area, width * heights[popped_index])

            # 压入列表中
            indices_stack.append(index)

        return area
