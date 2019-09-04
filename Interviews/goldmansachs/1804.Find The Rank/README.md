# 1804. Find The Rank

**Description**

Give a two-dimensional array of scores to indicate the scores of each student's subjects, and find the index of the `K-th` grade of the students' total scores.

```
0 <= scores[i][j] <= 100
```

**Example**

```
Input:
scores: [[90, 80, 70], [90, 90, 90], [60, 60, 60]]
k: 2
Output: 0
Explanation:
The second in the total score is the student with index 0.
```

**Heap**

```python
from heapq import heappush, heappop


class Solution:
    """
    @param scores: two dimensional array
    @param K: a integer
    @return: return a integer
    """

    def FindTheRank(self, scores, K):
        # write your code here
        heap = []
        for idx, score in enumerate(scores):
            # keep a min-heap with size K
            total = sum(score)
            if len(heap) < K:
                heappush(heap, (total, idx))
            else:
                # len(heap) >= K
                if total >= heap[0][0]:
                    heappop(heap)
                    heappush(heap, (total, idx))

        return heap[0][1]
```

**Plain Sorting**

```python
class Solution:
    """
    @param scores: two dimensional array
    @param K: a integer
    @return: return a integer
    """
    def FindTheRank(self, scores, K):
        # write your code here
        tuple_scores = []
        for idx, score in enumerate(scores):
            tuple_scores.append([score, idx])

        sorted_scores = sorted(tuple_scores, key=lambda x: sum(x[0]))

        return sorted_scores[::-1][K - 1][1]
```