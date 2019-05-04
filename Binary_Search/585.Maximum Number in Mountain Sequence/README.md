# 585. Maximum Number in Mountain Sequence

https://www.lintcode.com/problem/maximum-number-in-mountain-sequence/description

**Description**

Given a mountain sequence of `n` integers which increase firstly and then decrease, find the mountain top.

**Example**

```
Example 1:

Input: nums = [1, 2, 4, 8, 6, 3] 
Output: 8
Example 2:

Input: nums = [10, 9, 8, 7], 
Output: 10
```

**Related Problems**

75.Find Peak Elements


先上升在下降中间一定存在峰值, 没说有没有 duplicate numbers 哦