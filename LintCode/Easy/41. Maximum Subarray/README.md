# 41. Maximum Subarray

- **Description**
    - Given an array of integers, find a **contiguous** subarray which has the largest sum.
    - The subarray should contain **at least one number**.
- **Example**
    - Given the array `[−2,2,−3,4,−1,2,1,−5,3]`, the contiguous subarray `[4,−1,2,1]` has the largest `sum = 6`.
- **Challenge**
    - Can you do it in **time complexity `O(n)`**?


## Solution

采用 **prefixSum** 的思想，将数组的和保存起来，同时记录当前 `minSum`，以及当前数组的 `sum`。


### Code

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int max = Integer.MIN_VALUE, minSum = 0, sum = 0, length = nums.length;

        // Prefix Sum
        for (int i = 0; i < length; i++) {
            sum += nums[i];
            max = Math.max(max, sum - minSum);
            minSum = Math.min(minSum, sum);
        }

        return max;
    }

}
```