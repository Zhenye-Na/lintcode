# 189. First Missing Positive

- **Description**
    - Given an unsorted integer array, find the first missing positive integer.
- **Example**

    - Example 1:

    ```
    Input: [1,2,0]
    Output: 3
    ```

    - Example 2:

    ```
    Input: [3,4,-1,1]
    Output: 2
    ```

    - Example 3:

    ```
    Input: [7,8,9,11,12]
    Output: 1
    ```

- **Challenge**
    - Your algorithm should run in `O(n)` time and uses `constant space`.



## Solution

首先要读懂题意，这道题是所有的 `Array` 都是从 `1` 开始的，按照 `1，2，3，4， ....` 排列下去，而不是说 `[7,8,9,11,12]` 的 first missing positive number is `10`

- 位置正确的数不变 `A[i] == i + 1`
- 位置不正确的把它放到应该在的位置 `A[i] != A[A[i] - 1]`
- 超出范围的数，不动 `A[i] > 0 or A[i] <= len(A)`


### Python

```python
class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 1

        for i in range(len(A)):
            # Make sure A[i] is in range(1, len(A) + 1),if A[i] is not supposed to be at index i, then move it to the correct index/ position
            while A[i] > 0 and A[i] <= len(A) and A[i] != A[A[i] - 1]:
                # Swap two numbers
                self.switch(A, i, A[i] - 1)

        # Find the first missing positive integer
        for idx, num in enumerate(A):
            if num != idx + 1:
                return idx + 1

        # All the integers are not missing in the array, return the next number
        return len(A) + 1

    def switch(self, A, start, end):
        tmp = A[start]
        A[start] = A[end]
        A[end] = tmp
```


### Java

```java
public class Solution {
    /**
     * @param nums: An array of integers
     * @return: An integer
     */
    public int firstMissingPositive(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 1;

        int length = nums.length;
        for (int i = 0; i < length; i++) {
            while (nums[i] > 0 && nums[i] <= length && nums[i] != nums[nums[i] - 1]) {
                int tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
        }

        for (int j = 0; j < length; j++) {
            if (nums[j] != j + 1) {
                return j + 1;
            }
        }
        return length + 1;

    }
}

```
