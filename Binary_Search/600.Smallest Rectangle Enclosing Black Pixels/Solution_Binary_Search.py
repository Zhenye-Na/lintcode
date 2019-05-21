class Solution:
    
    def minArea(self, image, i, j):

        m, n = len(image), len(image[0])

        def is_row_empty(image, row):
            return sum(int(cell)
                       for cell in image[row]) == 0

        def is_col_empty(image, col):
            return sum(
                int(image[i][col]) for i in range(len(image))) == 0

        top = self.bisect_left(image, 0, i, is_row_empty)
        bottom = self.bisect_right(image, i, m, is_row_empty)
        left = self.bisect_left(image, 0, j, is_col_empty)
        right = self.bisect_right(image, j, n, is_col_empty)

        return (right - left + 1) * (bottom - top + 1)

    def bisect_left(self, image, lo, hi, is_file_empty):

        while lo < hi:
            mid = (lo + hi) // 2
            if is_file_empty(image, mid):
                lo += 1
            else:
                hi = mid
        return lo

    def bisect_right(self, image, lo, hi, is_file_empty):

        while lo < hi:
            mid = (lo + hi) // 2
            if is_file_empty(image, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo - 1
