# 22. Flatten List

**Description**

Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

If the element in the given list is a list, it can contain list too.

**Example**

Example 1:

```
Input:  [[1,1],2,[1,1]]
Output: [1,1,2,1,1]

Explanation:
flatten it into a simply list with integers.
```

Example 2:

```
Input:  [1,2,[1,2]]
Output:[1,2,1,2]

Explanation:  
flatten it into a simply list with integers.
```

Example 3:

```
Input: [4,[3,[2,[1]]]]
Output:[4,3,2,1]

Explanation: 
flatten it into a simply list with integers.
```

**Challenge**

Do it in non-recursive.


**Deque**


```python
from collections import deque

class Solution(object):

    # @param nestedList a list, each element in the list can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if not nestedList or len(nestedList) == 0:
            return nestedList

        queue = deque(nestedList)
        res = []
        while queue:
            ele = queue.popleft()
            if isinstance(ele, list):
                for e in reversed(ele):
                    queue.appendleft(e)
            else:
                res.append(ele)

        return res
```
