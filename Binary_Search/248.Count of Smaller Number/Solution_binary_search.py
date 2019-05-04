class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        if not A or len(A) == 0 or not queries or len(queries) == 0:
            return [0 for i in range(len(queries))]

        A_sorted = A.sort()
        result = [0 for i in range(len(queries))]
        
        for idx, query in enumerate(queries):
            result[idx] = self._binary_search(A, query)

        return result


    def _binary_search(self, A, target):
        if A[-1] < target:
            return len(A)

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return end + 1
