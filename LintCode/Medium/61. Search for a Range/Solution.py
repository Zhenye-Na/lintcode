class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0 or A[0] > target or A[-1] < target:
            return [-1, -1]

        index1 = self.binarySearch(A, target, True)
        index2 = self.binarySearch(A, target, False)

        return [index1, index2]


    def binarySearch(self, A, target, flag):
        start, end = 0, len(A) - 1

        while (start + 1 < end):
            mid = (start + end) / 2

            if A[mid] == target:
                # flag == True -> Find First Position
                if (flag):
                    end = mid
                # flag == False -> Find Last Position
                else:
                    start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid


        if (flag):
            if A[start] == target:
                return start
            elif A[end] == target:
                return end
            else:
                return -1
        else:
            if A[end] == target:
                return end
            elif A[start] == target:
                return start
            else:
                return -1
