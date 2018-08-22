# 437. Copy Books

- **Description**
    - Given `n` books and the i_th book has `A[i]` pages. You are given `k` people to copy the `n` books.
    - `n` books list in a row and each person can claim a continous range of the `n` books. For example one copier can copy the books from i_th to j_th continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
    - They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
    - What's the best strategy to assign books so that the slowest copier can finish at earliest time?  
- **Example**
    - Given array `A = [3,2,4]`, `k = 2`.
    - Return `5`( First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )
- **Challenge**
    - 时间复杂度 `O(nk)`


## Solution

这题很容易想到 Binary Search 的解法，但是之所以没写出来是因为一个细节没有读懂：

- 一本书可不可以拆开由两个人一起copy，根据参考答案看是不可以的，但是我自己写的时候，是按照“可以拆开”的就导致无论如何也过不了的情况

### Python

```python
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if pages is None or len(pages) == 0:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) / 2

            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid

        if self.get_least_people(pages, start) <= k:
            return start
        return end

    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0
        # Books cannot be divided to be copied by two people
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page

        return count + 1
```
