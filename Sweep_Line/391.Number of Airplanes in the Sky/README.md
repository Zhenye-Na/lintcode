# 391. Number of Airplanes in the Sky

Description

Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

If landing and taking off of different planes happen at the same time, we consider landing should happen at first.

**Example**

Example 1:

```
Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
Output: 3
Explanation:
The first airplane takes off at 1 and lands at 10.
The second ariplane takes off at 2 and lands at 3.
The third ariplane takes off at 5 and lands at 8.
The forth ariplane takes off at 4 and lands at 7.
During 5 to 6, there are three airplanes in the sky.
```

Example 2:

```
Input: [(1, 2), (2, 3), (3, 4)]
Output: 1
Explanation: Landing happen before taking off.
```

**Sweep Line**

将起飞时间和降落时间放到同一个数组中, 标识出是起飞还是降落时间, 然后对数组排序.

遍历数组即可, 碰到起飞计数器加一, 碰到降落计数器减一. 维护最大值作为答案.

注意降落优先于起飞.

算法：**扫描线**

```
每个飞机的状态由其起飞和降落区间决定
确定一个扫描线，从左到右依次扫过每个区间点
遇见起点则飞机数 +1，遇见终点则飞机数 -1，
在同一点有起飞和降落时，先考虑降落在考虑起飞

首先对 interval 中的每一个区间起点终点进行统计和标记
然后根据 index 大小排序，index 相同时根据 sky 排序
最后对所有点 index 进行从小到大的遍历，统计更新 count，取得最大值 max
```

- 时间复杂度: O(nlogn)
- 空间复杂度: O(n)


```python
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes or len(airplanes) == 0:
            return 0

        interval = []
        for airplane in airplanes:
            interval.append([airplane.start, 1])
            interval.append([airplane.end, -1])

        max_num_of_airplane, curr_num = -1, 0
        for timestamp, delta in sorted(interval):
            curr_num += delta
            max_num_of_airplane = max(max_num_of_airplane, curr_num)

        return max_num_of_airplane
```