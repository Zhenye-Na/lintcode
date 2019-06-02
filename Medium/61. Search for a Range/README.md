# 61. Search for a Range

- **Description**
  - Given a sorted array of n integers, find the starting and ending position of a given target value.
  - If the target is not found in the array, return `[-1, -1]`
- **Example**
  - Given `[5, 7, 7, 8, 8, 10]` and target value `8`,
  - return `[3, 4]`.
- **Challenge**
  - `O(log n)` time


## Solution

一语点醒命中人！

**Find First Position + Find Last Position** 变体 using Binary Search

### Java

```java
public class Solution {
    /**
     * @param A: an integer sorted array
     * @param target: an integer to be inserted
     * @return: a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        // write your code here
        if (A == null || A.length == 0) {
            return new int[]{-1, -1};
        }

        int startIndex, endIndex, start = 0, end = A.length - 1;
        startIndex = binarySearch(A, target, start, end, true);
        endIndex = binarySearch(A, target, start, end, false);

        return new int[]{startIndex, endIndex};
    }


    private int binarySearch(int[] A, int target, int start, int end, boolean flag) {

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (target > A[mid]) {
                start = mid;
            } else if (target < A[mid]) {
                end = mid;
            } else {
                if (flag) {
                    end = mid;
                } else {
                    start = mid;
                }
            }

        }


        if (flag) {
            if (target == A[start]) {
                return start;
            }
            if (target == A[end]) {
                return end;
            }
            return -1;

        } else {
            if (target == A[end]) {
                return end;
            }
            if (target == A[start]) {
                return start;
            }
            return -1;
        }

    }

}
```


### Python


```python
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
```
