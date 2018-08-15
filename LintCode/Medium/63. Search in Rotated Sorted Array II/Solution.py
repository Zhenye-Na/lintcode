class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return False

        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = (end + start) / 2

            if A[start] < A[mid]:
                if A[start] <= target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[start] < A[mid]:
                if A[end] >= target and A[mid] <= target:
                    start = mid
                else:
                    end = mid
            else:
                start += 1


        return True if A[start] == target or A[end] == target else False
