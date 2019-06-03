# 4. Ugly Number II

**Description**

Ugly number is a number that only have prime factors `2`, `3` and `5`.

Design an algorithm to find the nth ugly number. The first `10` ugly numbers are `1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...`

> Note that `1` is typically treated as an ugly number.

**Example**

Example 1:

```
Input: 9
Output: 10
```

Example 2:

```
Input: 1
Output: 1
```

**Challenge**

`O(n log n)` or `O(n)` time.


**Priority Queue**

用到新的数据结构 `priority queue`, python 中使用 heap 来实现的 (准确说是 min heap, 小顶堆)

先在 `pq` 里面放进 `1`, 然后每次从 `pq` `pop` 出来的数字分别乘 `2` `3` `5` 在 `push` 进去, 因为是 `priority queue` 会保持一个 `升序` 的状态, 同时维持一个 `set` 用来去重

```python
from heapq import heappush, heappop


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        pq = []
        history = set()
        history.add(1)
        heappush(pq, 1)

        count, res = 0, -1
        while count < n:
            res = heappop(pq)
            count += 1
            nums = [res * 2, res * 3, res * 5]
            for i in nums:
                if i not in history:
                    history.add(i)
                    heappush(pq, i)
        return res
```