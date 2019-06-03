# 510. Maximal Rectangle

**Description**

Given a 2D boolean matrix filled with `False` and `True`, find the largest rectangle containing all `True` and return its area.

**Example**

Example 1

```
Input:
[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
Output: 6
```

Example 2

```
Input:
[
    [0,0],
    [0,0]
]
Output: 0
```

**Monotone Stack**

122.Largest Rectangle in Histogram 变种

相当于以每一行作为 Histogram 的横坐标, 将每一列的数字取和, 但要注意, 最后一行是0的话, 这一列要清零!

然后单调栈做法就可以


```python
class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        area = 0
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return area

        height = [0 for _ in range(len(matrix[0]))]
        for row in matrix:
            for idx, elem in enumerate(row):
                height[idx] = height[idx] + 1 if elem else 0
            area = max(area, self._findMaxArea(height))

        return area

    def _findMaxArea(self, height):
        max_area = 0
        stack = []

        for i in range(len(height) + 1):
            cur = -1 if i == len(height) else height[i]

            while stack and height[stack[-1]] >= cur:
                h = height[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                max_area = max(max_area, w * h)

            stack.append(i)

        return max_area
```