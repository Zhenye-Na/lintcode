# 124. Longest Consecutive Sequence

**Description**

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

**Clarification**

Your algorithm should run in `O(n)` complexity.

Example

```
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
```

**HashMap**

```python
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        max_len = 0
        if not num or len(num) == 0:
            return max_len

        mapping = {number:True for number in num}
        for i in range(len(num)):
            if num[i] - 1 not in mapping:
                left, right = num[i], num[i] + 1
                while right in mapping:
                    right += 1
                max_len = max(max_len, right - left)
        # no else, because if num[i] - 1 in mapping, we have already compute this number in previous computation in the for loop

        return max_len

```


**HashMap - TLE Failed**

```python
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        if not num or len(num) == 0:
            return 0

        mapping = {}
        for i in range(len(num)):
            if num[i] not in mapping:
                mapping[num[i]] = 1

            if num[i] - 1 in mapping:
                mapping[num[i]] = mapping[num[i] - 1] + 1

            cur_num, next_num = num[i], num[i] + 1
            while next_num in mapping:
                mapping[next_num] = mapping[cur_num] + 1
                cur_num, next_num = next_num, next_num + 1

        length = sorted(mapping.items(), key=lambda kv: kv[1])

        return length[-1][1]
```
