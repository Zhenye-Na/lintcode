# 437. Copy Books

**Description**

Given n books and the i-th book has `pages[i]` pages. There are `k` persons to copy these books.

These books list in a row and each person can claim a continous range of books. For example, one copier can copy the books from `i`-th to `j`-th **continously**, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost `1` minute to copy `1` page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?

Return the **shortest time** that the slowest copier spends.


**Example**

Example 1:
```
Input: pages = [3, 2, 4], k = 2
Output: 5
Explanation: 
    First person spends 5 minutes to copy book 1 and book 2.
    Second person spends 4 minutes to copy book 3.
```

Example 2:

```
Input: pages = [3, 2, 4], k = 3
Output: 4
Explanation: Each person copies one of the books.
```


**Challenge**

`O(nk)` time


* * *

This problem can be solved by `binary search` and `dynamic programming`.


**Binary Search**

- use a function to compute `number of workers needed` for specific time.
- if `# of workers > k`, this means in order to finish on time, more workers is needed -> actual time is larger, increase
- if `# of workers <= k`, this could be done without using `k` workers, instead finishing time could be smaller


```python
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages or len(pages) == 0 or not k or k == 0:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self._compute_k(pages, mid) > k:
                start = mid
            else:
                end = mid

        if self._compute_k(pages, start) <= k:
            return start
        else:
            return end



    def _compute_k(self, pages, target):
        worker = 1
        time = 0
        for i in range(len(pages)):
            if time + pages[i] > target:
                time = pages[i]
                worker += 1
            else:
                time += pages[i]

        return worker
```



**Dynamic Programming**

TODO:

```python
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copyBooks(self, pages, k):
        n = len(pages)
        if k > n:
            k = n

        if n == 0:
            return 0

        sum = [0] * n
        sum[0] = pages[0]
        for i in range(1, n):
            sum[i] = sum[i - 1] + pages[i]

        f = [[0] * k for _ in range(n)]

        for i in range(n):
            f[i][0] = sum[i]

        for j in range(1, k):
            p = 0
            f[0][j] = pages[0]
            for i in range(1, j):
                f[i][j] = max(f[i - 1][j], pages[i])

            for i in range(j, n):
                while (p < i and f[p][j - 1] < sum[i] - sum[p]):
                    p += 1
                f[i][j] = max(f[p][j - 1], sum[i] - sum[p])
                if p > 0:
                    p -= 1
                f[i][j] = min(f[i][j], max(f[p][j - 1], sum[i] - sum[p]))
        return f[n-1][k-1]
```
