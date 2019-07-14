# 1308. Factor Combinations

**Description**

Numbers can be regarded as product of its factors. For example,

```
8 = 2 x 2 x 2;
  = 2 x 4.
```

Write a function that takes an integer `n` and return all possible combinations of its factors.

```
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
```

**Example**

Example 1

```
Input: 12
Output: 
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Explanation:
2*6 = 12
2*2*3 = 12
3*4 = 12
```

Example 2

```
Input: 32
Output: 
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
Explanation:
2*16=32
2*2*8=32
2*2*2*4=32
2*2*2*2*2=32
2*4*4=32
4*8=32
```
