# 1791. Simple queries

**Description**


Give you two arrays, the first array may contains repeatable integers, The second array is a sub of the first array.The length of the returned array is the same as the second array. For each element a in the second array, how many numbers are in the first array `<= a`.

**Example**

Example 1:

```
Input: nums = [3, 2, 4, 3, 5, 1],sub = [2, 4]
Output: [2, 5] 
Explanation: <=2 numbers are [1,2], <= 4 numbers are [1,2,3,3,4]
```

Example 2:

```
Input: nums = [3, 1, 2, 3, 3, 1], sub = [1,3]
Output: [2, 6] 
Explanation: <= 1 numbers are [1,1], <=3 numbers are [1,1,2,3,3,3]
```
