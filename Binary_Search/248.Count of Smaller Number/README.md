# 248. Count of Smaller Number

**Description**

Give you an integer array (index from `0` to `n-1`, where `n` is the size of this array, value from `0` to `10000`) and an query list. For each query, give you an integer, return the number of element in the array that are smaller than the given integer.

> We suggest you finish problem `Segment Tree Build` and `Segment Tree Query II` first.

**Example**

```
Example 1:

Input: array =[1,2,7,8,5] queries =[1,8,5]
Output:[0,4,2]
Example 2:

Input: array =[3,4,5,8] queries =[2,4]
Output:[0,1]
```

**Challenge**

Could you use three ways to do it.

- Just loop
- Sort and binary search
- Build Segment Tree and Search.

**Related Problems**

