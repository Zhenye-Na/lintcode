class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        first_index, last_index = -1, -1
        
        if A is None or len(A) == 0:
            return [first_index, last_index]

        # find first position
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            first_index = start
        elif A[end] == target:
            first_index = end

        # find last position
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            last_index = end
        elif A[start] == target:
            last_index = start


        return [first_index, last_index]