class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, A, target):
        # Write your code here
        if len(A) == 0 or A == None:
            return -1
        
        start = 0
        end = len(A) - 1
        
        if target < A[start] or target > A[end]:
            return -1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            if target == A[mid]:
                return mid
            elif target > A[mid]:
                start = mid
            else:
                end = mid
        
        if target == A[end]:
            return end
        elif target == A[start]:
            return start
        else:
            return -1
