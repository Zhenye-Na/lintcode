# 143. Sort Colors II

**Description**

Given an array of n objects with `k` different colors (numbered from `1` to `k`), sort them so that objects of the same color are adjacent, with the colors in the order `1, 2, ... k`.

```
You are not suppose to use the library's sort function for this problem.
k <= n
```

**Example**

Example 1

```
Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]
```

Example 2

```
Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]
```

**Challenge**

A rather straight forward solution is a two-pass algorithm using counting sort. That will cost `O(k)` extra memory. Can you do it without using extra memory?

**Rainbow Sort**

```python
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors or len(colors) == 0:
            return

        self._rainbowSort(colors, 0, len(colors) - 1, 1, k)

    def _rainbowSort(self, colors, start, end, startColor, endColor):
        if start == end or startColor == endColor:
            return

        left, right = start, end
        pivot = startColor + (endColor - startColor) // 2
        while left <= right:
            while left <= right and colors[left] <= pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self._rainbowSort(colors, start, right, startColor, pivot)
        self._rainbowSort(colors, left, end, pivot + 1, endColor)
```