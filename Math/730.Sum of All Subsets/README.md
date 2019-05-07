# 730. Sum of All Subsets

**Description**

Given a number n, we need to find the sum of all the elements from all possible subsets of a set formed by first n natural numbers.

**Example**

```
Example 1:

Input : n = 2
Output : 6
Explanation : 
Possible subsets are {{1}, {2}, {1, 2}}. Sum of elements in subsets
is 1 + 2 + 1 + 2 = 6
```

Example 2:

```
Input : n = 3
Output : 24
Explanation : 
Possible subsets are {{1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
Sum of subsets is : 
1 + 2 + 3 + (1 + 2) + (1 + 3) + 
(2 + 3) + (1 + 2 + 3) = 24
```

**分析**

```
[1]     ==>  0+1=1 // 1出现一次
[1,2]   ==>  0+1+2+(1+2)=6 // 1出现2次, 2出现2次
[1,2,3] ==>  0+1+2+3+(1+2)+(1+3)+(2+3)+(1+2+3)=24 // 1, 2, 3 出现 4次
```

好像有点规律了, 每个元素在求和过程中出现的次数是一样的. 假设出现的次数是N.

`sum = (1+2+3+4+...+n) * N`

N的值又和数组的长度有关系, `N=2^(n-1)`

`sum = (1+2+3+4+...+n) * 2^(n-1)`

```python
class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        # write your code here
        sum = 0
        for i in range(1, n + 1):
            sum += i
        return sum * (int)(math.pow(2, n - 1))

```

正常的 Backtracking 做法, 过不了


```python
class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    def subSum(self, n):
        # write your code here
        if not n or n == 0:
            return 0

        self.total = 0
        self._find_all_subsets(n, [], 1)
        return self.total

    def _find_all_subsets(self, n, tmp, start):
        self.total += sum(tmp)

        for i in range(start, n + 1):
            tmp.append(i)
            self._find_all_subsets(n, tmp, i + 1)
            tmp.pop()
```