# 373. Partition Array by Odd and Even

- **Description**
    - Partition an integers array into **odd number first and even number second**.
- **Example**
    - Given `[1, 2, 3, 4]`, return `[1, 3, 2, 4]`
- **Challenge**
    - Do it in-place.


## Solution


```java
public class Solution {
    /*
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return;
        
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            
            while (left < right && nums[left] % 2 != 0) {
                left++;
            }

            while (left < right && nums[right] % 2 == 0) {
                right--;
            }
            
            if (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                
            }
        }
    }
}
```