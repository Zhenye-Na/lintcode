# 363. Trapping Rain Water

Description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![Trapping Rain Water](https://lintcode-media.s3.amazonaws.com/problem/rainwatertrap.png)


Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Challenge
O(n) time and O(1) memory
O(n) time and O(n) memory is also acceptable.


## Solution

### Two Pointers

```python
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        leftMax, rightMax = 0, 0
        result = 0

        while left < right:
            if heights[left] < heights[right]:
                leftMax = max(heights[left], leftMax)
                result += leftMax - heights[left]
                left += 1
            else:
                rightMax = max(heights[right], rightMax)
                result  += rightMax - heights[right]
                right -= 1

        return result
```


### 九章算法

使用九章算法班中讲过的相向型双指针算法。
整个算法的思想是计算每个位置上可以盛放的水，累加起来。

记录如下几个值：

- left, right => 左右指针的位置
- left_max, right_max => 从左到右和从右到左到 left, right 为止，找到的最大的 height

每次比较 left_max 和 right_max，如果 left_max 比较小，就挪动 left 到 left + 1。与此同时，查看 left 这个位置上能够盛放多少水，这里有两种情况：

- 一种是 `left_max > heights[left]`，这种情况下，水可以盛放 `left_max - heights[left]` 那么多。因为右边有 right_max 挡着，左侧可以到 left_max。
- 一种是 `left_max <= heights[left]`，这种情况下，水无法盛放，会从左侧流走，此时更新 left_max 为 heights[left]

`left_max >= right_max` 的情况类似处理。

时间复杂度：`O(n)`，空间复杂度 `O(1)`

```python
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


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
                if left_max < heights[left]:
                    left_max = heights[left]
                else:
                    water += left_max - heights[left]
                left += 1
            else:
                if right_max < heights[right]:
                    right_max = heights[right]
                else:
                    water += right_max - heights[right]
                right -= 1
                    
        return water
```


### Two Pointers [Failed]

```python
class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights or len(heights) == 0:
            return 0

        # trim input
        # delete increasing section at the front and decreasing section at the end
        left = 0
        while left < len(heights) and heights[left] < heights[left+1]:
            left += 1
        right = len(heights) - 1
        while right > 0 and heights[right - 1] > heights[right]:
            right -= 1

        heights = heights[left: right+1]

        candidates = []
        left, right = 0, 1
        length = len(heights)
        while right < length:
            # increasing section
            if heights[left] < heights[right]:
                right += 1
                left += 1
            elif heights[left] >= heights[right]:
                while right < length and heights[left] >= heights[right]:
                    right += 1
                candidates.append([left, right])
                left, right = right, right + 1

        area = self.calculateArea(candidates, heights)
        return area

    def calculateArea(self, candidates, heights):
        totalArea = 0
        for section in candidates:
            subArea = 0
            print(section)
            subHeights = heights[section[0]: section[1]+1]
            if section[1] == len(heights):
                print(self.second_largest(subHeights))
                lowerbound = min(subHeights[0], self.second_largest(subHeights))
            else:
                lowerbound = min(subHeights[0], subHeights[-1])
            for height in subHeights:
                delta = lowerbound - height
                if delta > 0:
                    subArea += delta
            print(subArea)
            totalArea += subArea
        return totalArea


    def second_largest(self, numbers):
        count = 0
        m1 = m2 = float('-inf')
        for x in numbers:
            count += 1
            if x > m2:
                if x >= m1:
                    m1, m2 = x, m1            
                else:
                    m2 = x
        return m2 if count >= 2 else None
```