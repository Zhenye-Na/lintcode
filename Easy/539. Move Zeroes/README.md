# 539. Move Zeroes

- **Description**
    - Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    - You must do this in-place without making a copy of the array.
    - Minimize the total number of operations. 
- **Example**
    - Given `nums = [0, 1, 0, 3, 12]`, after calling your function, nums should be `[1, 3, 12, 0, 0]`.

    
## Solution

```java
public class Solution {
    /**
     * @param nums: an integer array
     * @return: nothing
     */
    public void moveZeroes(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return;
        
        int left = 0, right = 0, length = nums.length;
        while (right < length) {
            if (nums[right] != 0) {
                int temp = nums[left];
                nums[left++] = nums[right];
                nums[right] = temp;
            }
            right++;
        }
        
    }
}
```