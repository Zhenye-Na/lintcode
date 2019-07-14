# 1487. Judging Triangle

Description

Given an array `arr`, ask if you can find `3` elements from the array as the sides of the three sides, so that the three sides can form a triangle. If yes, return yes, if not, return no


- $1 \leq n \leq 100000$
- $1 \leq arr[i] \leq 1000000000$
- The program will be run `500` times


**Example**

Example 1:

```
Input: arr=[2,3,5,8]
Output: "no"
Explanation:
2, 3, 5 cannot form a triangle
2, 3, 8 cannot form a triangle
3, 5, 8 cannot form a triangle
So, return "no"
```

Example 2:

```
Input: arr=[3,4,5,8]
Output: "yes"
Explanation:
3, 4, 5 can form a triangle
So return "yes"
```

**Two Pointers**

```python
class Solution:
    """
    @param arr: The array
    @return: yes or no
    """

    def judgingTriangle(self, arr):
        # Write your code here
        if not arr or len(arr) == 0:
            return "no"

        n = len(arr)
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    return "yes"
                else:
                    left += 1

        return "no"
```