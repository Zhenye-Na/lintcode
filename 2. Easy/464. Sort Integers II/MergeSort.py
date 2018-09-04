class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        tmp = [0] * len(A)
        self.mergeSort(A, tmp, 0, len(A)-1)


    def mergeSort(self, A, tmp, start, end):
        # base case
        if start >= end:
            return

        mid = (end - start) / 2 + start

        # Divide
        self.mergeSort(A, tmp, start, mid)
        self.mergeSort(A, tmp, mid + 1, end)


        # Conquer / Merge

        idx, leftStart, rightStart = start, start, mid + 1


        while leftStart <= mid and rightStart <= end:
            if A[leftStart] <= A[rightStart]:
                tmp[idx] = A[leftStart]
                leftStart += 1
            else:
                tmp[idx] = A[rightStart]
                rightStart += 1
            idx += 1

        while leftStart <= mid:
            tmp[idx] = A[leftStart]
            idx += 1
            leftStart += 1


        while rightStart <= end:
            tmp[idx] = A[rightStart]
            idx += 1
            rightStart += 1


        for i in range(start, end+1):
            A[i] = tmp[i]
