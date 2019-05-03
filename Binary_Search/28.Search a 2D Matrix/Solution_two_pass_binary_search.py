class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return -1

        # Binary Search on first column
        first_col = [row[0] for row in matrix]
        indicator, found = self._binary_search_on_col(first_col, target)

        # Binary Search on row if needed
        if found:
            return True
        else:
            return self._binary_search_on_row(matrix[indicator], target)

    def _binary_search_on_col(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return -1, True
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] > target:
            return start - 1, False
        if nums[end] > target:
            return end - 1, False
        else:
            return end, False

    def _binary_search_on_row(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        return True if nums[start] == target or nums[end] == target else False
       