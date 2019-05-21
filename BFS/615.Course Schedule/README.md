# 615. Course Schedule

**Description**

There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course `0` you have to first take course `1`, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

**Example**

Example 1:

```
Input: n = 2, prerequisites = [[1,0]] 
Output: true
```

Example 2:

```
Input: n = 2, prerequisites = [[1,0],[0,1]] 
Output: false
```


**BFS**

```python
from collections import deque, defaultdict


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        courseIndegree = self._getCourseIndegree(prerequisites)
        neighbors = self._getNeighbors(prerequisites)

        start_courses = [course for course in range(numCourses) if courseIndegree[course] == 0]
        queue = deque(start_courses)
        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in neighbors[course]:

                courseIndegree[neighbor] -= 1
                if courseIndegree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses

    def _getCourseIndegree(self, prerequisites):
        courseIndegree = defaultdict(int)

        for i, j in prerequisites:
            courseIndegree[i] += 1

        return courseIndegree

    def _getNeighbors(self, prerequisites):
        neighbors = defaultdict(list)

        for i, j in prerequisites:
            neighbors[j].append(i)

        return neighbors
```