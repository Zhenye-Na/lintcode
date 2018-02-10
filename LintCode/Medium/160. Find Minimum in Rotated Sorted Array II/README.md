# 160. Find Minimum in Rotated Sorted Array II


- **Description**
    - Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    - i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`.
    - Find the minimum element.
    - The array **may contain duplicates**.
- **Example**
    - Given `[4,4,5,6,7,0,1,2]` return `0`.


## Solution

### Exhaustive Search

```java
/**
* 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
* - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
* - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
* - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
* - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
*/

// version 1: just for loop is enough
public class Solution {
    public int findMin(int[] num) {
        //  这道题目在面试中不会让写完整的程序
        //  只需要知道最坏情况下 [1,1,1....,1] 里有一个0
        //  这种情况使得时间复杂度必须是 O(n)
        //  因此写一个for循环就好了。
        //  如果你觉得，不是每个情况都是最坏情况，你想用二分法解决不是最坏情况的情况，那你就写一个二分吧。
        //  反正面试考的不是你在这个题上会不会用二分法。这个题的考点是你想不想得到最坏情况。
        int min = num[0];
        for (int i = 1; i < num.length; i++) {
            if (num[i] < min)
                min = num[i];
        }
        return min;
    }
}
```

### Binary Search `&&` Two Pointers

```java
public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        int l = 0, r = nums.length - 1, m, ans = nums[0];
        while(l < r && nums[l] == nums[r]) {
            ++l;
            --r;
        }
        ans = Math.min(ans, nums[l]);
        while(l <= r) {
            m = l + (r - l) / 2;
            if(nums[m] < nums[0]) {
                ans = Math.min(ans, nums[m]);
                r = m - 1;
            }
            else
                l = m + 1;
        }
        return ans;
    }
}
```

### Binary Search

```java
public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;

            if (nums[mid] == nums[end]) {
                end--;
            } else if (nums[mid] > nums[end]) {
                start = mid;
            } else {
                end = mid;
            }

        }

        if (nums[start] <= nums[end]) {
            return nums[start];
        } else {
            return nums[end];
        }


    }
}

```

```python
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1

        while (start + 1 < end):
            mid = (start + end) / 2

            if (nums[mid] > nums[end]):
                start = mid
            elif (nums[mid] < nums[end]):
                end = mid
            else:
                end = end - 1

        return nums[start] if nums[start] < nums[end] else nums[end]

```