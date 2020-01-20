# 76. Longest Increasing Subsequence

**Description**

Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

**Clarification**

What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

**Example**

```
Example 1:
	Input:  [5,4,1,2,3]
	Output:  3
	
	Explanation:
	LIS is [1,2,3]
```

```
Example 2:
	Input: [4,2,4,5,3,7]
	Output:  4
	
	Explanation: 
	LIS is [2,4,5,7]
```

**Challenge**

Time complexity `O(n^2)` or `O(nlogn)`


**解析**

> 两种方法的讲解视频:
> 
> https://www.youtube.com/watch?v=5rfZ4WnNKBk


`O(nlogn)`

*Binary Search*

相反与 DP 的做法, 二分搜索的做法是我们去自己构建一个数组去记录下目前的"上升子序列", 如果新来的数比数组末尾元素要大的话, 那么我们答案长度会增加, 否则就替换掉原数组中的元素.

Python 中自带的 二分搜索是 `bisect`

```python
from bisect import bisect_left

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        arr = [0 for _ in range(len(nums))]

        length = 0
        for num in nums:
            idx = bisect_left(arr, num, 0, length)

            arr[idx] = num

            if idx == length:
                length += 1

        return length
```

`O(n^2)`

*Dynamic Programming*

```python

```

