# 443. Two Sum - Greater than target
Description
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.

> *使用 O(1) 的额外空间和 O(nlogn) 的时间。*

Have you met this question in a real interview?  
Example
Given numbers = [2, 7, 11, 15], target = 24. Return 1. (11 + 15 is the only pair)

Challenge
Do it in O(1) extra space and O(nlogn) time.



```java
public class Solution {
    /**
     * @param nums: an array of integer
     * @param target: An integer
     * @return: an integer
     */
    public int twoSum2(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);
        int left = 0, right = nums.length - 1, count = 0;

        while (left < right) {

            while (left < right) {
                if (nums[left] + nums[right] > target) {
                    count++;
                }
                left++;
            }

            left = 0;
            right--;

        }
        return count;

    }
}
```




```java
public class Solution {
    /**
     * @param nums: an array of integer
     * @param target: An integer
     * @return: an integer
     */
    public int twoSum2(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);
        int left = 0, right = nums.length - 1, count = 0;

        while (left < right) {

            while (left < right) {
                if (left < right && nums[left] + nums[right] <= target) {
                    left++;
                } else {
                    count += right - left;
                    right--;
                }
            }
        }
        return count;

    }
}

```