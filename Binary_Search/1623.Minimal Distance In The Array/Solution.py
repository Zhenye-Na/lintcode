class Solution:
    """
    @param a: array a
    @param b: the query array
    @return: Output an array of length `b.length` to represent the answer
    """

    def minimalDistance(self, a, b):
        # Write your code here
        sorted_a = sorted(a)
        results = []

        for _b in b:
            results.append(self._findDistance(_b, sorted_a))

        return results

    def _findDistance(self, target, array):
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] <= target:
                start = mid
            else:
                end = mid

        if abs(target - array[start]) <= abs(target - array[end]):
            return array[start]
        else:
            return array[end]
