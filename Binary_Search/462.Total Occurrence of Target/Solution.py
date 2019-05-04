class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A or len(A) == 0 or not target:
            return 0

        first_index = self._find_first_position(A, target)
        last_index  = self._find_last_position(A, target)
 
        if last_index == -1 or first_index == -1:
            return 0
 
        return last_index - first_index + 1
 
    def _find_first_position(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                # A[mid] > target
                end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


    def _find_last_position(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[end] == target:
            return end
        if A[start] == target:
            return start
        return -1
