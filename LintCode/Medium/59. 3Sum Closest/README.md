# 59. 3Sum Closest
Description
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Have you met this question in a real interview?  
Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Challenge
O(n^2) time, O(1) extra space




## Solution

### Java


```java
public class Solution {
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target: An integer
     * @return: return the sum of the three integers, the sum closest target.
     */
    public int threeSumClosest(int[] numbers, int target) {
        // write your code here
        if (numbers == null || numbers.length < 3) {
            return -1;
        }

        Arrays.sort(numbers);
        int result = Integer.MAX_VALUE;

        for (int i = 0; i < numbers.length; i++) {
            int start = i + 1;
            int end = numbers.length - 1;

            while (start < end) {

                int sum = numbers[i] + numbers[start] + numbers[end];
                if (Math.abs(sum - target) < Math.abs(result - target)) {
                    // Update result
                    result = sum;
                }

                if (sum - target > 0){
                    end--;
                } else {
                    start++;
                }

            }

        }

        return result;
    }
}
```
