# 189. First Missing Positive

**Description**
Given an unsorted integer array, find the first missing positive integer.
**Example**

Example 1:
```
Input: [1,2,0]
Output: 3
```
Example 2:
```
Input: [3,4,-1,1]
Output: 2
```
Example 3:
```
Input: [7,8,9,11,12]
Output: 1
```
**Challenge**
Your algorithm should run in `O(n)` time and uses `constant space`.



## Solution



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
