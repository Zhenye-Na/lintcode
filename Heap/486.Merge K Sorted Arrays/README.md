# 486. Merge K Sorted Arrays

**Description**

Given k sorted integer arrays, merge them into one sorted array.

**Example**

Example 1:

```
Input: 
  [
    [1, 3, 5, 7],
    [2, 4, 6],
    [0, 8, 9, 10, 11]
  ]
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

Example 2:

```
Input:
  [
    [1,2,3],
    [1,2]
  ]
Output: [1,1,2,2,3]
```

**Challenge**

Do it in `O(N log k)`.

- `N` is the total number of integers.
- `k` is the number of arrays.


**Heap (PriorityQueue)**

```python
import heapq


class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        result = []
        heap = []
        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heapq.heappush(heap, (array[0], index, 0))
             
        while len(heap):
            val, x, y = heap[0]
            heapq.heappop(heap)
            result.append(val)
            if y + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][y + 1], x, y + 1))
            
        return result

```

**Divide and Conquer**

```python
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

```