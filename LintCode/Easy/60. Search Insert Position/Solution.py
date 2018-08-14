class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if (A == None or len(A) == 0):
            return 0

        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = (end - start) // 2 + start

            if (A[mid] == target):
                return mid
            elif (A[mid] < target):
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)
