class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors or len(colors) == 0:
            return

        self._rainbowSort(colors, 0, len(colors) - 1, 1, k)

    def _rainbowSort(self, colors, start, end, startColor, endColor):
        if start == end or startColor == endColor:
            return

        left, right = start, end
        pivot = startColor + (endColor - startColor) // 2
        while left <= right:
            while left <= right and colors[left] <= pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self._rainbowSort(colors, start, right, startColor, pivot)
        self._rainbowSort(colors, left, end, pivot + 1, endColor)
