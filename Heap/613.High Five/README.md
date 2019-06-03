# 613. High Five

**Description**

There are two properties in the node student `id` and `scores`, to ensure that each student will have at least `5` points, find the average of `5` highest scores for each person.

**Example**

Example 1:

```
Input: 
[[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
Output:
1: 72.40
2: 97.40
```

Example 2:

```
Input:
[[1,90],[1,90],[1,90],[1,90],[1,90],[1,90]]
Output: 
1: 90.00
```

**heapq and defaultdict**

```python
import heapq
from collections import defaultdict

'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        scores = defaultdict(list)
        for result in results:
            scores[result.id].append(result.score)

        avg = {}
        for student_id in scores:
            if len(scores[student_id]) >= 5:
                avg[student_id] = sum(heapq.nlargest(5, scores[student_id])) / 5
            else:
                avg[student_id] = sum(heapq.nlargest(len(scores[student_id]), scores[student_id])) / len(scores[student_id])

        return avg
```