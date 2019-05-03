class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or target is None:
            return False

        flat_matrix = [item for row in matrix for item in row]

        start, end = 0, len(flat_matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if flat_matrix[mid] == target:
                return True
            elif flat_matrix[mid] < target:
                start = mid
            else:
                end = mid


        if flat_matrix[start] == target or flat_matrix[end] == target:
            return True
        else:
            return False
