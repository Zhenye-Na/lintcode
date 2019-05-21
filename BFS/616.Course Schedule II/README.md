# 616. Course Schedule II

**Description**

There are a total of n courses you have to take, labeled from `0` to `n - 1`.

Some courses may have prerequisites, for example to take course `0` you have to first take course `1`, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

**Example**

Example 1:

```
Input: n = 2, prerequisites = [[1,0]] 
Output: [0,1]
```

Example 2:

```
Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] 
Output: [0,1,2,3] or [0,2,1,3]
```

**BFS**

```python
from collections import deque, defaultdict

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        courseIndegree = self._getCourseIndegree(prerequisites)
        neighbors = self._getNeighbors(prerequisites)

        start_courses = [course for course in range(numCourses) if courseIndegree[course] == 0]
        queue = deque(start_courses)
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in neighbors[course]:
                courseIndegree[neighbor] -= 1
                if courseIndegree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []


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