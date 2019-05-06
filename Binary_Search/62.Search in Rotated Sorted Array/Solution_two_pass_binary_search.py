class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
            
        index = self._find_min_index(A)
        if A[index] <= target <= A[-1]:
            return self._binary_search(A, index, len(A) - 1, target)
        return self._binary_search(A, 0, index - 1, target)
        
    def _find_min_index(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[end]:
                end = mid
            else:
                start = mid
        
        if A[start] < A[end]:
            return start
        return end

    def _binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1