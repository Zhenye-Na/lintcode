# 464. Sort Integers II


- **Description**
    - Given an integer array, sort it in ascending order. Use **quick sort, merge sort, heap sort** or any `O(nlogn)` algorithm.
- **Example**
    - Given `[3, 2, 1, 4, 5]`
    - return `[1, 2, 3, 4, 5]`.

## Solution

### Quick Sort

Related problem

- [x] 31. Partition Array

```python
import random

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return A
        self.quickSort(A, 0, len(A) - 1)


    def quickSort(self, A, start, end):
        # base case
        if start >= end:
            return

        pivotIndex = random.randint(start, end)
        pivot = A[pivotIndex]

        left, right = start, end

        while left <= right:

            while left <= right and A[left] < pivot:
                left += 1

            while left <= right and A[right] > pivot:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]

                left  += 1
                right -= 1

        # recursive case
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)

```


### Heap Sort

```python
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        n = len(A)

        for i in xrange(n, -1, -1):
            self.heapify(A, n, i)

        for i in xrange(n - 1, 0, -1):

            # Swap
            A[i], A[0] = A[0], A[i]

            # Re-Heapify
            self.heapify(A, i, 0)


    def heapify(self, A, n, i):
        # Ascending order -> Max Heap
        largest = i
        left    = 2 * i + 1
        right   = 2 * i + 2


        if left < n and A[largest] < A[left]:
            largest = left

        if right < n and A[largest] < A[right]:
            largest = right

        # Swap root with left or right if needed
        if largest != i:

            # Swap
            A[i], A[largest] = A[largest], A[i]

            # Re-Heapify
            self.heapify(A, n, largest)

```
