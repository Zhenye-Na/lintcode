# 521. Remove Duplicate Numbers in Array

- **Description**
    - Given an array of integers, remove the duplicate numbers in it.
    - You should:
        - Do it in place in the array.
        - Move the unique numbers to the front of the array.
        - Return the total number of the unique numbers.
        - You don't need to keep the original order of the integers.
- **Example**
    - Given `nums = [1,3,1,4,4,2]`, you should:
    - Move duplicate integers to the tail of nums => nums = `[1,3,4,2,?,?]`.
    - Return the number of unique integers in nums => `4`.
    - Actually we don't care about what you place in `?`, we only care about the part which has no duplicate integers.
- **Challenge**
    - Do it in `O(n)` time complexity.
    - Do it in `O(nlogn)` time without extra space.


## Solution


```java
public class Solution {
    /*
     * @param nums: an array of integers
     * @return: the number of unique integers
     */
    public int deduplication(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        Set<Integer> set = new HashSet<>();
        
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            if (!set.contains(nums[left])) {
                set.add(nums[left]);
                left++;
            } else {
                while (left < right && set.contains(nums[left])) {
                    swap(nums, left, right);
                    right--;
                }
            }
        }

        if (!set.contains(nums[left])) {
            return set.size() + 1;
        }
        return set.size();

    }


    private void swap(int[] nums, int left, int right) {
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }

}
```