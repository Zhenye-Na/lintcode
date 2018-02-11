# 159. Find Minimum in Rotated Sorted Array

- **Description**:
    - Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    - (i.e., `[0 1 2 4 5 6 7]` might become `[4 5 6 7 0 1 2]`).
- **Find the minimum element.**
    - You may assume no duplicate exists in the array.
- **Example**:
    - Given `[4, 5, 6, 7, 0, 1, 2]` return `0`

## Solution:

首先这道题可以想到用一个 `for loop`，就可以把最小的找到， 但是时间复杂度是 `O(n)`
去优化一个 `O(n)` 的算法，同时又明确指出是 `Rotated Sorted Array`，所以很自然的想到用 **二分法** 可以解决这道题。

![](http://images.cnitblog.com/blog/466943/201307/07172841-fd38445e08f4416ebe13a0bc861939e8.png)

如图所示，`Rotated Sorted Array` 存在两个上升区间，同时**第二个上升区间的最大值一定小于第一个上升区间的最小值**。那么，我们可以用 `二分法` 将 `nums[mid]` 和图中的 `High` 值进行比较，进而缩小区间。

套用 `二分法` 模板，代码如下：

### Python

```python
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while (start + 1 < end):
            mid = (start + end) // 2

            if (nums[mid] > target):
                start = mid
            elif (nums[mid] < target):
                end = mid


        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]

```

### Java

```java
public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here

        if (nums.length == 0) return -1;

        int start = 0, end = nums.length - 1;
        int target = nums[end];

        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (nums[mid] < target) {
                end = mid;
            } else {
                start = mid;
            }
        }

        if (nums[start] < target) {
            return nums[start];
        } else {
            return nums[end];
        }
    }
}
```
