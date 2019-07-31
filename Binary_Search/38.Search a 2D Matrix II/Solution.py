class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix1(self, matrix, target):
        # write your code here
        count = 0

        if not matrix or not target:
            return count

        m, n = len(matrix), len(matrix[0])
        x, y = m - 1, 0
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                count += 1
                y += 1
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                x -= 1

        return count

    def searchMatrix2(self, matrix, target):
        # write your code here
        if not matrix or not target:
            return 0

        count = 0
        for row in matrix:
            for col in row:
                if col == target:
                    count += 1
                    break
        return count
