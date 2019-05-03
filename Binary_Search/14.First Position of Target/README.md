# 14. First Position of Target

**Description**

For a given sorted array (ascending order) and a target number, find the first index of this number in `O(log n)` time complexity.

If the target number does not exist in the array, return `-1`.

**Example**

```
Example 1:
	Input:  [1,4,4,5,7,7,8,9,9,10]，1
	Output: 0
	
	Explanation: 
	the first index of  1 is 0.

Example 2:
	Input: [1, 2, 3, 3, 4, 5, 10]，3
	Output: 2
	
	Explanation: 
	the first index of 3 is 2.

Example 3:
	Input: [1, 2, 3, 3, 4, 5, 10]，6
	Output: -1
	
	Explanation: 
	Not exist 6 in array.

```

**Challenge**

If the count of numbers is bigger than `2^32`, can your code work properly?



## Solution

`Binary Search`

要找到第一个 `position`，那么就只需要改变 `target == nums[mid]` 时，要把 `end = mid` 也就是 `end` 指针向左移动，因为要找到 **First Position** 所以光找到不能停，因为可能在前面还有重复的。

### Python

```python
class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0 or target == None:
            return 0

        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = (start + end) // 2

            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
```


### Java


```java
public class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        // write your code here

        int start = 0, end = nums.length - 1;

        while (start + 1 < end) {

            int mid = (end - start) / 2 + start;

            if (target == nums[mid]) {
                end = mid;
            } else if (target < nums[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }


        if (target == nums[start]) return start;
        if (target == nums[end]) return end;

        return -1;

    }
}
```
