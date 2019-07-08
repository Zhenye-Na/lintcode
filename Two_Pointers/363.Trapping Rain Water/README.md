# 363. Trapping Rain Water

**Description**

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it is able to trap after raining.

![Trapping Rain Water](https://lintcode-media.s3.amazonaws.com/problem/rainwatertrap.png)

**Example**

Example 1:

```
Input: [0,1,0]
Output: 0
```

Example 2:

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Challenge**

- `O(n)` time and `O(1)` memory
- `O(n)` time and `O(n)` memory is also acceptable.


**Two Pointers**

整个算法的思想是计算每个位置上可以盛放的水，累加起来。

记录如下几个值：

- `left`, `right` => 左右指针的位置
- `left_max`, `right_max` => 从左到右和从右到左到 `left`, `right` 为止，找到的最大的 `height`

每次比较 `left_max` 和 `right_max，如果` `left_max` 比较小，就挪动 `left` 到 `left + 1`。

与此同时，查看 `left` 这个位置上能够盛放多少水，这里有两种情况：

- 一种是 `left_max > heights[left]`，这种情况下，水可以盛放 `left_max - heights[left]` 那么多。因为右边有 `right_max` 挡着，左侧可以到 `left_max。`
- 一种是 `left_max <= heights[left]`，这种情况下，水无法盛放，会从左侧流走，此时更新 `left_max` 为 `heights[left]`
- `left_max >= right_max` 的情况类似处理。

时间复杂度：`O(n)`，空间复杂度 `O(1)`


```python
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        water = 0

        while left <= right:
            if left_max < right_max:
                left_max = max(left_max, heights[left])
                water += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                water += right_max - heights[right]
                right -= 1

        return water
```


**Forward-Backward Traversal**

每个位置上的盛水数目 = `min(左侧最高，右侧最高) - 当前高度`

从左到右扫描一边数组，获得每个位置往左这一段的最大值，再从右到左扫描一次获得每个位置向右的最大值。然后最后再扫描一次数组，计算每个位置上的盛水数目。

时间复杂度` O(n)`, 空间复杂度 `O(n)`


```python
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        # Forward-Backward-Traverse
        if not heights or len(heights) <= 1:
            return 0

        # find the highest bar on the left
        left_max, curr_max = [], -1
        for i in range(len(heights)):
            curr_max = max(curr_max, heights[i])
            left_max.append(curr_max)

        # find the highest bar on the right
        right_max, curr_max = [], -1
        for i in range(len(heights) - 1, -1, -1):
            curr_max = max(curr_max, heights[i])
            right_max.append(curr_max)

        # select the lower bar from left_max and right_max
        res, n = 0, len(heights)
        for i in range(len(heights)):
            res += min(left_max[i], right_max[n - 1 - i]) - heights[i]

        return res
```