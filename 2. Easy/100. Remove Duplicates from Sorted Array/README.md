# 100. Remove Duplicates from Sorted Array

- **Description**
    - Given a sorted array, remove the duplicates **in place** such that each element appear only once and return the new length.
    - **Do not allocate extra space for another array, you must do this in place with constant memory**.
- **Example**
    - Given input array `A = [1,1,2]`,
    - Your function should return `length = 2`, and `A` is now `[1,2]`.


## Solution

### Two Pointers

```java
public class Solution {
    /*
     * @param nums: An ineger array
     * @return: An integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int start = 0, end = nums.length;
        for (int i = 0; i < end; i++) {
            if (nums[i] != nums[start]) {
                nums[++start] = nums[i];
            }
        }
        return start + 1;
    }
}

```