class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == [] or matrix[0] == []:
            return 0

        number = 0
        for row in matrix:
            if row[0] > target:
                continue
            for elem in row:
                if elem == target:
                    number += 1

        return number
