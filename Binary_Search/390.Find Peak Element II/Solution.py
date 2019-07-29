# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """

    def findPeakII(self, A):
        if not A or not A[0]:
            return None

        return self.find_peak(A, 0, len(A) - 1, 0, len(A[0]) - 1)

    def find_peak(self, matrix, top, bottom, left, right):
        if top + 1 >= bottom and left + 1 >= right:
            for row in range(top, bottom + 1):
                for col in range(left, right + 1):
                    if self.is_peak(matrix, row, col):
                        return [row, col]
            return [-1, -1]

        if bottom - top < right - left:
            col = (left + right) // 2
            row = self.find_col_peak(matrix, col, top, bottom)
            if self.is_peak(matrix, row, col):
                return [row, col]
            if matrix[row][col - 1] > matrix[row][col]:
                return self.find_peak(matrix, top, bottom, left, col - 1)
            return self.find_peak(matrix, top, bottom, col + 1, right)

        row = (top + bottom) // 2
        col = self.find_row_peak(matrix, row, left, right)
        if self.is_peak(matrix, row, col):
            return [row, col]
        if matrix[row - 1][col] > matrix[row][col]:
            return self.find_peak(matrix, top, row - 1, left, right)
        return self.find_peak(matrix, row + 1, bottom, left, right)

    def is_peak(self, matrix, x, y):
        return matrix[x][y] == max(
            matrix[x][y],
            matrix[x - 1][y],
            matrix[x][y - 1],
            matrix[x][y + 1],
            matrix[x + 1][y],
        )

    def find_row_peak(self, matrix, row, left, right):
        peak_val = -sys.maxsize
        peak = []
        for col in range(left, right + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak = col
        return peak

    def find_col_peak(self, matrix, col, top, bottom):
        peak_val = -sys.maxsize
        peak = None
        for row in range(top, bottom + 1):
            if matrix[row][col] > peak_val:
                peak_val = matrix[row][col]
                peak = row
        return peak
