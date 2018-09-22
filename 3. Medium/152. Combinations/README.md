# 152. Combinations

Description
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You don't need to care the order of combinations, but you should make sure the numbers in a combination are sorted.

Have you met this question in a real interview?  
Example
Given n = 4 and k = 2, a solution is:

```
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4]
]
```


## Solution

### Backtracking

```python
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def __init__(self):
        self.result = []
    
    def combine(self, n, k):
        # write your code here
        if n == 0 or k == 0:
            return self.result

        self.helper([], n, k, 1, k)
        return self.result


    def helper(self, combo, n, k, start, l):
        if len(combo) == l:
            self.result.append(combo[:])
            return
        
        for i in range(start, n+1):
            combo.append(i)
            self.helper(combo, n, k-1, i+1, l)
            combo.pop()
```



