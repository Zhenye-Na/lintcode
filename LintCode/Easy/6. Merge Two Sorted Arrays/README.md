# 6. Merge Two Sorted Arrays


- **Description**
    - Merge two given sorted integer array A and B into a new sorted integer array.
- **Example**

    ```
    A=[1,2,3,4]
    B=[2,4,5,6]
    ```

    - return `[1,2,2,3,4,4,5,6]`
- **Challenge**
    - How can you optimize your algorithm if one array is very large and the other is very small?

    
    
## Solution

遍历+比较

### Code

```java
public class Solution {
    /**
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        // write your code here
        if (A == null || B == null) {
            return null;
        }
        
        int alength = A.length;
        int blength = B.length;
        
        int[] result = new int[alength + blength];
        int i = 0, j = 0, index = 0;
        
        while (i < alength && j < blength) {
            if (A[i] < B[j]) {
                result[index++] = A[i++];
            } else {
                result[index++] = B[j++];
            }
        }
        
        while (i < alength) {
            result[index++] = A[i++];
        }
        while (j < blength) {
            result[index++] = B[j++];
        }
        
        return result;

    }
}
```