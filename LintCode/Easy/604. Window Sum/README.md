# 604. Window Sum

Description
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Have you met this question in a real interview?  
Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]

## Solution




```java
public class Solution {
    /**
     * @param nums: a list of integers.
     * @param k: length of window.
     * @return: the sum of the element inside the window at each moving.
     */
    public int[] winSum(int[] nums, int k) {
        // write your code here
        if (nums == null || nums.length < k || k <= 0) return new int[0];
        
        int length = nums.length;
        int[] prefixSum = new int[length + 1];
        int sum = 0;

        // Prefix Sum array
        for (int i = 0; i < length; i++) {
            sum += nums[i];
            prefixSum[i + 1] = sum;
        }
        
        
        int[] result = new int[length - k + 1];
        for (int i = 0; i < length - k + 1; i++) {
            result[i] = prefixSum[i + k] - prefixSum[i];
        }

        return result;
    }
}
```