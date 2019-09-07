# 76. Longest Increasing Subsequence

**Description**

Given a sequence of integers, find the longest <u>increasing subsequence</u> (*LIS*).

You code should return the length of the *LIS*.

**Clarification**

> **What's the definition of longest increasing subsequence?**

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence


**Example**

Example 1:

```
Input:  [5,4,1,2,3]
Output:  3

Explanation:
LIS is [1,2,3]
```

Example 2:

```
Input: [4,2,4,5,3,7]
Output:  4

Explanation: 
LIS is [2,4,5,7]
```

**Challenge**

Time complexity $O(n^2)$ or $O(n \log n)$


**Dynamic Programming**

*Sequence DP*

牢记 4 个要素, 状态转移方程

$O(n^2)$ 解法：

- `Dp[i]` 表示以第 `i` 个数字为结尾的最长上升子序列的长度。
- 对于每个数字，枚举前面所有小于自己的数字 `j`，`Dp[i] = max{Dp[j]} + 1`. 如果没有比自己小的，`Dp[i] = 1`;

```python
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        # initialization
        # f[i] represents the max length of increasing subsequence which ends with nums[i]
        n = len(nums)
        f = [1 for _ in range(n)]

        # function: f[i] <- f[j] with contraints on j < i, nums[i] > nums[j]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)

```

*Follow Up*: print the longest increasing subsequence

```python
# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0

        # state: dp[i] 表示从左到右跳到 i 的最长 sequence 的长度

        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)

        # prev[i] 代表 dp[i] 的最优值是从哪个 dp[j] 算过来的
        prev = [-1] * len(nums)

        # function dp[i] = max{dp[j] + 1},  j < i and nums[j] < nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        # answer: max(dp[0..n-1])
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i

        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])

        return longest
```



**Binary Search**

$O(n \log n)$ 解法：

使用一个辅助空间B数组。

`B[i]`存储Dp值为i的最小的数字。（有多个位置，以这些位置为结尾的LIS长度都为i， 则这些数字中最小的一个存在B[i]中）

则B数组严格递增。且下标表示LIS长度，也是严格递增，可以在B数组中进行二分查找。

对于每个位置i，我们要找，所有小于`A[i]`, 且Dp值最大的那个。这个操作在B数组中二分查找。


```java
public class Solution {
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        int[] minLast = new int[nums.length + 1];
        minLast[0] = Integer.MIN_VALUE;
        for (int i = 1; i <= nums.length; i++) {
            minLast[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < nums.length; i++) {
            // find the first number in minLast >= nums[i]
            int index = binarySearch(minLast, nums[i]);
            minLast[index] = nums[i];
        }

        for (int i = nums.length; i >= 1; i--) {
            if (minLast[i] != Integer.MAX_VALUE) {
                return i;
            }
        }

        return 0;
    }

    // find the first number > num
    private int binarySearch(int[] minLast, int num) {
        int start = 0, end = minLast.length - 1;
        while (start + 1 < end) {
            int mid = (end - start) / 2 + start;
            if (minLast[mid] < num) {
                start = mid;
            } else {
                end = mid;
            }
        }

        return end;
    }
}
```
