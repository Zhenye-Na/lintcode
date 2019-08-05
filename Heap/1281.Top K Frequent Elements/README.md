# 1281. Top K Frequent Elements

**Description**

Given a non-empty array of integers, return the k most frequent elements.

```
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
```

**Example**

Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

**Heap**

```python
from heapq import heappush, heappop
from collections import Counter


class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """

    def topKFrequent(self, nums, k):
        # Write your code here
        if not nums or len(nums) == 0:
            return []

        counter = Counter(nums)
        candidates = []
        for ele in counter:
            if len(candidates) < k:
                heappush(candidates, (counter[ele], ele))
            else:
                heappush(candidates, (counter[ele], ele))
                heappop(candidates)

        res = []
        for count, ele in candidates:
            res.append(ele)

        return res

```

**collections.Counter**

合理钻空子 ~

`Counter` 这个包竟然可以直接返回答案 233

```python
from collections import Counter

class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Write your code here
        if not nums or len(nums) == 0:
            return []

        counter = Counter(nums)
        res = []
        for ele, count in counter.most_common(k):
            res.append(ele)

        return res

```