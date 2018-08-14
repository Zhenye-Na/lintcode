# 60. Search Insert Position

- **Description**
    - Given a sorted array and a target value, **return the index if the target is found**.
    - If not, **return the index where it would be if it were inserted in order**.
    - You may assume **NO** duplicates in the array.
- **Example**

    ```python
    [1,3,5,6], 5 -> 2
    [1,3,5,6], 2 -> 1
    [1,3,5,6], 7 -> 4
    [1,3,5,6], 0 -> 0
    ```

- **Challenge**
    - `O(log(n))` time


## Solution

要求 `O(log(n))` time，用 Binary Search


### Python

```python
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if (A == None or len(A) == 0):
            return 0

        start, end = 0, len(A) - 1
        while (start + 1 < end):
            mid = (end - start) // 2 + start

            if (A[mid] == target):
                return mid
            elif (A[mid] < target):
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        return len(A)
```


### Java

```java
public class Solution {
    /**
     * @param A: an integer sorted array
     * @param target: an integer to be inserted
     * @return: An integer
     */
    public int searchInsert(int[] A, int target) {
        // write your code here
        if (A == null || A.length == 0) return 0;
        int start = 0, end = A.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (target == A[mid]) {
                return mid;
            } else if (target > A[mid]) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (target <= A[start]) {
            return start;
        } else if (target == A[end]) {
            return end;
        } else if (target > A[end]) {
            return end + 1;
        } else {
            return start + 1;
        }
    }
}
```
