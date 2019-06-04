class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if not arrays or len(arrays) == 0:
            return arrays

        new_array = self._mergeKArrays(arrays, 0, len(arrays) - 1)
        return new_array


    def _mergeKArrays(self, arrays, start, end):
        if start == end:
            return arrays[start]

        mid = start + (end - start) // 2

        left = self._mergeKArrays(arrays, start, mid)
        right = self._mergeKArrays(arrays, mid + 1, end)
        return self._merge(left, right)

    def _merge(self, a, b):
        merged = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1

        while i < len(a):
            merged.append(a[i])
            i += 1

        while j < len(b):
            merged.append(b[j])
            j += 1

        return merged
