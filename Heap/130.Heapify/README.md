# 130. Heapify

**Description**

Given an integer array, heapify it into a *min-heap* array.

For a heap array `A`, `A[0]` is the root of heap, and for each `A[i]`, `A[i * 2 + 1]` is the left child of `A[i]` and `A[i * 2 + 2]` is the right child of `A[i]`.

**Clarification**

**What is heap?**

- Heap is a data structure, which usually have three methods: **push, pop and top**.
- where "`push`" add a new element the heap,
- "`pop`" delete the minimum/maximum element in the heap,
- "`top`" return the minimum/maximum element.

**What is heapify?**

Convert an unordered integer array into a heap array. If it is min-heap, for each element `A[i]`, we will get `A[i * 2 + 1] >= A[i]` and `A[i * 2 + 2] >= A[i]`.

**What if there is a lot of solutions?**

Return any of them.

**Example**

Given `[3,2,1,4,5]`, return `[1,2,3,4,5]` or any legal heap array.

**Challenge**

`O(n)` time complexity


**Recursion**

```python
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        n = len(A)

        # Heapify
        for i in range(n, -1, -1):
            self.helper(A, i)



    def helper(self, A, i):
        lowest = i             # root is the smallest element
        left   = i * 2 + 1     # left child
        right  = i * 2 + 2     # right child

        # Find smallest in left / right / root
        if left < len(A) and A[i] > A[left]:
            lowest = left

        if right < len(A) and A[lowest] > A[right]:
            lowest = right

        if lowest != i:

            # Swap with the smallest
            A[i], A[lowest] = A[lowest], A[i]

            # Re-heapify again
            self.helper(A, lowest)
```


**Iteration**

```java
public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    private void siftdown(int[] A, int k) {
        while (k < A.length) {
            int smallest = k;
            if (k * 2 + 1 < A.length && A[k * 2 + 1] < A[smallest]) {
                smallest = k * 2 + 1;
            }
            if (k * 2 + 2 < A.length && A[k * 2 + 2] < A[smallest]) {
                smallest = k * 2 + 2;
            }
            if (smallest == k) {
                break;
            }

            int temp = A[smallest];
            A[smallest] = A[k];
            A[k] = temp;

            k = smallest;
        }
    }

    public void heapify(int[] A) {
        for (int i = A.length / 2; i >= 0; i--) {
            siftdown(A, i);
        }
    }
}
```


`Heapify()` 是 **Heap Sort** 里非常重要的一步


- Heap Sort for decreasing order using `min heap`
- Heap Sort for increasing order using `max heap`

```
Input data: 4, 10, 3, 5, 1

         4(0)
        /   \
     10(1)   3(2)
    /   \
 5(3)    1(4)

The numbers in bracket represent the indices in the array
representation of data.

Applying heapify procedure to index 1:

         4(0)
        /   \
    10(1)    3(2)
    /   \
5(3)    1(4)

Applying heapify procedure to index 0:

        10(0)
        /  \
     5(1)  3(2)
    /   \
 4(3)    1(4)

The heapify procedure calls itself recursively to build heap
in top down manner.
```