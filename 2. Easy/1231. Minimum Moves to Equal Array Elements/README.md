# 1231. Minimum Moves to Equal Array Elements

Description
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Have you met this question in a real interview?  
Example
Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


```python
import sys

class Solution:
    """
    @param nums: an array
    @return: the minimum number of moves required to make all array elements equal
    """
    def minMoves(self, nums):
        # Write your code here
        result = 0
        minimum = min(nums)
        result = sum([num - minimum for num in nums])
        return result
```
