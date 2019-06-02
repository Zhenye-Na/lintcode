# 28. Search a 2D Matrix


- **Description**
    - Write an efficient algorithm that searches for a value in an `m x n` matrix.
    - This matrix has the following properties:
        - Integers in each row are **sorted from left to right**.
        - **The first integer of each row is greater than the last integer of the previous row**.
- **Example**
    - Consider the following matrix:

    ```
    [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    ```

    - Given `target = 3`, return `true`.
- **Challenge**
    - `O(log(n) + log(m))` time


## Solution

1. 把整个 `matrix[][]` flatten 成一个 vector，然后 Binary Search
1. 先 Binary Search 第一列，然后根据结果 Binary Search 某一行


### Python

```python
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or target is None:
            return False

        flat_matrix = [item for row in matrix for item in row]

        start, end = 0, len(flat_matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if flat_matrix[mid] == target:
                return True
            elif flat_matrix[mid] < target:
                start = mid
            else:
                end = mid


        if flat_matrix[start] == target or flat_matrix[end] == target:
            return True
        else:
            return False

```

### Java

```java
public class Solution {
    /**
     * @param matrix: matrix, a list of lists of integers
     * @param target: An integer
     * @return: a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0) return false;

        List<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < matrix.length; i++) {
            // tiny change 1: proper dimensions
            for (int j = 0; j < matrix[i].length; j++) {
                // tiny change 2: actually store the values
                list.add(matrix[i][j]);
            }
        }

        int[] vector = new int[list.size()];
        for (int i = 0; i < vector.length; i++) {
            vector[i] = list.get(i);
        }

        if (binarySearch(target, vector) != -1) {
            return true;
        } else {
            return false;
        }
    }

    // Binary Search
    private int binarySearch(int target, int[] nums) {

        int start = 0, end = nums.length - 1;

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (target == nums[mid]) {
                return mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }

            if (target == nums[start]) {
                return start;
            }

            if (target == nums[end]) {
                return end;
            }

            return -1;
    }


}
```
