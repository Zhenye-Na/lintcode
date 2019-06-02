# 608. Two Sum II - Input array is sorted

- **Description**
    - Given an array of integers that is already sorted **in ascending order**, find two numbers such that they add up to a specific target number.
    - The function twoSum should return indices of the two numbers such that they add up to the target, **where index1 must be less than index2**. Please note that your returned answers (both index1 and index2) are **not zero-based**.
    - You may assume that each input would have exactly one solution.
- **Example**
    - Given `nums = [2, 7, 11, 15]`, `target = 9`
    - return `[1, 2]`



## Solution

- **双向指针，一头一尾** （因为数组是升序的），**相向而行**。如果两数之和加起来 `> target`, 说明 `right` 指针的数取得太大了，`right--`, 相反则 `left++`, `==target` 返回。
- （assuming there is only one pair of result）, 时间复杂度 `O(n)`

```java
public class Solution {
    /**
     * @param nums: an array of Integer
     * @param target: target = nums[index1] + nums[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] nums, int target) {
        // write your code here
        if (nums == null || nums.length == 0) return new int[2];
        
        int left = 0, right = nums.length - 1;
        
        while (left < right) {
            
            if (nums[left] + nums[right] == target) {
                return new int[]{left + 1, right + 1};
            } else if (nums[left] + nums[right] > target) {
                right--;
            } else {
                left++;
            }
        }

        return new int[2];
    }
}
```

- 也可以用 `HashMap` 来做，记录每一个值与 `target` 差值，如果刚又有一个跟 `nums` 里的 `element` 值相等的就是答案

```java
public class Solution {
    /**
     * @param nums: an array of Integer
     * @param target: target = nums[index1] + nums[index2]
     * @return: [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        int length = nums.length;
        for (int i = 0; i < length; i++) {
            if (map.get(nums[i]) != null) {
                int[] result = {map.get(nums[i]) + 1, i + 1};
                return result;
            }
            map.put(target - nums[i], i);
        }

        return new int[2];
    }
}
```
